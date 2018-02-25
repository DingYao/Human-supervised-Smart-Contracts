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
                  'notifications': ['Contract u2039 has paid out $1000 to Justin as scheduled on 21/11/2017', 
                                    'Protector psd21 has begun reviewing Contract u2039', 
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
                  'actions' : ['Approve', 'Review'] 
                },
    }
    return HttpResponse(template.render(context, request))

def crtDashboard(request):
    template = loader.get_template('main/crt_dashboard.html')
    context = {
        'user': { 'user_type': 3, 
                  'notifications': ['Contract 123ea has requested SIAC review citing: \"Help I forgot my private key\"', 
                                    'Contract glh18 has requested SIAC review citing: \"Please help me revoke a frustrated contract\"',
                                    'Contract h4xor has requested SIAC review citing: \"Monies paid out twice. Code is buggy\"', 
                                    'Contract 3152a has requested SIAC to be revoked citing: \"Was defrauded to enter smart contract!\"',
                                    'Contract we412 has requested SIAC review citing: \"Was defrauded to enter smart contract!\"', 
                                    ],
                  'actions' : ['Ignore', 'Review', 'Ignore', 'Revoke', 'Ignore']
                },
    }
    return HttpResponse(template.render(context, request))

def contractDetail(request):
    template = loader.get_template('main/contract_detail.html')
    context = {
        'summary' : {'Created' : '25 Feb 2018',
                     'Gifts Made': '2',
                     'Initial Amount Transferred': '20000',
                     'Remaining Balance': '10000',
                     'Owner Supervision': 'Revoke Only',
                     'Protector Supervision': 'Approval Only',
                     'SIAC Supervision': 'Revise Only',
                    }

    }
    return HttpResponse(template.render(context, request))
