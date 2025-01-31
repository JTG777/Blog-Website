from .models import Category


def category_processors(request):
    return {
        'categories':Category.objects.all()
    }