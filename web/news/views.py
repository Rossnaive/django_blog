from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


# Create your views here.
def index (request) :
    all_news = News.objects.order_by('-id')[:99]
    all_cate = Category.objects.all()
    # page paginator
    paginator = Paginator(all_news, 5)
    pageNumber = request.GET.get('page')
    try:
        all_news = paginator.page(pageNumber)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
         all_news = paginator.page(paginator.num_pages)

    # end page paginator
    content ={'news':  all_news, 'cate': all_cate }
    return render (request, "home.html", content )
def cate (request,cate) :
	news_cate = News.objects.filter(category=cate)
	cate_item = Category.objects.get(id=cate)
	all_cate = Category.objects.all()
	content = {'cate':all_cate,'news':news_cate,'cate_item':cate_item}
	return render(request,"cate.html",content);
def detail(request,detail):
    news_detail = News.objects.get(id =detail)
    all_cate = Category.objects.all()
    content ={'cate':all_cate,'detail': news_detail}
    return render (request, "detail.html",content)
def contact ( request):
    return render (request, "contact.html")
def about ( request):
    return render (request, "about.html")
# email
def email(request):
    form_class = ContactForm

    return render(request, 'email.html', {
        'form': form_class,
    })
