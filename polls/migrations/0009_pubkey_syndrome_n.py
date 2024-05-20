# Generated by Django 4.2.4 on 2023-08-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_syndrome_état'),
    ]

    operations = [
        migrations.CreateModel(
            name='pubkey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='syndrome',
            name='n',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]