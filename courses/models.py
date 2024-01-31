from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Categories(BaseModel):
    title = models.CharField(max_length = 255)
    amount = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.title

class SocialNetworks(BaseModel):
    facebook_url=models.CharField(max_length=255)
    instagram_url=models.CharField(max_length=255)
    youtube_url=models.CharField(max_length=255)
    telegram_url=models.CharField(max_length=255)
    tiktok_url=models.CharField(max_length=255)

    
class Interviews(BaseModel):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    time = models.CharField(max_length=20)
    author = models.CharField(max_length=30, default='who')

    def __str__(self) -> str:
        return self.title
    

class CourseArchive(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    class Status(models.TextChoices):
        BOUGHT = 'BT', 'Bought'
        UNBOUGHT = 'UB', 'Unbought'

    action = models.CharField( max_length=2, 
                              choices = Status.choices,
                              default=Status.BOUGHT)
    
    short_content = models.CharField(max_length=20)
    

class CourseList(BaseModel):
    title = models.CharField(max_length=100)

    class Status(models.TextChoices):
        BOUGHT = 'BT', 'Bought'
        UNBOUGHT = 'UB', 'Unbought'
        PROGRESS = 'PG', 'Progress'

    action = models.CharField( max_length=2, 
                              choices = Status.choices,
                              default=Status.BOUGHT)
    
    
    
