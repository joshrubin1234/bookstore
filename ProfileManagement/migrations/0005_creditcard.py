# Generated by Django 4.2.1 on 2023-07-19 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileManagement', '0004_alter_user_address_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('expiration_date', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_cards', to='ProfileManagement.user')),
            ],
        ),
    ]