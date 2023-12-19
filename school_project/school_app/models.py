from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

DEPARTMENT_CHOICES= (
    ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'),
    ('ART', 'ART'),
    ('SOCIAL SCIENCE', 'SOCIAL SCIENCE'),
    ('MEDICAL', 'MEDICAL'),
    ('COMMERCE', 'COMMERCE'),
)

COURSE_CHOICES = (
    ('AI', 'AI'),
    ('BA ART', 'BA ART'),
    ('MBBS', 'MBBS'),
    ('LLB', 'LLB'),
    ('B.COM', 'B.COM'),
)
PURPOSE_CHOICES = (
    ('Order Placed','Order Placed'),


)

class Form(models.Model):
    name = models.CharField(max_length=100)
    dob =models.DateField(auto_now=False, auto_now_add=False)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number =  models.IntegerField(max_length=10,validators=[ MaxValueValidator(9999999999)])
    mail_id = models.EmailField()
    address = models.CharField(max_length=255)
    department =models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    courses = models.CharField(choices=COURSE_CHOICES, max_length=50)
    purpose = models.CharField(choices=PURPOSE_CHOICES, max_length=50)
    materials= models.CharField(max_length=50)