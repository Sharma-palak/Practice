# Generated by Django 2.2.2 on 2019-08-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_filter_features_filters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filters',
            name='category',
        ),
        migrations.AddField(
            model_name='filters',
            name='category',
            field=models.ManyToManyField(to='ecommerce.Category'),
        ),
        migrations.DeleteModel(
            name='Filter_Features',
        ),
    ]
