from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.

class Organization(models.Model):
    Guid_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Id_higher_organization = models.OneToOneField('self',blank=True,null=True, on_delete=models.SET_NULL)
    Name = models.CharField(verbose_name="Название организации", max_length=150)
    Index = models.IntegerField(verbose_name="Индекс местонахождения", max_length=10)
    Location = models.CharField(verbose_name="Местонахождение", max_length=150)
    Postal_code = models.IntegerField(verbose_name="Почтовый индекс", max_length=10,blank=True)
    Postal_location = models.CharField(verbose_name="Почтовый адрес", max_length=150,blank=True)
    INN = models.IntegerField(verbose_name="ИНН", max_length=10)
    KPP = models.IntegerField(verbose_name="КПП", max_length=9)
    OGRN = models.IntegerField(verbose_name="ОГРН", max_length=13, blank=True)
    OKPO = models.IntegerField(verbose_name="ОКПО", max_length=8, blank=True)
    UFK_LS = models.CharField(verbose_name="л/сч УФК", max_length=13,blank=True)
    Treasury_AC = models.IntegerField(verbose_name="Казначейский счет", max_length=20, blank=True)
    Ed_Treasury_AC = models.IntegerField(verbose_name="Единый казначейский счет", max_length=20, blank=True)
    Bank = models.CharField(verbose_name="Название банка", max_length=150, blank=True)
    Bik_Bank = models.IntegerField(verbose_name="Бик банка", max_length=9, blank=True)
    Phone = PhoneNumberField(verbose_name="Телефон организации",blank=True,unique=True)
    E_mail = models.EmailField(blank=True,unique=False)

