from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Node(MPTTModel):
    attribute_name = models.CharField(max_length=64)
    parent = TreeForeignKey(
        'self', 
        null=True, 
        blank=True, 
        related_name='children', 
        on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f'{self.attribute_name}(ID {self.id})'
