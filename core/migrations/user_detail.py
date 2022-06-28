from core.utils.services import id_generator
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'user_type'),
        ('core', 'user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('unique_code', models.CharField(default=id_generator, max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True)),
                ('level', models.CharField(
                    choices=[('trainee', 'Trainee'), ('junior', 'Junior'), ('middle', 'Middle'), ('senior', 'Senior'),
                             ('team_lead', 'Team Lead'), ('tech_lead', 'Tech Lead'), ('head', 'Head of Department')],
                    max_length=100)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=models.deletion.SET_NULL,
                                           related_name='users', to='core.UserType')),
                ('user', models.OneToOneField(on_delete=models.deletion.CASCADE, related_name='detail',
                                              to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        )
    ]
