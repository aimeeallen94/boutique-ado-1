from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Oxu6GAIPqmQP3IqLe7rxQmO2TXXNd1XkjaPmpFvHYo9Z8DxsKNkY8FwaaK6W7cN4tIH6nLBIZPK9WRRMMncsWAr00Ya3W8wLN',
        'client_secret': 'client secret key',
    }

    return render(request, template, context)