from django.contrib import auth, messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

from .models import Movie, Category, Comment
from .forms import MovieForm, CommentForm



def ShowAllProducts(request):
    category = request.GET.get('category')

    if category == None:
        products = Movie.objects.filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Movie.objects.filter(category__title=category)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'showProducts.html', context)


def productDetail(request, pk):
    eachProduct = Movie.objects.get(id=pk)

    num_comments = Comment.objects.filter(product=eachProduct).count()

    context = {
        'eachProduct': eachProduct,
        'num_comments': num_comments,
    }

    return render(request, 'productDetail.html', context)



def addProduct(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form =MovieForm()

    context = {
        "form": form
    }

    return render(request, 'addProducts.html', context)



def updateProduct(request, pk):
    product = Movie.objects.get(id=pk)

    form = MovieForm(instance=product)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form": form
    }

    return render(request, 'updateProduct.html', context)



def deleteProduct(request, pk):
    product = Movie.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')



def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Movie.objects.filter(category__title__icontains=query)
            return render(request, 'searchbar.html', {'products': products})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})


def add_comment(request, pk):
    eachProduct = Movie.objects.get(id=pk)

    form = CommentForm(instance=eachProduct)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('showProducts')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    return redirect(reverse('product', args=[product_id]))


def admin_Show(request):
    category = request.GET.get('category')

    if category == None:
        products = Movie.objects.filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products, 2)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        products = Movie.objects.filter(category__title=category)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'adminshow.html', context)


def admin_product(request, pk):
    eachProduct = Movie.objects.get(id=pk)

    num_comments = Comment.objects.filter(product=eachProduct).count()

    context = {
        'eachProduct': eachProduct,
        'num_comments': num_comments,
    }

    return render(request, 'adminproduct.html', context)

