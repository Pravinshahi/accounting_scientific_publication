# Generated by Django 2.2.2 on 2019-06-15 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0011_type_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='ID_type_article',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Type_article'),
            preserve_default=False,
        ),
    ]
