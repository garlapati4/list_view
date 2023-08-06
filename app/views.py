from django.shortcuts import render
from django.views.generic import ListView
from app.models import *

# Create your views here.
class Trainer_List(ListView):
    model=Trainers
    template_name='Trainer_List.html'
    context_object_name='tl'
