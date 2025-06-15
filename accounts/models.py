from django.db import models
from. validators import validate_age
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[validate_age])
    image = CloudinaryField('image', blank=True, null=True)