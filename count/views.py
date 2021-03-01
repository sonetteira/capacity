from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *
from django.core.exceptions import ValidationError

def home(request):
    title = 'Capacity'
    template = loader.get_template('index.html')
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

def login(request):
    title = 'Login'
    template = loader.get_template('login.html')
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(uname=request.POST["uname"], password=request.POST["password"], active=1)
            request.session['user'] = user.uname
            request.session['admin'] = user.admin
            if user.admin == 1:
                return HttpResponseRedirect(reverse('controlPanel'))  
            return HttpResponseRedirect(reverse('count'))
    else:
        form = LoginForm()
    context = {
        'title': title,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    if 'admin' in request.session:
        del request.session['admin']
    return HttpResponseRedirect(reverse('home'))

def control(request):
    title = 'Control Panel'
    template = loader.get_template('control.html')
    org = ''
    object_list = []
    if 'user' in request.session and request.session['admin'] == 1:
        org = User.objects.get(uname = request.session['user']).org
        object_list.append({'tbl': Room.objects.filter(org = org)})
        object_list.append({'tbl': User.objects.filter(org = org),'edit':'','add':'addRoom'})
    else:
        return HttpResponseRedirect(reverse('home'))
    context = {
        'title': title,
        'object_list': object_list,
        'org': org,
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
    def get_success_url(self, **kwargs):
        #on success, add this object as the home org for creating user
        self.usr.org = self.object
        self.usr.save()
        return reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        #get org from url param
        self.usr = User.objects.get(id=kwargs['usr'])
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class AddRoom(CreateView):
    title = 'Add Room'
    model = Room
    template_name = 'register.html'
    form_class = RoomForm
    success_url = 'controlPanel'
    def dispatch(self, request, *args, **kwargs):
        if 'user' in request.session and request.session['admin'] == 1:
            self.user = request.session['user']
            self.admin = request.session['admin']
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class AddAdminUser(CreateView):
    title = 'Add Admin'
    model = User
    template_name = 'register.html'
    form_class = AdminUserForm
    def get_success_url(self, **kwargs):
        self.request.session['user'] = self.object.uname
        self.request.session['admin'] = 1
        return reverse_lazy('register', kwargs={'usr': self.object.id})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context