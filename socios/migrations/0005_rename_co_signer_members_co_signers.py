# Generated by Django 4.2.1 on 2023-06-03 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0004_co_signer_members_co_signer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='co_signer',
            new_name='co_signers',
        ),
    ]
