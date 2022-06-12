from django.db import migrations, models

from core.utils.services import id_generator


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'user_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Team name')),
                ('users', models.ManyToManyField('core.User', related_name='teams')),
                ('status', models.ForeignKey('core.Status', on_delete=models.SET_NULL, related_name='teams', blank=True, null=True)),
                ('machine_tool', models.ForeignKey('core.MachineTool', on_delete=models.SET_NULL, related_name='teams', blank=True, null=True)),
                ('building', models.ForeignKey('core.Building', on_delete=models.SET_NULL, related_name='teams', blank=True, null=True))
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
                'abstract': False,
            },
        )
    ]