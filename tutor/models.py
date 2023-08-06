from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


# Create your models here.
class Review(models.Model):
    objects = models.Manager()
    firstname = models.CharField(max_length=50, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    stars = models.PositiveSmallIntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    
    def as_json(self):
        return dict(
            review_id=self.id, review_firstname=self.firstname,
            review_lastname=self.lastname, 
            review_stars=self.stars,
            review_description=self.description)


class CallBack(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    #number = PhoneNumberField(unique=True, null=False, blank=False)
    number = models.CharField(unique=True, max_length=11, null=False, blank=False)
    message = models.TextField()