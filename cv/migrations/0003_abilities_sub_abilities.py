# Generated by Django 4.0.6 on 2022-07-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_remove_certifications_me_certifica_ended_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ablt_name', models.CharField(blank=True, max_length=50)),
                ('ablt_image', models.ImageField(blank=True, upload_to='')),
                ('ablt_experience', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_ablt_name', models.CharField(blank=True, max_length=50)),
                ('sub_ablt_image', models.ImageField(blank=True, upload_to='')),
                ('sub_ablt_experience', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]