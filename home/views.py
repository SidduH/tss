from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello tss. ")

def about(request):
    return HttpResponse("Hello about us. ")

def managementTeam(request):
    return HttpResponse("Hello management team")

def services(request):
    return HttpResponse("Hello security services")

def training(request):
    return HttpResponse("Hello training")

def clients(request):
    return HttpResponse("Hello clients")

def photoGallery(request):
    return HttpResponse("Hello photo gallery")

def enquiry(request):
    return HttpResponse("Hello enquiry")

def careers(request):
    return HttpResponse("Hello careers")

def contactUs(request):
    return HttpResponse("Hello contact us")


