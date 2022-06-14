from django.db import migrations, models
import django_countries.fields
from core.utils.services import id_generator


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', 'status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('area', models.FloatField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('status', models.ForeignKey(to='core.Status', on_delete=models.deletion.CASCADE,
                                             related_name='territories')),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
