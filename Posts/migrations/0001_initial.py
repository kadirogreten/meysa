# Generated by Django 3.0.6 on 2021-02-06 16:49

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Post Başlığı')),
                ('slug', models.SlugField(editable=False, max_length=350, unique=True, verbose_name='Post urlsi')),
                ('author', models.CharField(max_length=200, verbose_name='Yazar')),
                ('row', models.IntegerField(unique=True, verbose_name='Post Sırası')),
                ('post_image', models.ImageField(upload_to='', verbose_name='Post Resmi')),
                ('reels_video', models.FileField(blank=True, upload_to='', verbose_name='Video Reels')),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Post Detayı')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('IsShowHome', models.BooleanField(default=False, verbose_name='Banner Slider Göster')),
                ('IsShowTopSlider', models.BooleanField(default=False, verbose_name='Anasayfada Üst Slider Göster')),
                ('IsShowMidSlider', models.BooleanField(default=False, verbose_name='Anasayfada Orta Slider Göster')),
                ('post_type', models.CharField(choices=[('R', 'Reels'), ('P', 'Post'), ('S', 'Story'), ('O', 'Diğer')], default='O', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at', 'id'],
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Kategori Adı')),
                ('row', models.IntegerField(unique=True, verbose_name='Kategori Sırası')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True, verbose_name='Post Kategorisi urlsi')),
                ('IsShowMenu', models.BooleanField(default=False, verbose_name='Menüde Göster')),
                ('IsShowHome', models.BooleanField(default=False, verbose_name='Anasayfada Göster')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
            ],
            options={
                'verbose_name_plural': 'Post Kategorileri',
                'ordering': ['row', 'id'],
            },
        ),
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Post Başlığı')),
                ('row', models.IntegerField(unique=True, verbose_name='Etiket Sırası')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
            ],
            options={
                'verbose_name_plural': 'Post Etiketleri',
                'ordering': ['-created_at', 'id'],
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Adınız Soyadınız')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('detail', ckeditor.fields.RichTextField(verbose_name='Yorum')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Zamanı')),
                ('IsShowHome', models.BooleanField(default=False, verbose_name='Onayla Göster')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='Posts.Post', verbose_name='Post Seç')),
            ],
            options={
                'verbose_name_plural': 'Post Yorumları',
                'ordering': ['-created_at', 'id'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='post', to='Posts.PostCategory', verbose_name='Kategori Seç'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='Posts.PostTags', verbose_name='Etiket Seç'),
        ),
    ]
