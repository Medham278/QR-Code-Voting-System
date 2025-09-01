from django.db import models

# Create your models here.
religions=[
    ('Hindu','Hindu'),
    ('Islam','Islam'),
    ('Christian','Christian'),
    ('Jain','Jain'),
    ('Buddhist','Buddhist'),
    ('Sikh','Sikh'),
    ('Others','Others'),     
]

genders=[
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Rather Not Say'),
]
class Voter(models.Model):
    vid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    gender=models.CharField(max_length=30, choices=genders)
    dob=models.DateField()
    religion=models.CharField(max_length=20, choices=religions)
    dp=models.FileField(upload_to='vote/photos/')
    address=models.TextField()
    aadhar=models.PositiveIntegerField()
    pan=models.CharField(max_length=10)
    ebill=models.FileField(upload_to='vote/electricitybills/')
    def __str__(self):
        return f"VoterID:{self.vid} Name:{self.name}"