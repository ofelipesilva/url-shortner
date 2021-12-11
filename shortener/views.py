from django.shortcuts import render, redirect, get_object_or_404
import uuid
from .models import URL

# Create your views here.
def index(request):
    return render(request, 'base.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['url']

        if URL.objects.filter(link=url):
            uid = get_object_or_404(URL, link=url).uuid
            return render(request, 'create_short.html', context={'short_url': uid})

        uid = str(uuid.uuid4())[:5]

        url = URL.objects.create(
            link = url,
            uuid = uid
        )
        url.save()

        request.session['short_link'] = uid
        return render(request, 'create_short.html', context={'short_url': uid})

def shortened_go(request, uuid):
    url = get_object_or_404(URL, uuid=uuid)
    short_link = url.link
    
    return redirect(short_link)
