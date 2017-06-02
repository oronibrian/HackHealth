from __future__ import unicode_literals

from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    #equests.get('https://play.dhis2.org/release1/api/organisationUnits.json?paging=false', auth=('admin', 'district'))

    url = "https://play.dhis2.org/release1/api/organisationUnits.json? paging=false&fields=name,code,level"

    url2 = "https://play.dhis2.org/release1/api/dataElements.json?fields=name,code"


   # url = "https://play.dhis2.org/release1/api/25/analytics.json?dimension=dx:YtbsuPPo010;l6byfWFUGaP;s46m5MS0hxu&dimension=pe:LAST_12_MONTHS&filter=ou:ImspTQPwCqd&displayProperty=NAME&skipMeta=false"



    response = requests.get(url, auth=('admin', 'district'))
    response2= requests.get(url2, auth=('admin', 'district'))


    data = (response.json())
    data2 =(response2.json())

    title ='Home Page'
    context={
        'title':title,
        'objects': data['organisationUnits'],
        'objects2': data2['dataElements']
    }
    return render(request, 'index.html',context)

def dashboard(request):

    return render(request, 'dashboard.html')


