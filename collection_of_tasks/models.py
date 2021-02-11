from django.db import models
import uuid

# Create your models here.

class Organization(models.Model):
    Guid_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    Id_higher_organization = models.OneToOneField(Guid_id,)
    Name = models.