from django.http import HttpResponse
from books.models import Book, Post
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
	latest_book_list = Book.objects.all().order_by('-end_date')[:5]
	return render_to_response('books/index.html', {'latest_book_list':latest_book_list,})

def bookDetail(request, book_id):
	b = Book.objects.get(id=book_id)
	posts = Post.objects.filter(book=book_id)
	return render_to_response('books/bookdetail.html', {'book':b, 'posts':posts})

def postDetail(request, book_id, post_id):
	post = Post.objects.get(id=post_id)
	book = Book.objects.get(id=book_id)
	return render_to_response('books/postdetail.html', {'book':book, 'post':post})
	


