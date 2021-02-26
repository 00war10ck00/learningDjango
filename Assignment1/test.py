from django.http import HttpResponse
from django.shortcuts import render

count = 10
data = [
    {"S_No": 1, "name": "Yuvraj", "age": 24, "Mobile_No": 9888659456, "Gender": "M"},
    {"S_No": 2, "name": "Nipun", "age": 18, "Mobile_No": 9884637456, "Gender": "M"},
    {"S_No": 3, "name": "Kunal", "age": 21, "Mobile_No": 7564659456, "Gender": "M"},
    {"S_No": 4, "name": "Subhrato", "age": 27, "Mobile_No": 9888686382, "Gender": "M"},
    {"S_No": 5, "name": "Sonu", "age": 22, "Mobile_No": 7591342456, "Gender": "F"},
    {"S_No": 6, "name": "Rahul", "age": 25, "Mobile_No": 9874382456, "Gender": "M"},
    {"S_No": 7, "name": "Vmm", "age": 30, "Mobile_No": 4834694642, "Gender": "M"},
    {"S_No": 8, "name": "Yuvi", "age": 22, "Mobile_No": 7491259456, "Gender": "M"},
    {"S_No": 9, "name": "Yash", "age": 23, "Mobile_No": 9842749456, "Gender": "F"},
    {"S_No": 10, "name": "Mini", "age": 28, "Mobile_No": 9846682456, "Gender": "F"}
]


def index(request):
    # print(data)
    # return HttpResponse(data)
    return render(request, "test.html", {"data": data})


def test2(request):
    txt = request.GET['text1']
    # print(data)
    new_data = []
    for i in data:
        # if i['name'].upper() == txt.upper():
        if txt.upper() in i['name'].upper():
            new_data.append(i)
    # return HttpResponse(txt)
    return render(request, "test.html", {"data": new_data})


def append(request):
    global count
    count += 1
    name = request.GET['text1']
    age = request.GET['text2']
    mobile = request.GET['text3']
    gender = request.GET['text4']
    # print(gender)
    # for x in data:
    data.append({"S_No": count, "name": name, "age": age, "Mobile_No": mobile, "Gender": gender})

    return render(request, "test.html", {"data": data})


def delete(request):
    i = -1
    name = request.GET['bt2']
    for x in data:
        i += 1
        if x['name'] == name:
            break
    data.pop(i)

    return render(request, "test.html", {"data": data})
    # return HttpResponse(str(s_no))


def edit(request):
    list1=[]
    s_no = request.GET['bt3']
    val = int(s_no)
    # return HttpResponse(s_no)
    for x in data:
        if x['S_No'] == val:
            list1.append(x)
    return render(request,"edit_page.html",{"list1":list1})


def update(request):
    s_no = request.GET['sp1']
    val = int(s_no)
    name = request.GET['text1']
    age = request.GET['text2']
    mobile_no = request.GET['text3']
    gender = request.GET['text4']
    print(name)
    print(age)
    print(mobile_no)
    print(gender)
    for x in data:
        if x['S_No'] == val:
            x['name']=name
            x['age']=age
            x['Mobile_No']=mobile_no
            x['Gender']=gender

    return render(request,"test.html",{"data":data})