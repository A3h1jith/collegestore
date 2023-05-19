from django.contrib import messages
from django.shortcuts import render

from order.models import Order


# Create your views here.
# def shop(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         DOB = request.POST.get('DOB')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone_number = request.POST.get('phone_number')
#         mail_id = request.POST.get('mail_id')
#         address = request.POST.get('address')
#         department = request.POST.get('department')
#         purpose = request.POST.get('purpose')
#         materials_provide = request.POST.get('materials_provide')
#         order = Order(name=name,DOB=DOB,age=age,gender=gender,phone_number=phone_number,mail_id=mail_id,address=address,department=department,purpose=purpose,materials_provide=materials_provide)
#         order.save()
#     return render(request,'shop.html')


from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderCreationForm
from .models import Order
from a3h1collegestore.models import Course


def order_create_view(request):
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "order created successfully")
            return redirect('order:order_create')
    return render(request, 'shop.html', {'form': form})


# # AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

# def update(request,id):
#     orders=Order.objects.get(id=id)
#     form=OrderCreationForm(request.POST or None,request.FILES,instance=Order)
#     if form.is_valid():
#          form.save()
#          return redirect('/')
#     return render(request,'test.html',{'orders':orders,'form':form})