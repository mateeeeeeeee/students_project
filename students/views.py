import random
from django.shortcuts import render

def random_moswavle():
    saxelebi = ["giorgi", "anastasia", "tamari", "nika", "mariami", "daviti", "luka", "sopo", "ana", "kaxa"]
    gvarebi = ["baramidze", "beglarishvili", "janelidze", "maisuradze", "kekelia", "lomtadze", "mchedlidze"]

    moswavleebi = []
    for _ in range(100):
        moswavle = {
            "saxeli": random.choice(saxelebi),
            "gvari": random.choice(gvarebi),
            "gpa": round(random.uniform(1.0, 4.0), 2),
            "kursi": random.randint(1, 4)
        }
        moswavleebi.append(moswavle)
    return moswavleebi

def main_page_view(request):
    students = random_moswavle()
    student = random.choice(students)
    return render(request, 'main_page.html', {'student': student})

def students_page_view(request):
    students = random_moswavle()
    return render(request, 'students_page.html', {'students': students})

