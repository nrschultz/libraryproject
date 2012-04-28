from libraryproject.books.models import Book, Post
from django.contrib import admin

class PostInline(admin.StackedInline):
	fields = ['title','post_text']
	model = Post
	extra = 1

class BookAdmin(admin.ModelAdmin):
	fieldsets = [('Book Information', {'fields' : ['title','author','num_pages']}),
				('Reading Time', {'fields':['start_date','end_date']}),
				]
	inlines=[PostInline]



admin.site.register(Book, BookAdmin)
#admin.site.register(Post)
