from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    bio = RichTextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args,**kwargs)

    def __str__(self):
        return self.user.first_name

    class Meta: 
        verbose_name_plural ='Perfiles'
    
class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural ='Etiquetas'

class Post(models.Model):
    title =  models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(null=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count=models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", default=None, blank=True)
    likes = models.ManyToManyField(User, related_name="post_like", default=None, blank=True)

    def number_of_likes(self):
        return self.likes.count()

    class Meta: 
        verbose_name_plural ='Publicaciones'

class Comments(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')

    def __str__(self) -> str:
        return f'Comentado por {self.name}'

    class Meta: 
        verbose_name_plural ='Comentarios'
        
        
class WebsiteMeta(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    about = RichTextField()

    def __str__(self) -> str:
        return self.title

    class Meta: 
        verbose_name_plural ='Metadata del sitio'
        


