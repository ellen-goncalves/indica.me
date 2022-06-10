from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Idea (models.Model):
    class Category(models.TextChoices):
        Jogos = "Jogos"
        Educativos = "Educativo"
        Entretenimento = "Entretenimento"
        Saude = "Saúde e bem-estar"
        Aleatorio = "Aleatorio"


    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    image = models.URLField()
    url = models.URLField()
    created_on = models.DateTimeField(auto_now = True, verbose_name='Data de criação')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=Category.choices, default="Outros")

    class Meta:
        db_table = "idea"

    def __str__(self):
        return self.title
