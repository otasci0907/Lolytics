from django.shortcuts import render, HttpResponse
from django.views import View
import cassiopeia as cass
from os import listdir
from os.path import join
from django.views.decorators.csrf import csrf_exempt

cass.set_riot_api_key("RGAPI-1c0fb75b-7645-4bc5-bf1d-f83f70a0206b")
cass.set_default_region("NA")
# Create your views here.

def index(request):
    return render(request, "summoner/index.html")

@csrf_exempt
def summonerpage(request):
    if request.method == 'GET':
        return HttpResponse("you didnt write anything bucko")
    user = request.POST.get('summonername', None)
    region = request.POST.get('summonerregion', None)
    me = cass.get_summoner(name=user, region=region)
    context = {}
    context["name"] = me.name
    context["level"] = me.level
    context["region"] = me.region
    context["icon"] = me.profile_icon.id
    return render(request, "summoner/summonerpage.html", context)