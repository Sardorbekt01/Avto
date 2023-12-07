from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Avto(models.Model):
    model = models.CharField( max_length=30, blank=False)
    color = models.CharField(max_length=30,blank=False)
    price = models.IntegerField(blank=False,default=15000)
    about = models.TextField(blank=True)
    year = models.IntegerField(blank=False)
    image = models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return self.model
    

    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="70" height="70" />' % (self.image))

    image_tag.short_description = 'Image'
    

