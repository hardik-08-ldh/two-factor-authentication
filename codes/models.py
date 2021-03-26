from django.db import models
from users.models import CustomUser
import random
# Create your models here.

class Code(models.Model):
    number=models.CharField(max_length=5,blank=True)
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self,*args,**kwargs):
        number_list=[0,1,2,3,4,5,6,7,8,9]
        code_items=[]

        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)

        code_string="".join(str(item) for item in code_items)
        self.number=code_string

        super().save(*args,**kwargs)
