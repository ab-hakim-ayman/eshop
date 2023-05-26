# Generated by Django 4.1.3 on 2022-12-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_order', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('False', 'False'), ('True', 'True')], default=False, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sitecontact',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='sitecontact',
            name='start_time',
            field=models.TimeField(),
        ),
    ]