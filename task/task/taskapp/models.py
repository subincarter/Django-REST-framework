from django.db import models

# Create your models here.
class newtask(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=300)
    end_date=models.DateField()
    CHOICES=((1,'open'),
             (2,'close'))
    status=models.CharField(max_length=1, choices=CHOICES)
    comments=models.CharField(max_length=200)
    class Meta:
        verbose_name='newtask'
        verbose_name_plural='newtasks'
    def __str__(self):
        return self.title

