from django.db import models
from. validators import validate_age
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[validate_age])
    image = models.ImageField()