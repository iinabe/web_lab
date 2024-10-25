# Generated by Django 4.2.5 on 2023-12-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebWater', '0004_vacancies_duties_vacancies_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='duties',
            field=models.TextField(default='Уточняйте информацию у администратора', verbose_name='Обязанности'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='requirements',
            field=models.TextField(default='Уточняйте информацию у администратора', verbose_name='Требования'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='working_conditions',
            field=models.TextField(default='Уточняйте информацию у администратора', verbose_name='Условия работы'),
        ),
    ]
