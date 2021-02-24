from django.http import HttpResponse
from django.shortcuts import render

data = [
    {"name": "Yuvraj", "age": 24, "Mobile_No": 9888659456, "Gender": "M"},
    {"name": "Nipun", "age": 18, "Mobile_No": 9884637456, "Gender": "M"},
    {"name": "Kunal", "age": 21, "Mobile_No": 7564659456, "Gender": "M"},
    {"name": "Subhrato", "age": 27, "Mobile_No": 9888686382, "Gender": "M"},
    {"name": "Sonu", "age": 22, "Mobile_No": 7591342456, "Gender": "F"},
    {"name": "Rahul", "age": 25, "Mobile_No": 9874382456, "Gender": "M"},
    {"name": "Vmm", "age": 30, "Mobile_No": 4834694642, "Gender": "M"},
    {"name": "Yuvi", "age": 22, "Mobile_No": 7491259456, "Gender": "M"},
    {"name": "Yash", "age": 23, "Mobile_No": 9842749456, "Gender": "F"},
    {"name": "Mini", "age": 28, "Mobile_No": 9846682456, "Gender": "F"}
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
    name = request.GET['text1']
    age = request.GET['text2']
    mobile = request.GET['text3']
    gender = request.GET['text4']
    # print(gender)
    # for x in data:
    data.append({"name": name, "age": age, "Mobile_No": mobile, "Gender": gender})

    return render(request, "test.html", {"data": data})
