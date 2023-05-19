from django.urls import path

from order import views

app_name ='order'

urlpatterns=[
    # path('shop',views.shop,name='shop')
    path('',views.order_create_view,name='order_create'),
    path('ajax/load_course/',views.load_courses,name='ajax_load_courses')
    # path('update/<int:id>/',views.update,name='update')
    ]