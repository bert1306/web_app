from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
import datetime

def scbeton(request):
    return render(request, 'aliancestroyrb/index.html')