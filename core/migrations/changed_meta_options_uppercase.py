from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'changed_meta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'Building', 'verbose_name_plural': 'Buildings'},
        ),
        migrations.AlterModelOptions(
            name='buildingtype',
            options={'verbose_name': 'Building type', 'verbose_name_plural': 'Building types'},
        ),
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'Factory', 'verbose_name_plural': 'Factories'},
        ),
        migrations.AlterModelOptions(
            name='factorytype',
            options={'verbose_name': 'Factory type', 'verbose_name_plural': 'Factory types'},
        ),
        migrations.AlterModelOptions(
            name='machinetool',
            options={'verbose_name': 'Machine tool', 'verbose_name_plural': 'Machine tools'},
        ),
        migrations.AlterModelOptions(
            name='machinetooltype',
            options={'verbose_name': 'Machine tool type', 'verbose_name_plural': 'Machine tool types'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AlterModelOptions(
            name='territory',
            options={'verbose_name': 'Territory', 'verbose_name_plural': 'Territories'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='userdetail',
            options={'verbose_name': 'User Detail', 'verbose_name_plural': 'User Details'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'User Role', 'verbose_name_plural': 'User Roles'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'User type', 'verbose_name_plural': 'User types'},
        ),
    ]
