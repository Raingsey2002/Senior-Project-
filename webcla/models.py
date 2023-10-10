
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
# Create your models here.


gender_choices = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
)

class Member(AbstractUser):
    gender = models.CharField(max_length=10,choices=gender_choices,null=True,blank=True)
    dateofbirth = models.DateField(null=True)
    image = models.ImageField(upload_to='Image',null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Website(models.Model):
    url = models.URLField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=False ,default=True)

    extracted_text = models.TextField(max_length=None)

    def __str__(self):
        return self.url


    def get_rating(self):
        average_rating = Rating.objects.filter(url=self).aggregate(Avg('rating')).get('rating__avg')
        if average_rating is not None:
            rounded_rating = round(average_rating, 1)
            return rounded_rating
        else:
            return None



class Rating(models.Model):
    created_by = models.ForeignKey(Member,related_name='Ratings', on_delete=models.CASCADE)
    url = models.ForeignKey(Website, related_name='Ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

class CommentandRating(models.Model):
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
