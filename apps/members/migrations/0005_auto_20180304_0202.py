# Generated by Django 2.0.2 on 2018-03-03 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0004_remove_profile_email_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('allow_members', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', models.TextField(verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', verbose_name='ip address')),
                ('user_name', models.CharField(default='anonymous', max_length=50, verbose_name='user name')),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name='user email')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('academic_year', models.IntegerField(blank=True, null=True)),
                ('course', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('date_of_registration', models.DateField(auto_now_add=True)),
                ('date_of_expiry', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField()),
                ('bodytext', models.TextField(blank=True, verbose_name='message')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('modified', models.DateTimeField(null=True, verbose_name='modified')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('comment_count', models.IntegerField(blank=True, default=0, verbose_name='comment count')),
                ('posted_by', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='posted by')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-post_date'],
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='academic_year',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='course',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_expiry',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_registration',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='members.Post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='account',
            name='account_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_leader', to='members.Member'),
        ),
        migrations.AddField(
            model_name='account',
            name='member',
            field=models.ManyToManyField(to='members.Member'),
        ),
    ]