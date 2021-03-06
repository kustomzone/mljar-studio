from rest_framework import serializers
import apps.projects.models as models


class ProjectSerializer(serializers.ModelSerializer):

    created_by_username = serializers.SerializerMethodField(read_only=True)
    scripts_cnt = serializers.SerializerMethodField(read_only=True)
    uploaded_files_cnt = serializers.SerializerMethodField(read_only=True)

    def get_created_by_username(self, project):
        return "user"

    def get_uploaded_files_cnt(self, project):
        return models.File.objects.filter(
            parent_project=project, location="uploaded"
        ).count()

    def get_scripts_cnt(self, project):
        return models.Script.objects.filter(parent_project=project).count()

    class Meta:
        model = models.Project
        read_only_fields = (
            "id",
            "slug",
            "created_by",
            "created_at",
            "updated_at",
            "created_by_username",
            "scripts_cnt",
            "uploaded_files_cnt",
        )
        fields = read_only_fields + ("title", "description",)


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Script
        read_only_fields = (
            "id",
            "slug",
            "created_by",
            "created_at",
            "updated_at",
        )
        fields = (
            "id",
            "slug",
            "created_by",
            "created_at",
            "updated_at",
            "title",
            "code",
            "notebook_file",
            "script_file",
        )


class ScriptCellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Script
        read_only_fields = ("code",)
        fields = ("code",)


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Widget
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
        )
        fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "widgetUid",
            "widget_type",
            "data",
            "style",
            "layout",
            "cellUid",
            "visible",
        )


class AppShareLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AppShareLink
        read_only_fields = ("uid", "config")
        fields = ("uid", "config")


class FileSerializer(serializers.ModelSerializer):
    created_by_username = serializers.SerializerMethodField(read_only=True)

    def get_created_by_username(self, project):
        return "user"

    class Meta:
        model = models.File
        read_only_fields = (
            "id",
            "created_by",
            "created_at",
            "updated_at",
            "created_by_username",
        )
        fields = read_only_fields + (
            "title",
            "description",
            "location",
            "file_name",
            "file_size",
        )
