from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='approve_count',
        ),
        migrations.AddField(
            model_name='request',
            name='approves',
            field=models.JSONField(default=dict),
        ),
    ]