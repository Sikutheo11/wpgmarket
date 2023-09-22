from .models import Category


def Product_links(request):
    links = Category.objects.all()
    return dict(links=links)