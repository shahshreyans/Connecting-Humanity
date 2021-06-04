from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView

from .forms import RegisterNgoForm, NgoActivityForm, EditNgoProfileForm
from .models import NgoActivityModel, RegisterNgoModel


# Create your views here.

class Mainpageview(TemplateView):
    template_name = 'mainpage.html'


# Ngo views starts here

class Indexview(LoginRequiredMixin, ListView):
    model = NgoActivityModel
    context_object_name = 'activities'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ngoid = self.request.user.ngo_id
        context['activities'] = context['activities'].filter(ngo_id=ngoid)
        return context


class AddActivityview(LoginRequiredMixin, CreateView):
    model = NgoActivityModel
    form_class = NgoActivityForm
    template_name = 'addactivity.html'
    success_url = reverse_lazy('ngopages:index')

    def form_valid(self, form):
        form.instance.ngo = self.request.user
        return super(AddActivityview, self).form_valid(form)


class EditActivityview(LoginRequiredMixin, UpdateView):
    model = NgoActivityModel
    form_class = NgoActivityForm
    template_name = 'addactivity.html'
    success_url = reverse_lazy('ngopages:index')


class EditProfileview(LoginRequiredMixin, UpdateView):
    model = RegisterNgoModel
    form_class = EditNgoProfileForm
    template_name = 'editngoprofile.html'
    success_url = reverse_lazy('ngopages:index')


class DeleteActivityview(LoginRequiredMixin, DeleteView):
    model = NgoActivityModel
    context_object_name = 'activities'
    template_name = 'deleteactivity.html'
    success_url = reverse_lazy('ngopages:index')


class Loginview(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ngopages:index')


class Registerview(FormView):
    template_name = 'register.html'
    form_class = RegisterNgoForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('ngopages:index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registerview, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('ngopages:index')
        return super(Registerview, self).get(*args, **kwargs)


# User's View start here

class UserIndexview(ListView):
    model = NgoActivityModel
    context_object_name = 'activities'
    template_name = 'userhome.html'


class Povertycareview(ListView):
    model = RegisterNgoModel
    context_object_name = 'ngos'
    template_name = 'povertycare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ngos'] = context['ngos'].filter(category='No Poverty')
        return context


class Hungerreliefview(ListView):
    model = RegisterNgoModel
    context_object_name = 'ngos'
    template_name = 'hungerrelief.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ngos'] = context['ngos'].filter(category='No Hunger')
        return context


class Healthcareview(ListView):
    model = RegisterNgoModel
    context_object_name = 'ngos'
    template_name = 'healthcare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ngos'] = context['ngos'].filter(category='Good Health')
        return context


class Educationalaidsview(ListView):
    model = RegisterNgoModel
    context_object_name = 'ngos'
    template_name = 'educationalaids.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ngos'] = context['ngos'].filter(category='Quality Education')
        return context


class Ngodetailview(DetailView):
    model = RegisterNgoModel
    context_object_name = 'ngo'
    template_name = 'ngodetail.html'

