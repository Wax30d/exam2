from django import forms
from .models import Restaurant, Place, Reporter, Article, Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'students']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['place', 'serves_hot_dogs', 'serves_pizza']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'address']


class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ['first_name', 'last_name', 'email']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'pub_date', 'reporter']
