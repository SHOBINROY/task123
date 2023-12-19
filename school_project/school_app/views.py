# from django.contrib import messages
# from django.shortcuts import render
# from tkinter import *
# from tkinter import messagebox
#
#
#
# from .models import department,materials,course
#
# from django.shortcuts import render, redirect
#
# def form(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone_number = request.POST.get('phone_number')
#         mail_id = request.POST.get('mail_id')
#         address = request.POST.get('address')
#         department = request.POST.get('department')
#         course = request.POST.get('course')
#         purpose = request.POST.get('purpose')
#         materials = request.POST.getlist('materials_provided')
#         return redirect('/')
#
#         # departmentid = request.POST.get('department')
#         # courseid = request.POST.get('course')
#         # if departmentid:
#         #     department = department.objects.get(id=departmentid)
#         #     course = course.objects.filter(department=department)
#         #
#         # if courseid:
#         #     course = course.objects.get(id=courseid)
#         #     materials = materials.objects.filter(course=course)
#         #     department = department.objects.all()
#         # return render(request, 'department.html', locals())
#
#
#     else:
#         department = ['Commerce', 'Social Science', 'Arts','Computer Science','Medical']
#         course = {
#             'Commerce': ['BBA', 'BCom', 'BCOM (Hons.)'],
#         }
#         purpose = [ 'Place Order', 'Return']
#         if ['purpose'] == 'Place Order':
#             messages.info(request, 'order placed')
#         elif ['purpose'] == 'Return':
#             messages.info(request, 'order return')
#         materials_provided = ['Debit Note Book', 'Pen', 'Exam Peppers']
#
#         context = {
#             'department': department,
#             'course': course,
#             'purpose': purpose,
#             'materials_provided': materials_provided
#         }
#
#
#
#
#     return render(request, 'department.html', context)


from django.shortcuts import render
from . forms import OrderForm
from .models import Form
from django.views import View




class HomeView(View):
    def get(self, request):
        form = OrderForm()
        order = Form.objects.all()
        return render(request, 'department.html', {'order': order, 'form': form})

    def post(self, request):
            form = OrderForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                form.save();
                return render(request, 'order1.html', {'form': form})
            return HttpResponse("Invalid")



class OrderView(View):
    def get(self, request, pk):
        order = Form.objects.get(pk=pk)
        return render(request, 'school_app/order.html', {'order': order})

def index(request):
    return render(request,'index.html')

def course(request):
    return render(request,'course.html')
def art(request):
    return render(request,'art.html')
def cs(request):
    return render(request,'cs.html')
def ss(request):
    return render(request,'ss.html')
def md(request):
    return render(request,'md.html')
def order1(request):
    return render(request,'order1.html')
