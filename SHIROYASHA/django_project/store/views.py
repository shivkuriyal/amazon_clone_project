from django.shortcuts import render


def home(request):
    """Render the Amazon homepage clone."""
    return render(request, 'store/index.html')
