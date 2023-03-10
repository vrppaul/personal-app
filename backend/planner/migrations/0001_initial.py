# Generated by Django 4.1.4 on 2022-12-31 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannedPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('tasks_completed', models.PositiveSmallIntegerField(default=0)),
                ('tasks_moved', models.PositiveSmallIntegerField(default=0)),
                ('tasks_total', models.PositiveSmallIntegerField(default=0)),
                ('period_type', models.PositiveSmallIntegerField(choices=[(1, 'day'), (2, 'week'), (3, 'month'), (4, 'year')])),
            ],
        ),
        migrations.CreateModel(
            name='PlannedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('times_moved', models.PositiveSmallIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL)),
                ('planned_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planned_tasks', to='planner.plannedperiod')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
