# Generated by Django 3.0.8 on 2020-08-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200819_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='library_classroom',
            new_name='announcements_group',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='library_gmail_group',
            new_name='collaboration_group',
        ),
        migrations.AddField(
            model_name='sessionslot',
            name='hangouts_link',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
