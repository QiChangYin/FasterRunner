# Generated by Django 2.1.3 on 2018-12-03 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=100, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('relation', models.IntegerField(verbose_name='节点id')),
            ],
            options={
                'db_table': 'API',
                'verbose_name': '接口信息',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('relation', models.IntegerField(verbose_name='节点id')),
            ],
            options={
                'db_table': 'Case',
                'verbose_name': '用例信息',
            },
        ),
        migrations.CreateModel(
            name='CaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='用例名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=100, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('step', models.IntegerField(verbose_name='顺序')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Case')),
            ],
            options={
                'db_table': 'CaseStep',
                'verbose_name': '用例信息 Step',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='环境名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('base_url', models.CharField(max_length=100, verbose_name='请求地址')),
            ],
            options={
                'db_table': 'Config',
                'verbose_name': '环境信息',
            },
        ),
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, verbose_name='数据库名称')),
                ('server', models.CharField(max_length=100, verbose_name='服务地址')),
                ('account', models.CharField(max_length=50, verbose_name='登录名')),
                ('password', models.CharField(max_length=50, verbose_name='登陆密码')),
                ('type', models.IntegerField(choices=[(1, 'Sql Server'), (2, 'MySQL'), (3, 'Oracle'), (4, 'Mongodb'), (5, 'InfluxDB')], default=2, verbose_name='数据库类型')),
                ('desc', models.CharField(max_length=50, verbose_name='描述')),
            ],
            options={
                'db_table': 'DataBase',
                'verbose_name': '数据库信息',
            },
        ),
        migrations.CreateModel(
            name='Debugtalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(default='# write you code', verbose_name='python代码')),
            ],
            options={
                'db_table': 'Debugtalk',
                'verbose_name': '驱动库',
            },
        ),
        migrations.CreateModel(
            name='FileBinary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='文件名称')),
                ('body', models.BinaryField(verbose_name='二进制流')),
                ('size', models.CharField(max_length=30, verbose_name='大小')),
            ],
            options={
                'db_table': 'FileBinary',
                'verbose_name': '二进制文件',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='项目名称')),
                ('desc', models.CharField(max_length=100, verbose_name='简要介绍')),
                ('responsible', models.CharField(max_length=20, verbose_name='创建人')),
            ],
            options={
                'db_table': 'Project',
                'verbose_name': '项目信息',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree', models.TextField(default=[], verbose_name='结构主题')),
                ('type', models.IntegerField(default=1, verbose_name='树类型')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project')),
            ],
            options={
                'db_table': 'Relation',
                'verbose_name': '树形结构关系',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='报告名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('total', models.IntegerField(verbose_name='总共个数')),
                ('success', models.IntegerField(verbose_name='通过用例')),
                ('failure', models.IntegerField(verbose_name='失败用例')),
                ('skipped', models.IntegerField(verbose_name='跳过用例')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('duration', models.CharField(max_length=40, verbose_name='持续时间')),
            ],
            options={
                'db_table': 'Report',
                'verbose_name': '测试报告',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('account', models.CharField(max_length=20, verbose_name='账号')),
                ('permission', models.IntegerField(choices=[(1, 'admin'), (2, 'read'), (3, 'write'), (4, 'delete'), (5, 'admin')], verbose_name='权限')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project')),
            ],
            options={
                'db_table': 'Team',
                'verbose_name': '项目成员',
            },
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='config',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
    ]
