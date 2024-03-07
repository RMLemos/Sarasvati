# Generated by Django 4.2 on 2024-03-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('picture', models.ImageField(blank=True, default='', upload_to='pictures/authors/')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, unique=True, verbose_name='Slug')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('cover', models.ImageField(blank=True, default='', upload_to='pictures/cover')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('publisher', models.CharField(max_length=100, verbose_name='Publisher')),
                ('isbn', models.CharField(max_length=100, unique=True, verbose_name='ISBN')),
                ('nr_pages', models.IntegerField(blank=True, null=True, verbose_name='Pages')),
                ('synopsis', models.TextField(blank=True, null=True, verbose_name='Synopsis')),
                ('author', models.ManyToManyField(related_name='book', to='library.author', verbose_name='Author(s)')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
            },
        ),
    ]
