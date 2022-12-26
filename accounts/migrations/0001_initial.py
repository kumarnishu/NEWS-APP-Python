# Generated by Django 4.1.3 on 2022-12-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=155, unique=True)),
                ('email', models.EmailField(max_length=155, unique=True)),
                ('name', models.CharField(blank=True, max_length=155, null=True)),
                ('dp', models.ImageField(blank=True, null=True, upload_to='dp/images')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True, verbose_name='date joined')),
                ('password_reset_token', models.TextField(blank=True, max_length=500, null=True)),
                ('password_reset_token_expire', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]