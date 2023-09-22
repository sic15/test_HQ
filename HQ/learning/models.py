from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Product(models.Model):
   owner = models.CharField(max_length=30, verbose_name='Владелец')
   title = models.CharField(max_length=50, verbose_name='Название курса')

   def __str__(self):
       return self.title

class Student(AbstractUser):
    products = models.ManyToManyField(Product, related_name='products')
    username = models.CharField(
        max_length=40,
        verbose_name='Ник',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='email',
    )

    def __str__(self):
       return self.username

class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField()
    viewing = models.IntegerField(verbose_name='Продолжительность')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='lessons')
    student_time=models.ManyToManyField(Student, through='TimeInfo')

    def __str__(self):
       return self.title

class TimeInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson')
    viewing_duration = models.IntegerField(verbose_name='Продолжительность просмотра')
    viewing_time = models.TimeField(verbose_name='Время просмотра') 

    def __str__(self):
       return f'{self.student.username} посмотрел {self.viewing_time} секунд из {self.lesson.title}'
