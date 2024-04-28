from .models import Order


def get_total_quantity(request):
    if request.user.is_authenticated:
        
        total_quantity = Order.objects.get_total_quantity(request.user)
        return {'total_quantity' :total_quantity}
    return {"total_quantity" : 0}   