from core.utils.services import id_generator
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True,
                                          choices=[('owner', 'Owner'),
                                                   ('admin', 'Admin'),
                                                   ('staff', 'Staff'),
                                                   ('outsource', 'Outsource')])),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        )
    ]
