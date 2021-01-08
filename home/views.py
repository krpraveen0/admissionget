from django.shortcuts import render
from home.models import EnggCollege, MedicalCollege, MmgCollege, LawCollege, Courses, Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home/site/index.html')

def about(request):
    return render(request, 'home/site/about.html')

def enggCourse(request):
    course = Courses.objects.all()
    context = {'course':course}
    return render(request, 'home/site/enggCourse.html',context)

def mmgCourse(request):
    return render(request, 'home/site/mmgCourse.html')

def medicalCourse(request):
    return render(request, 'home/site/medicalCourse.html')

def lawCourse(request):
    return render(request, 'home/site/lawCourse.html')

def enggCollege(request):
    enggColleges = EnggCollege.objects.all()
    context = {'enggColleges': enggColleges}
    return render(request, 'home/site/enggCollege.html', context)

def mmgCollege(request):
    mmgColleges = MmgCollege.objects.all()
    context = { 'mmgColleges':mmgColleges}
    return render(request, 'home/site/mmgCollege.html', context)

def medicalCollege(request):
    medicalColleges = MedicalCollege.objects.all()
    context = { 'medicalColleges':medicalColleges}
    return render(request, 'home/site/medicalCollege.html', context)

def lawCollege(request):
    lawColleges = LawCollege.objects.all()
    context = {'lawColleges':lawColleges}
    return render(request, 'home/site/lawCollege.html', context)

def EnggCollegeDetail(request, slug):
    college = EnggCollege.objects.filter(slug=slug).first()
    context = { 'college' : college}
    return render(request, 'home/site/EnggCollegeDetail.html', context)

def MedicalCollegeDetail(request, slug):
    college = MedicalCollege.objects.filter(slug=slug).first()
    context = { 'college' : college}
    return render(request, 'home/site/MedicalCollegeDetail.html', context)

def MmgCollegeDetail(request, slug):
    college = EnggCollege.objects.filter(slug=slug).first()
    context = { 'college' : college}
    return render(request, 'home/site/MmgCollegeDetail.html', context)

def LawCollegeDetail(request, slug):
    college = EnggCollege.objects.filter(slug=slug).first()
    context = { 'college' : college}
    return render(request, 'home/site/LawCollegeDetail.html', context)
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        lname = request.POST['last-name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if len(name)<2 or len(email)<3 or len(mobile)<10 or len(content)<3:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name,lname=lname, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, "your form is submitted successfully")
        
    return render(request, 'home/site/contact.html')
