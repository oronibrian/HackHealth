from __future__ import unicode_literals

from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    #equests.get('https://play.dhis2.org/release1/api/organisationUnits.json?paging=false', auth=('admin', 'district'))

    url = "https://play.dhis2.org/release1/api/organisationUnits.json? paging=false&fields=name,code,level"


    response = requests.get(url, auth=('admin', 'district'))

    data = (response.json())

    title ='Home Page'
    context={
        'title':title,
    }
    return render(request, 'index.html',{'objects': data['organisationUnits']})
