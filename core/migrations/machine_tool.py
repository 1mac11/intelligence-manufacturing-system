from django.db import migrations, models
from core.utils.services import id_generator


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', 'status'),
        ('core', 'machine_tool_type'),
        ('core', 'building'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.ForeignKey(to='core.MachineToolType', on_delete=models.deletion.CASCADE,
                                           related_name='machine_tools')),
                ('status', models.ForeignKey('core.Status', on_delete=models.CASCADE, related_name='machine_tools')),
                ('building', models.ForeignKey(to='core.Building', on_delete=models.deletion.CASCADE,
                                               related_name='machine_tools')),

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
