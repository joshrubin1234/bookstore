# Generated by Django 4.2.1 on 2023-06-18 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0008_remove_wishlist_listbooks_wishlist_book_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='Book',
            new_name='Books',
        ),
    ]