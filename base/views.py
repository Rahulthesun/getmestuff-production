from django.forms import BaseModelForm
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy , reverse 
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView , LogoutView 
from django.views.generic import FormView , CreateView
from django.contrib import messages

from .models import CreatorGoal , SupporterInteraction
from .forms import DonateForm , CreateGoalForm
from customauth.forms import CustomUserForm

from decimal import *
import requests , json
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.



def landing_page(request):
    return render(request, 'base/landing_page.html')

class CreatorLogin(LoginView):
    redirect_authenticated_user = True
    template_name = "base/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
    
class CreatorSignup(FormView):
    form_class = CustomUserForm
    template_name = 'base/signup.html'
    success_url = reverse_lazy("home")

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request , user)
        return super(CreatorSignup,self).form_valid(form)


@login_required
def homepage(request):
    goals = CreatorGoal.objects.filter(creator = request.user.id)
    context = {
    }
    context['goals'] = goals   
    return render(request , "base/home.html" , context)


class CreateGoal(CreateView , LoginRequiredMixin):
    form_class = CreateGoalForm
    model = CreatorGoal
    template_name = 'base/create_goal.html'
    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.item_price += form.instance.item_price * Decimal(0.05)
        return super().form_valid(form) 
    
    def get_success_url(self):
        return reverse_lazy("home")
    
@login_required
def GoalPreview(request , pk):
    context = {}
    context['goal'] = CreatorGoal.objects.get(id=pk)
    return render(request , 'base/goal_preview.html' , context)


class LiveGoalLink(FormView):
    form_class = DonateForm
    template_name = 'base/live_goal.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = CreatorGoal.objects.get(id = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):

        goal = CreatorGoal.objects.get(id = self.kwargs['pk'])
        supporter_instance = SupporterInteraction.objects.create(
            goal = goal,
            supporter_email = form.cleaned_data['email'],
        )
        custom_tip = form.cleaned_data['custom_tip']
        if custom_tip:
            supporter_instance.donation_amount = Decimal(custom_tip)
        else:
            supporter_instance.donation_amount = Decimal(form.cleaned_data['tip_amount'])

        previous_url = self.request.META.get('HTTP_REFERER', '')
        supporter_instance.redirect_link = previous_url

        supporter_instance.save()

        self.supporter_id = supporter_instance.id

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("payment" , kwargs={"pk":self.supporter_id})


def payment(request, pk):
    supporter_instance = SupporterInteraction.objects.get(id=pk)

    paypal_dict = {
        'business': 'wearaiofficial@gmail.com',
        'amount': supporter_instance.donation_amount,
        'currency_code':'USD',
        'item_name': supporter_instance.goal.channel_name  ,
        'return': request.build_absolute_uri(reverse("payment_status" , kwargs={"pk":pk})),
        'cancel_return':request.build_absolute_uri(reverse("payment_failure",kwargs={"pk":pk}))
    }
    form = PayPalPaymentsForm(initial= paypal_dict)
    context = {
        'supporter': supporter_instance ,
        'form': form
    }
    return render(request , 'base/payment.html' , context)

def payment_success(request , pk):
    supporter = SupporterInteraction.objects.get(id =pk)
    context = {
        'supporter' : supporter
    }
    return render(request , 'base/payment_success.html' , context)

def payment_failure(request , pk):
    supporter_instance = SupporterInteraction.objects.get(id=pk)
    context = {
        "live_goal_id": supporter_instance.goal.id
    }
    return render(request , 'base/payment_failure.html' , context)
    

def payment_status(request, pk):
    supporter_instance = SupporterInteraction.objects.get(id=pk)
    goal = CreatorGoal.objects.get(id = supporter_instance.goal.id)

    supporter_instance.paid = True
    supporter_instance.save()
    goal.funded_amount+= supporter_instance.donation_amount
    goal.save()
    goal.funded_percent = (goal.funded_amount / goal.item_price) *100
    goal.supporters +=1 
    goal.save()
    
            

    return redirect(reverse("payment_success" , kwargs={"pk":pk}))


            




    