from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'machine_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='buildings', to='core.status'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='factories', to='core.status'),
        ),
        migrations.AlterField(
            model_name='machinetool',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='machine_tools', to='core.machinetooltype'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='territories', to='core.status'),
        ),
    ]
