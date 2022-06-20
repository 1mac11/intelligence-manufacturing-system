from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'name_choices'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'building', 'verbose_name_plural': 'buildings'},
        ),
        migrations.AlterModelOptions(
            name='buildingtype',
            options={'verbose_name': 'building type', 'verbose_name_plural': 'building types'},
        ),
        migrations.AlterModelOptions(
            name='factory',
            options={'verbose_name': 'factory', 'verbose_name_plural': 'factories'},
        ),
        migrations.AlterModelOptions(
            name='factorytype',
            options={'verbose_name': 'factory type', 'verbose_name_plural': 'factory types'},
        ),
        migrations.AlterModelOptions(
            name='machinetool',
            options={'verbose_name': 'machine tool', 'verbose_name_plural': 'machine tools'},
        ),
        migrations.AlterModelOptions(
            name='machinetooltype',
            options={'verbose_name': 'machine tool type', 'verbose_name_plural': 'machine tool types'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'status', 'verbose_name_plural': 'statuses'},
        ),
        migrations.AlterModelOptions(
            name='territory',
            options={'verbose_name': 'territory', 'verbose_name_plural': 'territories'},
        ),
        migrations.AlterModelOptions(
            name='userdetail',
            options={'verbose_name': 'user detail', 'verbose_name_plural': 'user details'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'user role', 'verbose_name_plural': 'user roles'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'building type', 'verbose_name_plural': 'building types'},
        ),
    ]
