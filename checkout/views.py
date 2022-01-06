from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['sub_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KEwzcAMxik52sBxgsmD6AZ0JHPZUy4TZ7vflv0Z8xU66rvoExTMQblwT5KuwJ8e0YKoBqPh8raxtl6AweH389jk00cGP004cX',
        'client_secret': 'test client secret',
    }

    return render (request, template, context)