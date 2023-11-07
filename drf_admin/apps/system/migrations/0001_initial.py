# Generated by Django 3.2.22 on 2023-11-07 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=30, verbose_name='权限名')),
                ('sign', models.CharField(max_length=30, unique=True, verbose_name='权限标识')),
                ('menu', models.BooleanField(verbose_name='是否为菜单')),
                ('method', models.CharField(blank=True, choices=[('POST', '增'), ('DELETE', '删'), ('PUT', '改'), ('PATCH', '局部改'), ('GET', '查')], default='', max_length=8, verbose_name='方法')),
                ('path', models.CharField(blank=True, default='', max_length=200, verbose_name='请求路径正则')),
                ('desc', models.CharField(blank=True, default='', max_length=30, verbose_name='权限描述')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.permissions', verbose_name='父权限')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
                'db_table': 'system_permissions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='角色')),
                ('desc', models.CharField(blank=True, default='', max_length=50, verbose_name='描述')),
                ('permissions', models.ManyToManyField(blank=True, db_table='system_roles_to_system_permissions', to='system.Permissions', verbose_name='权限')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'system_roles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='部门')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.departments', verbose_name='父部门')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
                'db_table': 'system_departments',
                'ordering': ['id'],
            },
        ),
    ]
