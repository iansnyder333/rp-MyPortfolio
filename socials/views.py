from django.shortcuts import render
from socials.models import Social
# Create your views here.
def socials_index(request):
    social = Social.objects.all()
    context = {'social': social}
    return render(request, 'socials_index.html', context)
