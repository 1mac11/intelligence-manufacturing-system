from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

            ],
        ),
    ]
