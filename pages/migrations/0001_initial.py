# Generated by Django 4.2.2 on 2023-06-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='summary')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('price', models.BigIntegerField(verbose_name='price')),
                ('is_discount', models.BooleanField(default=False, verbose_name='is_discount')),
                ('price_with_discount', models.BigIntegerField(blank=True, null=True, verbose_name='price_with_discount')),
                ('page_count', models.BigIntegerField(verbose_name='page count')),
                ('cover', models.ImageField(upload_to='cover/', verbose_name='cover')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='edited')),
                ('exist', models.CharField(choices=[('have', 'have'), ('in_order', 'in_order'), ('finish', 'finish')], default='have', max_length=8, verbose_name='exist')),
                ('category', models.ManyToManyField(related_name='books', to='pages.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
