from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField

SUBCATEGORY_COUNTRY_CHOICES = (
    ('india', 'INDIA'),
    # ('india', 'INDIA'),
    # ('usa', 'USA'),
    # ('brazil', 'BRAZIL'),
)

SUBCATEGORY_CITY_CHOICES = (
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Nagpur', 'Nagpur'),
    ('Delhi', 'Delhi'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Surat', 'Surat'), 
    ('Jaipur', 'Jaipur'),
    ('Lucknow', 'Lucknow'),
    ('Bhopal', 'Bhopal'),
    ('Indore', 'Indore'),
    ('Patna', 'Patna'),
    ('Srinagar', 'Srinagar'),
    ('Ranchi', 'Ranchi'),
    ('Raipur', 'Raipur'),
    ('Chandigarh', 'Chandigarh'),
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Dehradun', 'Dehradun'),
    ('Jammu', 'Jammu'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Shimla', 'Shimla'),
    
)

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = AutoSlugField(populate_from='name', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Job(models.Model):
    job_offered_by = models.ForeignKey(User, related_name='job_offered_by', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='job_category', on_delete=models.CASCADE)
    country = models.CharField(max_length=20, choices=SUBCATEGORY_COUNTRY_CHOICES, default='india')
    city = models.CharField(max_length=20, choices=SUBCATEGORY_CITY_CHOICES, default='Mumbai')
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=False)
    slug = AutoSlugField(populate_from='name', null=False)

    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Applicant(models.Model):
    applicant_name = models.ForeignKey(User, related_name='job_applied_by', on_delete=models.CASCADE)
    job_name = models.ForeignKey(Job, related_name='job_applied_name', null=True, blank=True, on_delete=models.CASCADE)   
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name