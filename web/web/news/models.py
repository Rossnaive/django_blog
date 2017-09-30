from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

# Create your models here.
class Category  (models.Model):
    name = models.CharField(max_length =200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
class News (models.Model) :
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    intro  = RichTextField()
    content = RichTextField()
    thumbnail = models.FileField( null= True, blank = True)
    created = models.DateTimeField()


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __unicode__ (self) :
        return self.title

    def __str__ (self):
        return self.title
