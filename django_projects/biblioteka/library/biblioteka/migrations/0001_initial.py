# Generated by Django 4.0.4 on 2022-05-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='iveskite knygos zanra(pvz. veiksmo)',
                 max_length=200, verbose_name='pavadinimas')),
            ],
        ),
    ]
