from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .script_runner.script_runner import ScriptRunner

# Create your views here.

def index(request):
    object_passed_to_template = {'key': 'value'}
    template = loader.get_template('main/index.html')
    context = {
        'object_passed_to_template': object_passed_to_template,
    }
    return HttpResponse(template.render(context, request))

def run_script(request):
    sr = ScriptRunner()
    script_output = sr.run()
    template = loader.get_template('main/script_runner.html')
    context = {
        'script_output': script_output,
    }
    return HttpResponse(template.render(context, request))

