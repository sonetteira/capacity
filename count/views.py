from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

def home(request):
    title = 'Capacity'
    template = loader.get_template('index.html')
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

def count(request, r):
    title = 'Capacity'
    current = Room.objects.get(id=r)
    template = loader.get_template('count.html')
    if request.method=='POST':
        if 'plus' in request.POST:
            current.current_capacity += 1
            current.save()
        elif 'minus' in request.POST:
            current.current_capacity -= 1
            current.save()
    context = {
        'title': title,
        'current': current.current_capacity,
    }
    return HttpResponse(template.render(context, request))

class Register(CreateView):
    title = 'Register'
    model = Org
    template_name = 'register.html'
    form_class = OrgForm
    success_url = 'home'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class AddRoom(CreateView):
    title = 'Add Room'
    model = Room
    template_name = 'register.html'
    form_class = RoomForm
    success_url = 'home'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class AddAdminUser(CreateView):
    title = 'Add Admin'
    model = User
    template_name = 'register.html'
    form_class = AdminUserForm
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        #get org from url param
        self.org = Org.objects.get(id=kwargs['org'])
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        print("we are here")
        form.instance.admin = 1
        form.instance.active = 1
        form.instance.org = self.org
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context