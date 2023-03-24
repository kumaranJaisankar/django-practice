from django.db import models

# Create your models here.
# class User(models.Model):
#     uid = models.CharField(max_length=20)
#     uname = models.CharField(max_length=100)
#     uemail = models.EmailField()
#     ucontact = models.CharField(max_length=15)

#     class Meta:
#         db_table = 'user'

class User(models.Model):
  uid = models.AutoField(
    primary_key=True
  )

  uname = models.CharField(
    max_length=20,
    null=False,
    blank=False
  )

  uemail = models.EmailField(
    max_length=255,
    null=False,
    blank=False
  )

  ucontact= models.CharField(
    max_length=15,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'usertb'
