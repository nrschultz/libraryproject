from django.db import models

class Book(models.Model):
	author = models.CharField(max_length=100)
	num_pages = models.IntegerField()
	start_date = models.DateTimeField('date started')
	end_date = models.DateTimeField('date finished')
	title = models.CharField(max_length=256)
	
	def __unicode__(self):
		return self.title + " by "+ self.author

class Post(models.Model):
	post_text = models.TextField()
	book = models.ForeignKey(Book)
	title = models.CharField(max_length=256)

	def __unicode__(self):
		return self.title




# Create your models here.
