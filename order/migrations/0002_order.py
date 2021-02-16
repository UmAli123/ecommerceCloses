# Generated by Django 3.1.5 on 2021-02-14 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_usercloses'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delivery_name', models.TextField()),
                ('street', models.TextField()),
                ('address', models.TextField(verbose_name='Address')),
                ('Card_number', models.CharField(max_length=19, verbose_name='Card Number')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('payment_method', models.CharField(max_length=50, verbose_name='Payment Method')),
                ('date_purchased', models.DateField(auto_now=True)),
                ('last_modification', models.DateField()),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Shipping Cost')),
                ('shipping_method', models.CharField(max_length=50, verbose_name='Shipping Method')),
                ('status', models.IntegerField(verbose_name='Status')),
                ('date_finished', models.DateField(verbose_name='Dated Finished')),
                ('comments', models.TextField(verbose_name='Comments')),
                ('currency', models.CharField(default='SDG', max_length=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usercloses', verbose_name='Customer')),
            ],
        ),
    ]
