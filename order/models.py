from django.db import models
from accounts.models import Customeuser
from pages.models import Book
from django.utils.translation import gettext_lazy as _

# Create your models here.

# models for save user's recieve information
class OrderInfo(models.Model):
	user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE,related_name='orderinfo')
	name=models.CharField(_("firstname"), max_length=50)
	last_name=models.CharField(_("lastname"), max_length=50)
	address=models.CharField(_("address"), max_length=400)
	phone_number=models.CharField(_("phone"), max_length=11)
	creted=models.DateTimeField(_("created"), auto_now_add=True)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = _("OrderInfo")
		verbose_name_plural = _("OrderInfos")
	

# models to save user's orders
class Order(models.Model):
	user = models.ForeignKey(Customeuser, on_delete=models.CASCADE, related_name='orders',verbose_name=_('user'))
	info=models.ForeignKey(OrderInfo, verbose_name=_("info"), on_delete=models.CASCADE,related_name=_('order'))
	paid = models.BooleanField(default=False,verbose_name=_('paid'))
	created = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))
	updated = models.DateTimeField(auto_now=True,verbose_name=_('updated'))

	class Meta:
		ordering = ('paid', '-updated')
		verbose_name = _("Order")
		verbose_name_plural = _("Orders")
	

	def __str__(self):
		return f'{self.user.username}'

	def get_total_price(self):
		total = sum(item.get_cost() for item in self.items.all())
		return total

# models to save order's each items
class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',verbose_name=_('order'))
	product = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name=_('product'))
	price = models.IntegerField(verbose_name=_('price'))
	quantity = models.IntegerField(default=1,verbose_name=_('quantity'))

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity