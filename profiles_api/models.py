from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    
    def create_user(self, email, nama, umur, tanggal_lahir, codeforces_id, password=None):
        if not email:
            raise ValueError("Tidak ada email yang dimasukan")

        email = self.normalize_email(email)
        user = self.model(email=email, nama=nama, umur=umur, tanggal_lahir=tanggal_lahir, codeforces_id=codeforces_id)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nama, umur, tanggal_lahir, codeforces_id, password):
        user = self.create_user(email, nama, umur, tanggal_lahir, codeforces_id, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    nama = models.TextField(max_length=255)
    umur = models.IntegerField(null=True)
    tanggal_lahir = models.DateField()
    codeforces_id = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama', 'umur', 'tanggal_lahir', 'codeforces_id']

    def get_full_name(self):
        return self.nama
    
    def get_short_name(self):
        return self.nama

    def __str__(self):
        return self.email

class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    status_tags = models.CharField(max_length=25)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Text : {self.status_text} \n Tags : {self.status_tags}"