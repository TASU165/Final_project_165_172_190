from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import login as authlogin, logout as authlogout
# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def login(request):
    return render(request, 'app_general/login.html')

def species(request):
    return render(request, 'app_general/species.html')

def article(request, year, slug):
    return HttpResponse('Article Year=' + str(year) + ' Slug=' +slug)

def species_dog(request):
    return render(request, 'app_general/species_dog.html')

def species_cat(request):
    return render(request, 'app_general/species_cat.html')

def guideline_dog(request):
    return render(request, 'app_general/guideline_dog.html')

def guideline_dog_Beagle(request):
    return render(request, 'app_general/guideline_dog_Beagle.html')

def guideline_dog_Chihuahua(request):
    return render(request, 'app_general/guideline_dog_Chihuahua.html')

def guideline_dog_Corgi(request):
    return render(request, 'app_general/guideline_dog_Corgi.html')

def guideline_dog_Golden_retriever(request):
    return render(request, 'app_general/guideline_dog_Golden_retriever.html')

def guideline_dog_German_shepherd(request):
    return render(request, 'app_general/guideline_dog_German_shepherd.html')

def guideline_dog_Siberian_Husky(request):
    return render(request, 'app_general/guideline_dog_Siberian_Husky.html')

def guideline_dog_Shih_tzu(request):
    return render(request, 'app_general/guideline_dog_Shih_tzu.html')

def guideline_dog_Dalmatian(request):
    return render(request, 'app_general/guideline_dog_Dalmatian.html')

def guideline_dog_Samoyed(request):
    return render(request, 'app_general/guideline_dog_Samoyed.html')

def species_bird(request):
    return render(request, 'app_general/species_bird.html')

def species_other(request):
    return render(request, 'app_general/species_other.html')

def species_small(request):
    return render(request, 'app_general/species_small.html')

def guideline_cat(request):
    return render(request, 'app_general/guideline_cat.html')

def guideline_cat_a(request):
    return render(request, 'app_general/guideline_cat_a.html')

def guideline_cat_b(request):
    return render(request, 'app_general/guideline_cat_b.html')

def guideline_cat_c(request):
    return render(request, 'app_general/guideline_cat_c.html')

def guideline_cat_d(request):
    return render(request, 'app_general/guideline_cat_d.html')

def guideline_cat_e(request):
    return render(request, 'app_general/guideline_cat_e.html')

def guideline_cat_f(request):
    return render(request, 'app_general/guideline_cat_f.html')

def guideline_cat_g(request):
    return render(request, 'app_general/guideline_cat_g.html')

def guideline_cat_h(request):
    return render(request, 'app_general/guideline_cat_h.html')

def guideline_cat_i(request):
    return render(request, 'app_general/guideline_cat_i.html')

def guideline_bird(request):
    return render(request, 'app_general/guideline_bird.html')

def guideline_bird_a(request):
    return render(request, 'app_general/guideline_bird_a.html')

def guideline_bird_b(request):
    return render(request, 'app_general/guideline_bird_b.html')

def guideline_bird_c(request):
    return render(request, 'app_general/guideline_bird_c.html')

def guideline_bird_d(request):
    return render(request, 'app_general/guideline_bird_d.html')

def guideline_bird_e(request):
    return render(request, 'app_general/guideline_bird_e.html')

def guideline_bird_f(request):
    return render(request, 'app_general/guideline_bird_f.html')

def guideline_bird_g(request):
    return render(request, 'app_general/guideline_bird_g.html')

def guideline_bird_h(request):
    return render(request, 'app_general/guideline_bird_h.html')

def guideline_bird_i(request):
    return render(request, 'app_general/guideline_bird_i.html')

def guideline_bird(request):
    return render(request, 'app_general/guideline_bird.html')

def guideline_bird_a(request):
    return render(request, 'app_general/guideline_bird_a.html')

def guideline_bird_b(request):
    return render(request, 'app_general/guideline_bird_b.html')

def guideline_bird_c(request):
    return render(request, 'app_general/guideline_bird_c.html')

def guideline_bird_d(request):
    return render(request, 'app_general/guideline_bird_d.html')

def guideline_bird_e(request):
    return render(request, 'app_general/guideline_bird_e.html')

def guideline_bird_f(request):
    return render(request, 'app_general/guideline_bird_f.html')

def guideline_bird_g(request):
    return render(request, 'app_general/guideline_bird_g.html')

def guideline_bird_h(request):
    return render(request, 'app_general/guideline_bird_h.html')

def guideline_bird_i(request):
    return render(request, 'app_general/guideline_bird_i.html')

def guideline_small(request):
    return render(request, 'app_general/guideline_small.html')

def guideline_small_a(request):
    return render(request, 'app_general/guideline_small_a.html')

def guideline_small_b(request):
    return render(request, 'app_general/guideline_small_b.html')

def guideline_small_c(request):
    return render(request, 'app_general/guideline_small_c.html')

def guideline_small_d(request):
    return render(request, 'app_general/guideline_small_d.html')

def guideline_small_e(request):
    return render(request, 'app_general/guideline_small_e.html')

def guideline_small_f(request):
    return render(request, 'app_general/guideline_small_f.html')

def guideline_small_g(request):
    return render(request, 'app_general/guideline_small_g.html')

def guideline_small_h(request):
    return render(request, 'app_general/guideline_small_h.html')

def guideline_small_i(request):
    return render(request, 'app_general/guideline_small_i.html')

def guideline_other(request):
    return render(request, 'app_general/guideline_other.html')

def guideline_other_a(request):
    return render(request, 'app_general/guideline_other_a.html')

def guideline_other_b(request):
    return render(request, 'app_general/guideline_other_b.html')

def guideline_other_c(request):
    return render(request, 'app_general/guideline_other_c.html')

def guideline_other_d(request):
    return render(request, 'app_general/guideline_other_d.html')

def guideline_other_e(request):
    return render(request, 'app_general/guideline_other_e.html')

def guideline_other_f(request):
    return render(request, 'app_general/guideline_other_f.html')

def guideline_other_g(request):
    return render(request, 'app_general/guideline_other_g.html')

def guideline_other_h(request):
    return render(request, 'app_general/guideline_other_h.html')

def guideline_other_i(request):
    return render(request, 'app_general/guideline_other_i.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            authlogin(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'app_general/login.html',{
        'form':form,
    })

def logout_view(request):
    if request.method == 'POST':
        authlogout(request) 
        return redirect('home')
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authlogin(request, user)
            return redirect('products')
    else:
        form = UserCreationForm()
    return render(request, 'app_general/signup.html', {'form':form})