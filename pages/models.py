from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.

class category(models.Model):
    title=models.CharField(max_length=50,verbose_name=_('category'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class Book(models.Model):
    exist=(
        ('have','have'),
        ('in_order','in_order'),
        ('finish','finish'),
    )
    title=models.CharField(_("title"), max_length=100)
    description=models.TextField(_("summary"))
    author=models.CharField(_("author"), max_length=50)
    price=models.BigIntegerField(_("price (تومان)"))
    is_discount=models.BooleanField(_("is_discount"),default=False)
    price_with_discount=models.BigIntegerField(_("price_with_discount (تومان)"),null=True,blank=True)
    page_count=models.BigIntegerField(_("page count"))
    cover=models.ImageField(_("cover"), upload_to='cover/')
    category=models.ManyToManyField(category, verbose_name=_("category"),related_name='books')
    created=models.DateTimeField(_("created"),auto_now_add=True)
    updated=models.DateTimeField(_("edited"), auto_now=True)
    exist=models.CharField(max_length=8,choices=exist,default='have',verbose_name=_('exist'))
    def cover_tag(self):
            return format_html('<img width=150px height=150px src="{}" />'. format(self.cover.url))

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title

