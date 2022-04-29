from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Idea (models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    image = models.URLField()
    url = models.URLField()
    created_on = models.DateTimeField(auto_now = True, verbose_name='Data de criação')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "idea"

    def __str__(self):
        return self.title
