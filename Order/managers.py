from django.db.models import Manager,Sum

class OrderManager(Manager):
    def get_total_quantity(self, user):
        orders = self.all()
        orders_user = orders.filter(user=user)
        result = orders_user.aggregate(
            total_quantity= Sum('quantity')
        )
        return result['total_quantity']