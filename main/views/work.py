from django.shortcuts import render
from main.models import Painting, Category


def work(request):
    paintings = Painting.objects.filter(is_published=True)
    categories = Category.objects.all()

    active_category = request.GET.get('category')
    if active_category:
        paintings = paintings.filter(category__slug=active_category)

    return render(request, 'main/pages/work.html', {
        'paintings': paintings,
        'categories': categories,
        'active_category': active_category,
    })