from django.shortcuts import render
from rest_framework import serializers
from learning.models import Product, Lesson, TimeInfo, Student

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TimeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeInfo
        fields = '__all__'#('student', 'lesson')

class Lesson1Serializer(serializers.ModelSerializer):
  #  student_time = TimeInfoSerializer(many=True, read_only=True)
  #  student_time = serializers.HyperlinkedRelatedField(many=True,
   #     read_only=True,
   #     view_name='time-detail')
    class Meta:
        model = Lesson
        fields = ('title', 'url', 'viewing', 'student_time')

class ProductSerializer(serializers.ModelSerializer):
    lessons = Lesson1Serializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ("id", "owner", "title", 'lessons')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Student
        fields = ('products',)

class StatisticSerializer(serializers.ModelSerializer):
    sum_viewing = serializers.SerializerMethodField(source='Суммарное просмотренное время')
    
    class Meta:
        model = Product
        fields = ('sum_viewing',)