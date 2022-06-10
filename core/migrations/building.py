from django.db import migrations, models
from core.utils.services import id_generator


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', 'status'),
        ('core', 'building_type'),
        ('core', 'factory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.ForeignKey(to='core.BuildingType', on_delete=models.deletion.CASCADE, related_name='buildings')),
                ('status', models.ForeignKey('core.Status', on_delete=models.CASCADE, related_name='buildings')),
                ('factory', models.ForeignKey(to='core.Factory', on_delete=models.deletion.CASCADE, related_name='buildings')),

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
