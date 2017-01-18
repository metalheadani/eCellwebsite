from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=15, blank= False)
    last_name = models.CharField(max_length=15, blank= False)
    email = models.CharField(max_length=254, blank=False)
    contact = models.IntegerField(max_length=10, blank=False)

def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
