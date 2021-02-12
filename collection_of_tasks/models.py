from django.db import models
import uuid

# Create your models here.

class Organization(models.Model):
    Guid_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    Id_higher_organization = models.OneToOneField(Guid_id,blank=True)
    Name = models.CharField(verbose_name="Название организации", max_length=150)
    Index = models.IntegerField(verbose_name="Индекс местонахождения", max_length=10)
    Location = models.CharField(verbose_name="Местонахождение"max_length=150)
    Postal_code = models.IntegerField(verbose_name="Почтовый индекс", max_length=10)
    Postal_location = models.CharField(verbose_name="Почтовый адрес"max_length=150)
    INN = models.IntegerField(verbose_name="ИНН", max_length=10)
    KPP = models.IntegerField(verbose_name="КПП", max_length=9)
    OGRN = models.IntegerField(verbose_name="ОГРН", max_length=13, blank=True)
    OKPO = models.IntegerField(verbose_name="ОКПО", max_length=8, blank=True)
    

