from django.db import models
from accounts.models import Customeuser
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.

class AboutUs(models.Model):
    sitename=models.CharField(_("site name"), max_length=100)
    logo=models.ImageField(_("logo"), upload_to='logo/')
    description=models.TextField(_("description"))
    email=models.EmailField(_("email"), max_length=254,null=True,blank=True)
    telegram_id=models.CharField(_("telegram_id"), max_length=50,null=True,blank=True)
    whatsapp_number=models.CharField(_("whatsapp_number"), max_length=11,null=True,blank=True)
    phone_number=models.CharField(_("phone_number"), max_length=11,null=True,blank=True)
    created=models.DateTimeField(_("created"),auto_now_add=True)
    updated=models.DateTimeField(_("edited"), auto_now=True)
    

    class Meta:
        verbose_name = _("AboutUs")
        verbose_name_plural = _("AboutUs")

    def logo_tag(self):
        return format_html('<img width=150px height=150px src="{}" />'. format(self.logo.url))

    def __str__(self):
        return self.sitename

class ContactUs(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE)
    text=models.TextField(_("text"))
    created=models.DateTimeField(_("created"),auto_now_add=True)
    updated=models.DateTimeField(_("edited"), auto_now=True)

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUs")

    def __str__(self):
        return self.user.username

