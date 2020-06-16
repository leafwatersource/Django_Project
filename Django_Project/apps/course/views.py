from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request,'course/course.html')


def course_detail(request):
    return render(request,'course/course_detail.html')