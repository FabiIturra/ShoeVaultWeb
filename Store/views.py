from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import qrcode


def index_view(request):
    user_agent = get_user_agent(request)

    is_movile = user_agent.is_mobile or user_agent.is_tablet
    is_notebook = not is_movile

    context = {
        'is_notebook': is_notebook,
        'is_phone': is_movile,
    }

    return render(request, 'index.html', context)

def generate_qr(request):
    qr_url = 'https://drive.usercontent.google.com/download?id=1OOt8fg5IC1aahvW2Q4GQArv4Na4xdN5l&export=download&authuser=0'

    qr = qrcode.make(qr_url)

    qr_image = BytesIO()
    qr.save(qr_image)
    qr_image.seek(0)

    return HttpResponse(qr_image, content_type="image/png")
