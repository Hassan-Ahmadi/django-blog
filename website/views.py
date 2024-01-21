from django.shortcuts import render

# Create your views here.
# custom 404 view
def custom_404(request, exception):
    return render(request, 'website/404-page.html', status=404)