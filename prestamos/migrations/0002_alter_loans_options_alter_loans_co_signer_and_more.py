# Generated by Django 4.2.1 on 2023-06-03 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0004_co_signer_members_co_signer'),
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loans',
            options={'verbose_name': 'Loan', 'verbose_name_plural': 'Loans'},
        ),
        migrations.AlterField(
            model_name='loans',
            name='co_signer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='socios.co_signer'),
        ),
        migrations.DeleteModel(
            name='Co_signer',
        ),
    ]
