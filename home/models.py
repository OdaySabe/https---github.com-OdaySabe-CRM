from django.db import models
from login.models import BaseModel
from django.core.validators import  MinValueValidator 
from login.models import Role

class Agents(BaseModel):
    first_name=models.fields.CharField(max_length=50,blank=False,null=False)
    last_name=models.fields.CharField(max_length=50,blank=False,null=False)
    country=models.fields.CharField(max_length=50,blank=False,null=False)
    age=models.fields.IntegerField(validators=[MinValueValidator(18)])
    balance=models.fields.FloatField(validators=[MinValueValidator(0)])

    role=models.OneToOneField(Role, verbose_name="user_role", on_delete=models.CASCADE)


