# from django.db import models
#
# # Create your models here.
# from django.db import models
#
#
# c
#
# class purpose(models.Model):
#     PURPOSE_CHOICES = (
#         ('WISHLIST', "wishlist"),
#         ('ORDER', "place order"),
#
#     )
#     purpose =  models.CharField(max_length=9,
#                                 choices=PURPOSE_CHOICES, null=True)
#
# class details(models.Model):
#     name=models.CharField(max_length=100,blank=True,null=True)
#     address=models.CharField(max_length=100,blank=True,null=True)
#     age=models.IntegerField(blank=True,null=True)
#     phone=models.IntegerField(blank=True,null=True)
#     email= models.EmailField(max_length=100, blank=True, null=True)
#     dob=models.DateField(blank=True,null=True)
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
#     course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
#     purpose= models.ForeignKey(purpose, on_delete=models.CASCADE, null=True)
#     materials= models.ForeignKey(materials, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.name
# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
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


#
# class department(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
# class course(models.Model):
#     department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
# class materials(models.Model):
#     course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#      def __str__(self):
#              return self.name
#
#
