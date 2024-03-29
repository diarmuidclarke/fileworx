"""
Serializers (python objects <--> JSON format for REST endpoints)

"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FXSource, FXDestination, FXApprover, FXTaskSpec



class fx_approverlist_Serializer(serializers.Serializer):
    apprlist = serializers.ListField(
        child = serializers.CharField()
    )

class fx_files_at_src_Serializer(serializers.Serializer):
    filelist = serializers.ListField(
        child = serializers.CharField()
    )


class fx_filemeta_Serializer(serializers.Serializer):
    dictmeta = serializers.DictField(
        child = serializers.CharField()
    )

class FXSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FXSource
        fields = [ 'source_path', 'source_path_friendlyname']


class FXDestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FXDestination
        fields = [ 'dest_path', 'dest_path_friendlyname']


class FXApproverSerializer(serializers.HyperlinkedModelSerializer):
    dest = FXDestinationSerializer(many=True)
    class Meta:
        model = FXApprover
        fields = [ 'approver_userac', 'dest']


class FXTaskSpecSerializer(serializers.HyperlinkedModelSerializer):
    file_source_doc_path = FXSourceSerializer()
    dest = FXDestinationSerializer()
    class Meta:
        model = FXTaskSpec
        fields = [ 'raised_date', 'raised_by_userac','dest','file_source_doc_path']
