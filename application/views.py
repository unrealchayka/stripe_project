import stripe
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.http import JsonResponse

from .models import Item, Order
from pyment import settings
from django.http import JsonResponse


class ItemView(View):
    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        return render(request, 'Item.html', locals())


class BuyItemView(View):
    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        total = item.price
        if item.currency == 'rub':
             total = total * 100
        session = stripe.checkout.Session.create(
        payment_method_types=['card'],
            api_key=settings.SRTIPE_SECRET_KEY,
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                        },
                    'unit_amount': total,
                    },
                'quantity': 1,
                }],
            mode='payment',
        success_url='http://localhost:8000/success.html',
        cancel_url='http://localhost:8000/cancel.html',
        )        
        return JsonResponse({'session_id': session.id})


class OrderView(View):
    def get(self, request, pk):
        item = Order.objects.get(id=pk)
        return render(request, 'order.html', locals())


class BuyOrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        total = 0 
        for i in order.items.all():
            total += i.price
        if order.currency == 'rub':
            total = total * 100
        session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        api_key=settings.SRTIPE_SECRET_KEY,
        line_items=[{
            'price_data': {
                'currency': order.currency,
                'product_data': {
                    'name': 'Корзина товаров',
                    },
                'unit_amount': total,
                },
            'quantity': 1,
            }],
        mode='payment',
        success_url='http://localhost:8000/success.html',
        cancel_url='http://localhost:8000/cancel.html',
        )        
        return JsonResponse({'session_id': session.id})



