from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KEwzcAMxik52sBxgsmD6AZ0JHPZUy4TZ7vflv0Z8xU66rvoExTMQblwT5KuwJ8e0YKoBqPh8raxtl6AweH389jk00cGP004cX',
        'client_secret': 'test client secret',
    }

    return render (request, template, context)