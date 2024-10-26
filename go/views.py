from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Place, Reporter, Article, Student, Course
from .forms import RestaurantForm, PlaceForm, ReporterForm, ArticleForm, StudentForm, CourseForm


# 1-to1
def place_list(request):
    places = Place.objects.all()
    return render(request, '1-to-1/place_list.html', {'places': places})


def place_detail(request, pk):
    place = Place.objects.get(pk=pk)
    return render(request, '1-to-1/place_detail.html', {'place': place})


def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, '1-to-1/place_form.html', {'form': form})


def place_update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm(instance=place)
    return render(request, '1-to-1/place_form.html', {'form': form})


def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        place.delete()
        return redirect('place_list')
    return render(request, '1-to-1/place_confirm_delete.html', {'object': place})


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, '1-to-1/restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    return render(request, '1-to-1/restaurant_detail.html', {'restaurant': restaurant})


def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, '1-to-1/restaurant_form.html', {'form': form})


def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, '1-to-1/restaurant_form.html', {'form': form})


def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, '1-to-1/restaurant_confirm_delete.html', {'object': restaurant})


# 1-to-many
# Reporter Views
def reporter_list(request):
    reporters = Reporter.objects.all()
    return render(request, '1-to-many/reporter_list.html', {'reporters': reporters})


def reporter_create(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporter_list')
    else:
        form = ReporterForm()
    return render(request, '1-to-many/reporter_form.html', {'form': form})


def reporter_detail(request, pk):
    reporter = get_object_or_404(Reporter, pk=pk)
    return render(request, '1-to-many/reporter_detail.html', {'reporter': reporter})


def reporter_edit(request, pk):
    reporter = get_object_or_404(Reporter, pk=pk)
    if request.method == 'POST':
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('reporter_detail', pk=pk)
    else:
        form = ReporterForm(instance=reporter)
    return render(request, '1-to-many/reporter_form.html', {'form': form})


def reporter_delete(request, pk):
    reporter = get_object_or_404(Reporter, pk=pk)
    if request.method == 'POST':
        reporter.delete()
        return redirect('reporter_list')
    return render(request, '1-to-many/reporter_confirm_delete.html', {'reporter': reporter})


# Article Views
def article_list(request):
    articles = Article.objects.all()
    return render(request, '1-to-many/article_list.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, '1-to-many/article_form.html', {'form': form})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, '1-to-many/article_detail.html', {'article': article})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, '1-to-many/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, '1-to-many/article_confirm_delete.html', {'article': article})


# many-to-many
# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'many-to-many/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'many-to-many/student_detail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'many-to-many/student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'many-to-many/student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'many-to-many/student_confirm_delete.html', {'student': student})


# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'many-to-many/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'many-to-many/course_detail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the course and the many-to-many relationships
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'many-to-many/course_form.html', {'form': form})


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()  # This will save the updated course and the many-to-many relationships
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'many-to-many/course_form.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'many-to-many/course_confirm_delete.html', {'course': course})
