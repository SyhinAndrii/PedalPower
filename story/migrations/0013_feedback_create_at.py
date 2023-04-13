# Generated by Django 4.1.7 on 2023-04-12 19:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("story", "0012_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="create_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
