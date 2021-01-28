import re
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect

from hello.models import LogMessage
from hello.forms import LogMessageForm

class LogMessageListView(ListView):
    model = LogMessage
    template_name = "hello/home.html"

    def get_context_data(self, **kwargs):
        context = super(LogMessageListView, self).get_context_data(**kwargs)
        return context


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect('home')
    else:
        return render(
            request,
            'hello/log_message.html',
            {
                "form": form
            }
        )

def home(request):
    # return HttpResponse("Hello, Django!")
    return render(
        request,
        'hello/home.html'
    )

def about(request):
    return render(
        request,
        'hello/about.html'
    )

def contact(request):
    return render(
        request,
        'hello/contact.html'
    )

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'now': formatted_now
        }
    )

def hello_there_old(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match('[a-zA-Z]+', name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
