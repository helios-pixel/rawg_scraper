from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    rawg_id=models.IntegerField()

    def __str__(self):
        return self.title

class UserLibrary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.game.title}'

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    game= models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.game.title} ({self.rating})'


    