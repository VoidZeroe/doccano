# Generated by Django 4.0.2 on 2022-02-22 05:12

from django.db import migrations


def copy_relation_type(apps, schema_editor):
    RelationTypeOld = apps.get_model("label_types", "RelationTypeOld")
    RelationType = apps.get_model("label_types", "RelationType")
    for relation_type in RelationTypeOld.objects.all():
        RelationType(
            background_color=relation_type.color, text=relation_type.name, project=relation_type.project
        ).save()
        relation_type.delete()


def delete_new_relation_type(apps, schema_editor):
    RelationTypeNew = apps.get_model("label_types", "RelationType")
    RelationTypeOld = apps.get_model("label_types", "RelationTypeOld")
    for relation_type in RelationTypeNew.objects.all():
        RelationTypeOld.objects.get_or_create(
            color=relation_type.background_color, name=relation_type.text, project=relation_type.project
        )
        relation_type.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("label_types", "0005_relationtype_and_more"),
    ]

    operations = [
        migrations.RunPython(code=copy_relation_type, reverse_code=delete_new_relation_type),
    ]
