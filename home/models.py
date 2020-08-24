from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.Autofield(primary_key = True)
    name =models.CharField(max_length = 120)
    email =models.CharField(max_length = 120)
    phone = models.CharField(max_length = 12)
    content = models.Textfield()
    timestamp = models.DateTimeField(auto_now_add=True, blank = True )


    def __str__(self):
        return self.name
