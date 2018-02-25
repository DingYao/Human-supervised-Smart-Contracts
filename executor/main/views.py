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
        'user': { 'user_type': 1, 
                  'contracts': contracts,
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
    gifts = [
        {
            'number': 1,
            'recipient': 'Justin',
            'type' : 'Periodic',
            'description': 'S$50 every week',
            'total': 'S$5,200',
            'paid_out': 'S$350',
            'remaining_to_pay': 'S$4,850',
            'status': 'Active',
        },
        {
            'number': 2,
            'recipient': 'Bieber',
            'type' : 'Lumpsum',
            'description': 'S$250',
            'total': 'S$250',
            'paid_out': '-',
            'remaining_to_pay': 'S$250',
            'status': 'Active',
        },
        {
            'number': 3,
            'recipient': '小明',
            'type' : 'Periodic',
            'description': 'S$6,000 every year',
            'total': 'S$60,000',
            'paid_out': 'S$12,000',
            'remaining_to_pay': 'S$48,000',
            'status': 'Pending Approval',
        },
    ]
    context = {
        'summary' : {'Created' : '25 Feb 2018',
                     'Gifts Made': '2',
                     'Initial Amount Transferred': '20000',
                     'Remaining Balance': '10000',
                     'Owner Supervision': 'Revoke Only',
                     'Protector Supervision': 'Approval Only',
                     'SIAC Supervision': 'Revise Only',
                    },
        'gifts'  : gifts,
        'powers' : ['Revoke', 'Request Protector Review','Request SIAC Review']

    }
    return HttpResponse(template.render(context, request))
