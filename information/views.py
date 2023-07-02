from django.shortcuts import render
from .models import AboutUs,ContactUs
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def aboutus(request):
    about=AboutUs.objects.last()
    return render(request,'information/aboutus.html',context={'about':about})

class ContactUsCreateView(LoginRequiredMixin,generic.CreateView):
    model = ContactUs
    template_name = "information/contactus.html"
    fields=['text']
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        instance.save()
        messages.success(self.request, _("your message successfuly send to us"),'success')
        return super().form_valid(form)
