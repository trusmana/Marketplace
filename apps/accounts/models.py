from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from PIL import Image

class AccountsUser(AbstractUser):
    email = models.EmailField(_('email address'),unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar", blank= True)

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.avatar.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (250, 250)
            img.thumbnail(output_size) # Resize image
            img.save(self.avatar.path)
