from django.db import models

class Node(models.Model):
    attribute_name = models.CharField(max_length=64)
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        related_name='children', 
        on_delete=models.CASCADE
    )
