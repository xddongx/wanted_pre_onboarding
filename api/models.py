from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    company = models.ForeignKey(Company, related_name="company", on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    compensation = models.IntegerField()
    content = models.TextField()
    stack = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.company.name}, {self.position}'

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Application(models.Model):
    jobPosting = models.ForeignKey(JobPosting, related_name="jobPosting", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
