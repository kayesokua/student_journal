# Generated by Django 3.2.5 on 2021-08-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_total_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit_count_fake',
            field=models.IntegerField(default=0),
        ),
    ]
