# Generated by Django 3.1.7 on 2021-03-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210310_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='answer',
        ),
        migrations.AddField(
            model_name='vote',
            name='answer',
            field=models.ManyToManyField(related_name='vote_answers', to='polls.Answer'),
        ),
    ]
