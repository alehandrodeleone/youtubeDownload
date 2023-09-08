from django.db import models

class links(models.Model):
    Links=models.CharField(max_length=200, null=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True)
