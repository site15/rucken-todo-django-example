# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-28 15:01
from __future__ import unicode_literals

from django.db import migrations


def add_permissions_for_pages_and_frames(apps, schema_editor):
    GroupModel = apps.get_model('auth', 'group')
    PermissionModel = apps.get_model('auth', 'permission')

    keys = ['read']
    content_types = ['themespage', 'accountpage', 'profileframe', 'adminpage', 'groupsframe', 'usersframe',
                     'projectspage']

    group = GroupModel.objects.get(name='admin')

    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)

    keys = ['read']
    content_types = ['themespage', 'accountpage', 'profileframe', 'projectspage']

    group = GroupModel.objects.get(name='user')

    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)


def add_permissions_for_entities(apps, schema_editor):
    GroupModel = apps.get_model('auth', 'group')
    PermissionModel = apps.get_model('auth', 'permission')

    keys = ['read', 'add', 'change', 'delete']
    content_types = ['group', 'permission', 'user', 'contenttype', 'todoproject', 'todotask', 'todostatus',
                     'todochange']

    group = GroupModel.objects.get(name='admin')
    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)

    keys = ['read', 'add', 'change', 'delete']
    content_types = ['todoproject', 'todotask', 'todostatus']

    group = GroupModel.objects.get(name='user')
    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)

    keys = ['read', 'add']
    content_types = ['user']

    group = GroupModel.objects.get(name='user')
    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)

    keys = ['read']
    content_types = ['todochange']

    group = GroupModel.objects.get(name='user')
    for key in keys:
        for content_type in content_types:
            permission = PermissionModel.objects.get(codename='%s_%s' % (key, content_type))
            group.permissions.add(permission)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('rucken_todo', '0002_create_groups'),
    ]

    operations = [
        migrations.RunPython(add_permissions_for_pages_and_frames),
        migrations.RunPython(add_permissions_for_entities),
    ]
