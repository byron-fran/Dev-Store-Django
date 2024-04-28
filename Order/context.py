from .models import Order


def get_total_quantity(request):
    
    total_quantity = Order.objects.get_total_quantity(request.user)
    
    return {
        'total_quantity' :total_quantity
    }