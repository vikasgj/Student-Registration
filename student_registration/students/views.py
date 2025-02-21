from django.shortcuts import render , redirect , get_object_or_404

from .forms import StudentForm
from .models import Student


def register_student(request):
    if request.method =='POST' :
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
            form=StudentForm()
    return render(request,'students/register.html',{'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',{'students':students})

def student_details(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_details.html',{'student':student})




