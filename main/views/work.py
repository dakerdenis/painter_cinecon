from django.shortcuts import render, get_object_or_404
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


def painting_detail(request, pk):
    painting = get_object_or_404(Painting, pk=pk, is_published=True)
    return render(request, 'main/pages/painting_detail.html', {
        'painting': painting,
    })