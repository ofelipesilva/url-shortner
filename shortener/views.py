from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import URL

# Create your views here.
def index(request):
    return render(request, 'base.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['url']
        uid = str(uuid.uuid4())[:5]

    url = URL.objects.create(
        link = url,
        uuid = uid
    )
    url.save()

    request.session['short_link'] = uid
    return redirect('shortener:index')

def shortened_go(request, uuid):
    url = get_object_or_404(URL, uuid=uuid)
    short_link = url.link
    
    return redirect(short_link)
