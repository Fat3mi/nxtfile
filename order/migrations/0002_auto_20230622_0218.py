# Generated by Django 3.2.19 on 2023-06-21 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('paid', '-updated'), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': 'OrderInfo', 'verbose_name_plural': 'OrderInfos'},
        ),
        migrations.AlterField(
            model_name='order',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='سفارش', to='order.orderinfo', verbose_name='info'),
        ),
    ]
