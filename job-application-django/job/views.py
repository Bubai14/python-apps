from django.contrib import messages
from django.shortcuts import render
from .forms import ApplicationForm
from .models import JobForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            start_date = form.cleaned_data['start_date']
            occupation = form.cleaned_data['occupation']

            # Save the records to the database
            JobForm.objects.create(first_name=first_name, last_name=last_name,
                                   email=email, start_date=start_date, occupation=occupation)
            messages.success(request, f"{first_name}, your application has been submitted successfully!!!")
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')
