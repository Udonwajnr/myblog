from .models import Post,Category

def category_renderer(request):
    pass
    return {'category':Category.objects.all()}