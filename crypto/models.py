from django.db import models

# Create your models here.


# registration form will diaplay users visual cryptography image on registration, it will redirect the user to the page

class RegistrationModel(models.Model):
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)


# During login form asks for cryptography image
class LoginFormModel(models.Model):
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    users_share = models.ImageField(upload_to = "shares/")
    
    



