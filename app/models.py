from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.IntegerField()
    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_day = models.DateField()

    job = models.CheckConstraint
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    # Add other fields like address, social media links, etc. as needed

    def __str__(self):
        return self.first_name
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    images = models.ImageField(upload_to='static/')
    project_url = models.URLField(blank=True, null=True)
    github_repository = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    # Add other fields as needed

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    little_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    diploma = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    little_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.diploma} at {self.institution}"