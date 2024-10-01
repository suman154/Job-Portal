from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    cover_letter = models.TextField()

    def __str__(self):
        return f"Application by {self.applicant_name} for {self.job.title}"



