from django.shortcuts import render

from a3h1collegestore.models import Message
from order.models import Order


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        messages=Message(name=name,email=email,subject=subject,message=message)
        messages.save()
        from django.contrib import messages
        messages.success(request, 'Message sent successfully')
    return render(request,'contact.html')
# def shop(request):
#     return render(request, 'shop.html')
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
#         course = request.POST.get('course')
#         purpose = request.POST.get('purpose')
#         materials_provide = request.POST.get('materials_provide')
#         order = Order(name=name,DOB=DOB,age=age,gender=gender,phone_number=phone_number,mail_id=mail_id,address=address,department=department,course=course,purpose=purpose,materials_provide=materials_provide)
#         order.save()
#     return render(request,'shop.html')