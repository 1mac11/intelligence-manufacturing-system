from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'changed_meta_options_uppercase'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinetool',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET_NULL,
                                    related_name='machine_tools', to='core.team'),
        ),
        migrations.AlterField(
            model_name='machinetool',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, related_name='machine_tools',
                                    to='core.machinetooltype'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='machine_tool'
        ),
        migrations.AddField(
            model_name='team',
            name='machine_tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.deletion.SET_NULL,
                                    related_name='teams', to='core.machinetool'),
        ),
    ]
