from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
#from marketing.models import Signup


def index(request):

    posts_latest3 = Post.objects.order_by('-timestamp')[:3]

    context = {
        'destination' : 'about',
        'post_latest3' : posts_latest3,
    }
    return(render(request, 'index.html', context))

def bloghome(request):
    
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')

    posts = Post.objects.order_by('-timestamp')
    # categoriesList = Category.objects.order_by('title')

    # page_request_var = 'page'
    # paginator = Paginator(posts, 2)
    # page = request.GET.get(page_request_var)
    # try:
    #     paginated_queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     paginated_queryset = paginator.page(1)
    # except EmptyPage:
    #     paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'destination' : 'blog',
        'posts' : posts,
        #'categoriesList' : categoriesList, 
        # 'paginated_queryset' : paginated_queryset,
        # 'page_request_var' : page_request_var,
    }
    return(render(request, 'blog-home.html', context))


def blogpost(request, id, title):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')

    context = {
        'destination' : 'blog',
        'post' : post,
    }
    return(render(request, 'blog-post.html', context))


def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for reaching out - I will get back to you as soon as possible!')
    
    
    context = {
        'destination' : 'contact',
    }
    return(render(request, 'contact.html', context))


def portfolio(request):
    context = {
        'destination' : 'portfolio',
    }
    return(render(request, 'portfolio.html', context))

def resume(request):
    context = {
        'destination' : 'resume',
    }
    return(render(request, 'resume.html', context))


 
#Projects

def project(request):
    return(render(request, 'projects/project.html', ))

def project0(request):
    return(render(request, 'projects/cro-pdp-few-left-product-tags.html', ))

def project1(request):
    return(render(request, 'projects/cro-voucher-test.html', ))

def project2(request):
    return(render(request, 'projects/cro-pdp-sticky-cta.html', ))

def project3(request):
    return(render(request, 'projects/web-data-privacy-engineering.html', ))

def project4(request):
    return(render(request, 'projects/datascience-cac-cltc.html', ))

def project5(request):
    return(render(request, 'projects/datascience-nps-lifetime.html', ))

def project6(request):
    return(render(request, 'projects/datascience-nps-drivers.html', ))

def project7(request):
    return(render(request, 'projects/datascience-effect-of-product-descriptions.html', ))

def project8(request):
    return(render(request, 'projects/datascience-on-the-fence-users-popup.html', ))

def project13(request):
    return(render(request, 'projects/cro-checkout-urgency-message.html', ))

def project15(request):
    return(render(request, 'projects/cro-a2r-recommendation-popup.html', ))

def cookiepolicy(request):
    return(render(request, 'cookiepolicy.html', ))

# def services(request):
#     context = {
#     }
#     return(render(request, 'services.html', context))

# def index(request):
#     destination = 'Home'
    
#     posts_latest = Post.objects.order_by('-timestamp')[:1]
#     posts_orderby = Post.objects.order_by('-timestamp')
    
#     page_request_var = 'page'
#     paginator = Paginator(posts_orderby, 10)
#     page = request.GET.get(page_request_var)
#     try:
#         paginated_queryset = paginator.page(page)
#     except PageNotAnInteger:
#         paginated_queryset = paginator.page(1)
#     except EmptyPage:
#         paginated_queryset = paginator.page(paginator.num_pages)


#     if request.method == 'POST':
#         email = request.POST['email']
#         new_signup = Signup()
#         new_signup.email = email
#         new_signup.save()

#     context = {
#         'destination': destination,
#         'posts_latest': posts_latest,
#         'orderby_list': posts_orderby,
#         'paginated_queryset': paginated_queryset,
#         'page_request_var' : page_request_var,
#     }
#     return(render(request, 'index.html', context))

# def blogpost(request, id):
#     destination = 'Blogpost'
#     posts_latest = Post.objects.order_by('-timestamp')[:1]
#     post = get_object_or_404(Post, id=id)
#     context = {
#         'destination' : destination,
#         'posts_latest' : posts_latest,
#         'post' : post
#     }
#     return(render(request, 'blog-post.html', context))

# def about(request):
#     destination = 'About'
#     posts_latest = Post.objects.order_by('-timestamp')[:1]
#     print(posts_latest)
#     if request.method == 'POST':
#         email = request.POST['email']
#         new_signup = Signup()
#         new_signup.email = email
#         new_signup.save()

#     context = {
#         'destination' : destination,
#         'posts_latest' : posts_latest,
#     }
#     return(render(request, 'about.html', context))
