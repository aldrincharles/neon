from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='Active')
    location = models.CharField(max_length=255, blank=True)
    salary_range = models.CharField(max_length=255, blank=True)
    positions_filled = models.IntegerField(default=0)
    positions_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    GRADE_CHOICES = [
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)  # The applicant's current job title
    industry = models.CharField(max_length=255)
    applied_date = models.CharField(max_length=100)  # String for simplicity ('2 days ago')
    avatar_url = models.URLField(max_length=500, blank=True)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    verified_grade = models.CharField(max_length=20, choices=GRADE_CHOICES, blank=True)

    def __str__(self):
        return self.name
