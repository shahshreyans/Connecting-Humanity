from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
from django.utils.text import slugify


class RegisterNgoModel(AbstractUser):
    contactno_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                     message="Format:'+999999999'. Up to 15 digits allowed.")

    category_choice = [('No Poverty', 'No Poverty'), ('No Hunger', 'No Hunger'), ('Good Health', 'Good Health'),
                       ('Quality Education', 'Quality Education')]

    ngo_id = models.BigAutoField(primary_key=True)
    ngo_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=10, default='Ahmedabad')
    state = models.CharField(max_length=10, default='Gujarat')
    contact_number = models.CharField(validators=[contactno_regex], max_length=17)
    website = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=category_choice, default='No Poverty')
    mission = models.CharField(max_length=500)
    paypal_account = models.EmailField(blank=True)
    bank_name = models.CharField(max_length=100)
    bank_account_number = models.IntegerField(null=True)
    bank_ifsc_code = models.CharField(max_length=15)
    register_date = models.DateTimeField(auto_now_add=True)
    ngo_logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.ngo_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ngo_name)
        super(RegisterNgoModel, self).save(*args, **kwargs)


class NgoActivityModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True, blank=True)
    detail = models.TextField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    location_map_url = models.URLField()
    location = models.CharField(max_length=20)
    note_for_donner = models.TextField(max_length=1000)
    note_for_needy = models.TextField(max_length=1000)
    document_list = models.TextField(max_length=1000, null=True, blank=True)
    posted_date = models.DateField(auto_now_add=True)
    posted_time = models.TimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    ngo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(NgoActivityModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['complete']
