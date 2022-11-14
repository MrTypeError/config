from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse
from .models import Shortner
from .forms import ShortnerFrom


# Create your views here.

def home(request):
    tmplt = "home.html"
    context = {}
    context["form"] = ShortnerFrom()

    if request.method == "GET":
        myObj = Shortner()
        context["times_followed"] = myObj.times_followed
        return render(request, tmplt, context)

    elif request.method == "POST":
        formObj = ShortnerFrom(request.POST)

        if formObj.is_valid():
            shortUrl = formObj.save()
            reDirect_Url = request.build_absolute_uri("/") + shortUrl.short_url
            long_url = shortUrl.long_url
            context["redirect_url"] = reDirect_Url
            context["long_url"] = long_url
            return render(request, tmplt, context)

        context["error"] = formObj.errors
        return render(request, tmplt, context)


def redirectUrl(request, shortUrl):
    try:
        shortnerObj = Shortner.objects.get(short_url=shortUrl)
        shortnerObj.times_followed += 1
        shortnerObj.save
        return HttpResponseRedirect(shortnerObj.long_url)
        # return HttpResponseRedirect("https://www.google.com")
    except Exception as e:
        pass
    # TODO - Handle 404
