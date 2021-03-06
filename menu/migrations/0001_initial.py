# Generated by Django 3.0.3 on 2020-03-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_title', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('named_url', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('sub_menu_title', models.CharField(max_length=64)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.SubMenu')),
            ],
        ),
    ]
