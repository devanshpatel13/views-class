from django.shortcuts import render
from django.views.generic import DetailView
from .models import Contact

from .forms import ContactForm
from django.views.generic.edit import FormView, UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView



# Create your views here.

class ContactFormView(FormView):
    model = Contact
    form_class = ContactForm
    template_name = "App/contact_form.html"
    success_url = "/list/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        insta = form.save(commit=False)
        insta.save()
        # perform a action here
        print(form.cleaned_data)
        # form.save()
        return super().form_valid(form)
    # context_object_name = 'form'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class DoneTemplateView(TemplateView):
    template_name = "App/done.html"


#
# class ContatViews(CreateView):
#     model = Contact
#     fields = ["name","email","massage"]

class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    success_url = "/done/"


class ContactlistView(ListView):
    model = Contact


class ContactDeleteview(DeleteView):
    model = Contact
    fields ='__all__'
    success_url = "/list/"
    template_name = "App/delete.html"

    # def form_valid(self, form):
    #     inst=form.delete(commit= False)
    #     inst.delete()