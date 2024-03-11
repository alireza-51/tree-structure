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
    
    def __str__(self) -> str:
        return f'{self.attribute_name}(ID {self.id})'
