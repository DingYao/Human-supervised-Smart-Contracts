from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    object_passed_to_template = {'key': 'value'}
    template = loader.get_template('main/index.html')
    context = {
        'object_passed_to_template': object_passed_to_template,
    }
    return HttpResponse(template.render(context, request))

def usrDashboard(request):
    template = loader.get_template('main/usr_dashboard.html')
    context = {
        'user': { 'user_type': 1, 
                  'notifications': ['Contract u203917731232aadsasdae3ada has paid out $1000 to Justin as scheduled on 21/11/2017', 
                                    'Protector psd2132183572132135 has begun reviewing Contract u203917731232aadsasdae3ada', 
                                    ],
                  'actions' : ['Revoke', 'Revoke']
                },
    }
    return HttpResponse(template.render(context, request))

def ptrDashboard(request):
    template = loader.get_template('main/ptr_dashboard.html')
    contracts = [
        {
            'address': 'ujorda',
            'date_created': '13/12/2099',
            'current_balance': 'S$14,842.00',
            'latest_event': 'Pending approval from requisite protectors',
            'current_status': 'active',
        },
        {
            'address': 'ea8ac',
            'date_created': '13/12/2099',
            'current_balance': 'S$19,018.00',
            'latest_event': 'Upcoming disbursement in two (2) weeks',
            'current_status': 'active',
        },
        {
            'address': 'ea8ac',
            'date_created': '13/06/2029',
            'current_balance': 'S$392.00',
            'latest_event': 'Disbursed S$1,000.00 last Thursday',
            'current_status': 'revoked',
        },
    ]
    context = {
        'user': { 'user_type': 2,
                  'contracts': contracts,
                },
    }
    return HttpResponse(template.render(context, request))

def crtDashboard(request):
    template = loader.get_template('main/crt_dashboard.html')
    context = {
        'user': { 'user_type': 3 },
    }
    return HttpResponse(template.render(context, request))

def contractDetail(request):
    template = loader.get_template('main/contract_detail.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
