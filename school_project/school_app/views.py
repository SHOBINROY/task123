
from django.shortcuts import render
from . forms import OrderForm
from .models import Form
from django.views import View




class HomeView(View):
    def get(self, request):
        form = OrderForm()
        orders = Form.objects.all()
        return render(request, 'department.html', {'orders': orders, 'form': form})

    def post(self, request):
            form = OrderForm(request.POST, request.FILES)
            if form.is_valid():
                form.save();
                return render(request, 'department.html', {'form': form})



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
from django.shortcuts import render

# Create your views here.
