from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

import braintree

from apps.orders.models import Order


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    settings.BRAINTREE_MERCHANT_ID,
    settings.BRAINTREE_PUBLIC_KEY,
    settings.BRAINTREE_PRIVATE_KEY
)


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {'submit_for_settlement': True}
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('done')
        else:
            return redirect('canceled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request, 'payments/process.html', locals())


def done_payment(request):
    return render(request, 'payments/done.html')


def canceled_payment(request):
    return render(request, 'payments/canceled.html')