# Generated by Django 3.0.8 on 2020-08-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products')),
                ('discount_price', models.FloatField()),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('lady', 'LADIES')], max_length=5)),
            ],
        ),
    ]