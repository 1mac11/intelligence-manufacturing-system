from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', 'user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(choices=[('working', 'Working'), ('stopped', 'Stopped'), ('pending', 'Pending'),
                                            ('repairing', 'Repairing')], max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='factorytype',
            name='name',
            field=models.CharField(choices=[('car', 'Car'), ('food', 'Food'), ('wood', 'Wood'), ('metal', 'Metal')],
                                   max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='machinetooltype',
            name='name',
            field=models.CharField(
                choices=[('case', 'Case'), ('masher', 'Masher'), ('painting', 'Painting'), ('interior', 'Interior')],
                max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='buildingtype',
            name='name',
            field=models.CharField(choices=[('storage', 'Storage'), ('workshop', 'Workshop'), ('canteen', 'Canteen'),
                                            ('rest_zone', 'Rest zone'), ('head_office', 'Head Office')], max_length=255,
                                   unique=True),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='name',
            field=models.CharField(
                choices=[('it', 'IT'), ('manager', 'Manager'), ('supervisor', 'Supervisor'), ('worker', 'Worker'),
                         ('mechanics', 'Mechanics')], max_length=255, unique=True),
        ),
    ]
