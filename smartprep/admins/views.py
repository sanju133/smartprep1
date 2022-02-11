from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from accounts.auth import admin_only


from materials.forms import CategoriesForm, CoursesForm, LecturesForm
from materials.models import Categories, Courses, Lectures


def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

def form(request):
    return render(request, 'admins/form.html')

def show_course(request):
    return render(request, 'admins/show_course.html')

def show_contact(request):
    return render(request, 'admins/show_contact.html')


# retrieving category form
def categories_form(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/admins/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add the category')
            return render(request, 'admins/category_form.html', {'form_category':form})
    context ={
        'form_category': CategoriesForm,

    }
    return render(request, 'admins/category_form.html', context)

#
# retrieving category
def get_category(request):
    category=Categories.objects.all().order_by('-id')

    context={
        'category':category,
        'activate_category_admin':'active'
    }
    return render(request, 'admins/get_category.html', context)



#deleting category
def delete_category(request, categories_id):
    category=Categories.objects.get(id=categories_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted!')
    return redirect('/admins/get_category/')

#
#
# # Courses Form
# def courses_form(request):
#     if request.method=='POST':
#         form=CoursesForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS, 'Course added successfully!')
#             return redirect('/admins/get_course/')
#         else:
#             messages.add_message(request, messages.ERROR, 'Unable to add the Course')
#             return render(request,'admins/course_form.html', {'form_course':form})
#     context ={
#         'form_course': CoursesForm,
#     }
#     return render(request, 'admins/course_form.html', context)
#
# # retrieving course
# def get_course(request):
#     course=Courses.objects.all().order_by('-id')
#     context={
#         'course':course,
#     }
#     return render(request, 'admins/get_course.html', context)
#
# #lectures Form
# def lectures_form(request):
#     if request.method=="POST":
#         form=LecturesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'Lecture added successfully')
#             return redirect('/admins/get_lecture/')
#         else:
#             messages.add_message(request, messages.ERROR, 'Unable to add the Lecture')
#             return render(request, 'admins/lecture_form.html', {'form_lecture': form})
#     context = {
#         'form_lecture': LecturesForm,
#     }
#     return render(request, 'admins/lecture_form.html', context)
#
# # retrieving lecture form
# def get_lecture(request):
#     lecture=Lectures.objects.all().order_by('-id')
#     context={
#         'lecture':lecture
#     }
#
#     return render(request,'admins/get_lecture.html', context)