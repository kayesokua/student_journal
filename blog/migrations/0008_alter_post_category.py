# Generated by Django 3.2.5 on 2021-07-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210729_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('art-and-design', 'art-and-design'), ('assistive-technology', 'assistive-technology'), ('python-for-web', 'python-for-web'), ('python-for-data', 'python-for-data'), ('berlin-living', 'berlin-living'), ('python-programming', 'python-programming'), ('maths-and-statistics', 'maths-and-statistics')], default='uncategorized', max_length=255),
        ),
    ]
