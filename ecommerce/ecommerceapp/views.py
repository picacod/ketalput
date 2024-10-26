from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from ecommerceapp.models import Dress, User, Wishlist

def index(request):
    trending_dresses = Dress.objects.order_by('-created_at')[:4]
    count = Wishlist.objects.count() 
    return render(request, 'index.html',{'trending_dresses':trending_dresses,'wishlist_count': count})




def rough(request):
    return render(request, 'rough.html')

def admindash(request):
    return render(request, 'admin/base.html')

def add_dress(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        gender = request.POST['gender']
        category = request.POST['category']
        price = request.POST['price']
        discount = request.POST['discount']
        color = request.POST['color']
        sizes = request.POST.getlist('size')  
        sizes_str = ','.join(sizes)  
        image = request.FILES.get('image')
        add_img1 = request.FILES.get('addimg1')
        add_img2 = request.FILES.get('addimg2')
        add_img3 = request.FILES.get('addimg3')
        stock_quantity = request.POST['stock_quantity']
        dress = Dress(
            name=name,
            desc=desc,
            gender=gender,
            category=category,
            price=price,
            discount=discount,
            color=color,
            size=sizes_str, 
            image=image,
            add_img1=add_img1,
            add_img2=add_img2,
            add_img3=add_img3,
            stock_quantity=stock_quantity
        )
        print('Dress object before saving:', dress)
        dress.save()
        print('Dress saved successfully!')
    return render(request,'admin/addDress.html')


def admin_index(request):
    return render(request,'admin/index.html')

def view_dress(request):
    dresses=Dress.objects.all().order_by('-id')
    return render(request,'admin/viewDress.html',{'dresses':dresses})

def delete_dress(request,dress_id):
    dress=Dress.objects.get(id=dress_id)
    dress.delete()
    return redirect('view_dress')

def collections(request,gender):
    dresses = Dress.objects.filter(gender=gender).order_by('-id')
    categories = Dress.objects.values_list('category', flat=True).distinct()
    wishlist_dress_ids = Wishlist.objects.values_list('dress_id', flat=True)
    count = Wishlist.objects.count() 
   
    return render(request,'collections.html',{'dresses':dresses,'gender':gender,'categories':categories,'wishlist_dress_ids':wishlist_dress_ids,'wishlist_count': count})



def filter_list(request,gender):
    filter_list = Dress.objects.filter(gender=gender).order_by('-id')
    selected_categories = request.GET.getlist('category')
    selected_colors = request.GET.getlist('color')
    selected_sizes = request.GET.getlist('size')
    count = Wishlist.objects.count() 
    if selected_categories:
        filter_list = filter_list.filter(category__in=selected_categories)
    
    if selected_colors:
        filter_list = filter_list.filter(color__in=selected_colors)
    
    if selected_sizes:
        filter_list = filter_list.filter(size__in=selected_sizes)
    
    categories = Dress.objects.values_list('category', flat=True).distinct()
    filter_count = len(selected_categories) + len(selected_colors) + len(selected_sizes)
    return render(request, 'collections.html', {
        'filter_list': filter_list, 
        'categories': categories, 
        'selected_categories': selected_categories,
        'selected_colors': selected_colors,
        'selected_sizes': selected_sizes,
        'filter_count':filter_count,
        'wishlist_count': count
    })


def add_to_wishlist(request, dress_id):
    if request.method == "POST":
        dress = Dress.objects.get(id=dress_id)
        wishlist, created = Wishlist.objects.get_or_create(dress=dress)

    if created:
        return redirect('collections', gender=dress.gender)  
    else:
        wishlist.delete()
        gender = dress.gender
    return redirect('collections',gender=gender)


def wishlist(request):
    dresses=Wishlist.objects.all()
    return render(request,'wishlist.html',{'dresses':dresses})


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')
        country = request.POST.get('country')
        title = request.POST.get('title')
        dob = request.POST.get('dob')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            country=country,
            dob=dob,
            title=title
        )
        user.set_password(password) 
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')

    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Email: {email}, Password: {password}")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('index')  
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Email: {email}, Password: {password}")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('index')  
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')



def detail(request,dress_id):
    dress=Dress.objects.get(id=dress_id)
    count = Wishlist.objects.count() 
    return render(request,'product.html',{'dress':dress,'wishlist_count':count})