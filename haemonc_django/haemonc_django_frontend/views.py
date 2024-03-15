# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import VariantEn  # import the model that maps to the variant table
from django.contrib import messages
from .forms import VariantEnForm
from django.views.generic import CreateView
from django.forms import ModelForm


class VariantEnForm(ModelForm):
    class Meta:
        model = VariantEn
        fields = ['hgvs', 'gene', 'disease', 'frequency']

def index(request):
    # get all the records from the variant table
    variants = VariantEn.objects.all()#Variant.objects.all()
    # render the index.html template with the variants as context
    return render(request, 'haemonc_django_frontend/index.html', {'variants': variants})

def create_variant(request):
    if request.method == 'POST':
        form = VariantEnForm(request.POST)
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Variant created successfully.') 
            return redirect('haemonc_django_frontend/index.html') 
    else: 
        form = VariantEnForm()
    return render(request, 'haemonc_django_frontend/create_variant.html', {'form': form}) 

# Define a view function for the variant input page
def variant_input(request):
    # If the request is a POST, process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with the data from the request
        form = VariantEnForm(request.POST, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the variant display page
            return redirect('variant_display')
    # If the request is a GET, create a blank form
    else:
        form = VariantEnForm()
    # Render the form template with the form as a context variable
    return render(request, 'variant_input.html', {'form': form})

class VariantEnCreateView(CreateView):
    model = VariantEn
    form_class = VariantEnForm
    #template_name = 'varianten_form.html'
    success_url = '/success/' 
   

