from django.shortcuts import render, get_object_or_404
from main.models import Painting


def single_work(request, pk):
    painting = get_object_or_404(Painting, pk=pk, is_published=True)
    return render(request, 'main/pages/single_work.html', {
        'painting': painting,
    })