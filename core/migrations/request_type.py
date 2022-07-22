from core.utils.services import id_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'request_status')
    ]

    operations = [
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('sick_day', 'Sick day'), ('vacation', 'Vacation'), ('day_off', 'Day off')], max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Request type',
                'verbose_name_plural': 'Request types',
            }
        )
    ]
