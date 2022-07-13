from core.utils.services import id_generator
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'request_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, related_name='requests', to='core.requeststatus')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, related_name='requests', to='core.requesttype')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
