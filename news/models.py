from django.db import models
from config.models import BaseModel
from ckeditor.fields import RichTextField

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()


    def __str__(self) -> str:
        return self.name
    
class News(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=255, null=True)
    body = RichTextField()
    image = models.ImageField(upload_to='image/')
    banner = models.ImageField(upload_to='banner/')
    view = models.BigIntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class Contact(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name
