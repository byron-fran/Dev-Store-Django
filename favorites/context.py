from .models import Favorite

def total_favs(request):
    if request.user.is_authenticated:
        
        count_favs = Favorite.objects.filter(user=request.user).count()
        return {
            'total_favs' : count_favs
        }
    return {
        "total_favs" : 0
    }    