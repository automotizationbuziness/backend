from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


class ContactFace(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО контактного лица')
    phone = PhoneNumberField(verbose_name='Контактный телефон')

    def __str__(self) -> str:
        return str(self.phone)
    
    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'
