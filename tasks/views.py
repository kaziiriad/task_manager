from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task

from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
)

def 