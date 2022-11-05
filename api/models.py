from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=True) #an images folder is created in this step
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)     #more than one user can aswer the questions

    def __str__(self):
        return self.title


class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE) #each question have more than one answers
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE) #more than one user can aswer the questions(one to many)
    upvote=models.ManyToManyField(User,related_name="upvote")  #many user can upvote the answer 
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.answer







