# Generated by Django 4.1.3 on 2022-12-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_payment_method_wish'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('update_desc', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]