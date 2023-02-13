from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from main.settings import STRIPE_API_KEY
from .models import Item
import stripe


class ItemView(TemplateView):
    template_name = "stripe_test_task/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, pk=kwargs['pk'])
        return context


class BuyView(View):

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        stripe.api_key = STRIPE_API_KEY
        url = f'{request.scheme}://{request.get_host()}/'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': get_amount(item.price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'{url}success/',
            cancel_url=f'{url}cancel/',
        )

        return JsonResponse({'id': session.id})


class SuccessView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(f'OK!')


class CancelView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(f"NOT OK :,-(")


def get_amount(price: float) -> int:
    return int(price*100)
