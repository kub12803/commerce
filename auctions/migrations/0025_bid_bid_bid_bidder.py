# Generated by Django 4.1.4 on 2023-01-20 07:43

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_remove_user_watchlist_user_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Bid Amount'),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
