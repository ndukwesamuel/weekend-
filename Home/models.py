from django.db import models

# Create your models here.


class Post(models.Model):
    First_name = models.CharField(max_length=50, )
    Last_name  = models.CharField(max_length=50)
    Age = models.IntegerField()
    bvn = models.IntegerField(default=20)

    def __str__(self):
        return self.First_name  

    pass


class Profile(models.Model):
    profile = models.OneToOneField(Post, on_delete=models.CASCADE)
    Address = models.CharField(max_length=300)
    Phone_number = models.IntegerField()
    Email = models.EmailField(max_length=254)


    def __str__(self):
        return self.profile.First_name
    




class PRoduct(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    des = models.TextField()

    def __str__(self):
        return self.name
