from django.shortcuts import render


def student_loginpage(request):
    return render(request, 'student/student_login.html')

def student_registrationpage(request):
    return render(request, 'student/student_registration.html')