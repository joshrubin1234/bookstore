# Generated by Django 4.2.1 on 2023-06-07 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0006_rename_list_books_wishlist_books_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='books',
            new_name='listbooks',
        ),
    ]
