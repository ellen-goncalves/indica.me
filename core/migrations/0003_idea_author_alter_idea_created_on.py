# Generated by Django 4.0.4 on 2022-04-28 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_idea_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação'),
        ),
    ]