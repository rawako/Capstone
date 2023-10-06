from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_menu_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
