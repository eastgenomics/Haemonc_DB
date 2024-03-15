# Generated by Django 4.2.7 on 2024-02-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haemonc_django_frontend', '0002_alter_variant_hgvs_nomenclature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantEn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgvs', models.CharField(max_length=255, unique=True)),
                ('gene', models.CharField(max_length=255)),
                ('disease', models.CharField(max_length=255)),
                ('frequency', models.FloatField()),
            ],
        ),
    ]
