from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post,Category,Comment
from next_prev import next_in_order,prev_in_order
from django.db.models import Q
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

# from 
# Create your views here.

def error_404(request,exception):
    return render(request, '404.html', status=404)

def error_505(request,exception):
    return render(request, '505.html', status=404)

def home(request):
    all_post = Post.objects.all().order_by('created')
    
    # all_category = Category.objects.all()
    slide_carousel = all_post.order_by('-created')[:3]
    page = request.GET.get('page',1)
    paginator = Paginator(all_post, 5)
    
    try:
        posts = paginator.page(page)
        
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context ={'posts':posts, 'slide_carousel':slide_carousel}
    return render(request, 'blog/home.html', context)

def blog(request):
    return render(request, 'blog/blog.html', context)

def post_details(request,pk):
    post = Post.objects.filter().get(id=pk)
    comment= post.comment_set.all()
    
    next_post = next_in_order(post, loop=True)
    prev = prev_in_order(post,loop=True)
    if request.method == "POST":
        message = Comment.objects.create(
            user = request.user,
            post=post,
            message=request.POST.get('cMessage')
        )
        return redirect('post_detail', pk=post.id)
    context={
        'post':post,
        'next':next_post,
        'prev':prev,
        'comment':comment
             }
    return render(request, 'blog/post_detail.html', context)



def category(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
                                Q(category__name=q) 
                                |
                                Q(title__icontains=q) 
                                |
                                Q(description=q)
                                ).distinct()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page', 1)

    try:
        search_pagination = paginator.page(page)

    except PageNotAnInteger:
        search_pagination = paginator.page(1)

    except EmptyPage:
        search_pagination = paginator.page(paginator.num_pages)

    # posts = Post.objects.all()                            
    category = Category.objects.all()
    context =  {
        'category':category,
        'posts': search_pagination,
        'q':q
    }
    return render(request, 'blog/category.html', context)


# def about(request):
#     return render(request, 'blog/about.html')


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cName = form.cleaned_data['cName']
            cEmail = form.cleaned_data['cEmail']
            cMessage = form.cleaned_data['cMessage']
            cSubject = form.cleaned_data['cSubject']
            try:
                send_mail(cSubject,cMessage,'umohu67@gmail.com', [cEmail])
                messages.success(request, 'Your message was sent successfully.')
            except:
                return messages.error(request,'Your message has not been sent please check your network. ')
            return redirect('contact')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    context={'form':form}
    return render(request, 'blog/contact.html',context)

