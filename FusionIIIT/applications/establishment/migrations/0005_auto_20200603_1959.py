# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-03 19:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establishment', '0004_auto_20200530_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment_variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='CPDA_bills',
            new_name='Cpda_bill',
        ),
        migrations.RemoveField(
            model_name='cpda_tracking',
            name='id',
        ),
        migrations.AlterField(
            model_name='cpda_tracking',
            name='application',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tracking_info', serialize=False, to='establishment.Cpda_application'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cpda_tracking',
            name='review_status',
            field=models.CharField(choices=[('to_assign', 'To Assign'), ('under_review', 'Under Review'), ('reviewed', 'Reviewed')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cpda_tracking',
            name='reviewer_design',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.Designation'),
        ),
        migrations.AlterField(
            model_name='cpda_tracking',
            name='reviewer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
