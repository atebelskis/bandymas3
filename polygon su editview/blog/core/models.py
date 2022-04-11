from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name
