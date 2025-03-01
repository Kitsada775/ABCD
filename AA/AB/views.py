cmd
D:
git config –global user.name
git config –global user.email
gh auth login
clone ที่สร้างมา cdเข้า แล้ว code .
Tmn
python -m venv venv
.\venv\Scripts\activate
รอบแรกpip install djando /รอบ2 pip install djando pyyaml
django-admin startproject AA รอบ2ไม่ต้อง
เอาขึ้น git ก่อน
git add .
git commit -m “AAA”
git push origin main
สร้างและแก้ไข branch ตามชื่อฟังก์ชัน ใน git ก่อน ค่อย โคลน
ลง venv ใหม่
python manage.py startapp AB
ไปที่ srttings.py เอาชื่อ app ไปลง
ไปที่ urls.py เพิ่ม include
ส่วน path(“”,include(“AB.urls”))
สร้างไฟล์urls.py ในFolder ฟังก์ชั่นของเรา


from django.db import models
class a(models.Model):
    id = models.CharField(max_length=128 , primary_key=True) #เพื่อบอกว่าเป็นPrimary key
    name = models.CharField(max_length=128 )
    Teacher = models.CharField(max_length=128)

#python manage.py makemigrations
#python manage.py migrate

#สร้างFolder templates 
#สร้าง fixtures แล้วสร้างไฟล์ Doyaml
สร้างfixtures ไว้ในApp/ Do.yaml
model : AB.a
pk : 1
fields : 
    id : 1
    N : ชื่อ
    T : ชื่ออาจาร์ย
model : AB.a
pk : 2 
fields : 
    id : 2
    N : ชื่อ
    T : ชื่ออาจาร์ย
#	ชื่อField : ค่าที่ต้องการใส่ #ไม่ต้องใส่เครื่องหมายqoute
#พิมพ์คำสั่งใน cmd python mange.py loaddata Do.yaml

from django.shortcuts import render
from .models import*
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


def bb(req):
    n = a.objects.all()
    return render(req,"home.html",{"A1":n})


def cc(req):
    m = req.GET.get("id","")
    n1 = a.objects.filter(id=m)
    return render(req,"home1.html",{"A2":n1})


def dd(req):
    o = req.GET.get("N","")
    n2 = a.objects.filter(N=o)
    return render(req,"home2.html",{"A3":n2})


class ss (UpdateView):
    model = a
    fields = ["N","t"]
    template_name = "home3.html"
    success_url = reverse_lazy("bb")


class yy (DeleteView):
    model = a
    template_name = "home4.html"
    success_url = reverse_lazy("bb")


from django.urls import path, include
from .views import*

urlpatterns = [
    path("",bb,name="bb"),
    path("1",cc,name="cc"),
    path("2",dd,name="dd"),
    path("3/<str:pk>",ss.as_view(),name="ss"),
    path("4/<str:pk>",yy.as_view(),name="yy"),


]

<h1>show</h1>
{%for i in A1%}
<h1>{{i.id}}{{i.N}}{{i.t}}</h1>
{%endfor%}


<h1>show</h1>
<form method="get">
    <input type="text" name="id">
    <button type="submit">กด</button>
</form>
{%for i in A2%}
<h1>{{i.id}}{{i.N}}{{i.t}}</h1>
{%endfor%}

<h1>show</h1>
<form method="get">
    <input type="text" name="N">
    <button type="submit">กด</button>
</form>
{%for i in A3%}
<h1>{{i.id}}{{i.N}}{{i.t}}</h1>
{%endfor%}

<form method="post">
   {%csrf_token%}
   {{form.as_p}}
    <button type="submit">ตกลง</button>
</form>

<h1> ลบวิชา {{a.N}}</h1>
<form method="post">
    {%csrf_token%}
   
     <button type="submit">ตกลง</button>
 </form>

สร้าง file .dockerignore ใน project แล้วใส่ venv
สร้าง  Dockerfile
FROM python:3.11-slim


WORKDIR /AA


COPY . .


RUN pip install django


RUN python manage.py migrate


EXPOSE 9999


CMD ["python","manage.py","runserver","0.0.0.0:9999"]

ก่อนจะรันคำสั่งต้องเปิดdockerdesktopก่อน

เขียนคำสั่ง เพื่อ build
docker build -t do:1.0 .
docker run –name do -p 9999:9999 do:1.0
