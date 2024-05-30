from django.db import models
from django.contrib.auth.models import User
from .utils import get_current_user
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(
        User,
        null=True,
        editable=False,
        related_name="%(class)s_created",
        on_delete=models.DO_NOTHING,
        verbose_name='Created by'
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        editable=False,
        related_name="%(class)s_updated",
        on_delete=models.DO_NOTHING,
        verbose_name='Updated by'
    )
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            self.updated_by = user
            if not self.id:
                self.created_by = user
        super(BaseModel, self).save(*args, **kwargs)
    
class Role(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Support', 'Support'),
        ('Developer', 'Developer'),
        ('OnlyAgent', 'OnlyAgent'),
    ]
    type = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='OnlyAgent')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        null=True
    )

