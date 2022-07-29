import platform
from urllib import request

from requests import get
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
import ipapi
import requests
import socket
import os
from django.contrib.gis.geoip2 import GeoIP2
from pytonik.Functions.ip import ip
import urllib.request
from bs4 import BeautifulSoup
import ssl
def HomeView(requests):
    x_forwarded_for = requests.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = requests.META.get('REMOTE_ADDR')

    data = ip
    # data = get('https://api.ipify.org').text
    # data = requests.META.get('REMOTE_ADDR', None)
    g = GeoIP2()
    country = g.country(data)
    city = g.city(data)
    data6 = get('https://api64.ipify.org').text
    datadet = get('http://ip-api.com/json/'+data).text
    hostname = socket.gethostname()
    ipadrr = socket.gethostbyname(hostname)
    browser = requests.META['HTTP_USER_AGENT']
    if requests.method == "POST":
        f = requests.POST.get('username')
        print("Do something")
        return redirect('now', pk=f)
    else:
     context = {"pubip": data,
               "pubip6": data6,
               "privip": ipadrr,
               "os": platform.system(),
               "browser": browser,
                "city":city,
               "country": country,
                "det": datadet
               }
     print(city)
     print(country)
     print(datadet)
     return render(requests, 'iplookup/home.html', context)

def IpLookup(requests):
    data = get('https://api.ipify.org').text
    # data = requests.META.get('REMOTE_ADDR', None)
    g = GeoIP2()
    country = g.country(data)
    city = g.city(data)

    data6 = get('https://api64.ipify.org').text
    datadet = get('http://ip-api.com/json/' + data).json
    hostname = socket.gethostname()
    ipadrr = socket.gethostbyname(hostname)
    browser = requests.META['HTTP_USER_AGENT']
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://ipwhois.io/" + data
    # html = urllib.request.urlopen(url)
    # htmlParse = BeautifulSoup(html, 'html.parser')
    # for para in htmlParse.find_all("li"):
    #     print(para.get_text())
    # print(para.zip)
    if requests.method == "POST":
        f = requests.POST.get('username')
        print("Do something")
        return redirect('now',pk=f)
    else:
     context = {"pubip": data,
               "pubip6": data6,
               "privip": ipadrr,
               "os": platform.system(),
               "browser": browser,
               "city": city,
               "country": country,
               "det": datadet,

               }
     return render(requests, 'iplookup/iplookup.html', context)
def now(requests,pk):

    data = pk
    # data = requests.META.get('REMOTE_ADDR', None)
    g = GeoIP2()
    country = g.country(data)
    city = g.city(data)

    data6 = get('https://api64.ipify.org').text
    datadet = get('http://ip-api.com/json/' + data).json
    hostname = socket.gethostname()
    ipadrr = socket.gethostbyname(hostname)
    browser = requests.META['HTTP_USER_AGENT']
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://ipwhois.io/" + data
    if requests.method == "POST":
        f = requests.POST.get('username')
        print("Do something")
        return redirect('now', pk=f)
    else:

     context = {"pubip": data,
               "pubip6": data6,
               "privip": ipadrr,
               "os": platform.system(),
               "browser": browser,
               "city": city,
               "country": country,
               "det": datadet,

               }
     return render(requests, 'iplookup/now.html', context)

