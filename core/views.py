from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_api.models import Url


def index(request):
    data = dict()
    return render(request, "core/index.html", data)

def url_redirect(request, link_short):

    url = get_object_or_404(Url, link_short=link_short)
    url.increase_count_clicked()
    url.save()

    print('Redirecting to '+url.get_url_redirect())

    return redirect(to=url.get_url_redirect())

def url_statistics(request, link_short):
    data = dict()
    url = get_object_or_404(Url, link_short=link_short)
    data['url'] = url

    return render(request, "core/statistics.html", data)