from rest_framework import serializers
from .models import Interviews, CourseArchive, CourseList


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviews
        fields = '__all__'

class CourseArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseArchive
        fields = ['title', 'image', 'action', 'short_content']

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = '__all__'
    