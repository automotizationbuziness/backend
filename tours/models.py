from django.db import models
from hotels.models import Hotel
from contactface.models import ContactFace
from django.core.exceptions import ValidationError


class Tour(models.Model):
    TOUR_TYPES_OF_FOOD = (
        ('Без питания', 'Без питания'),
        ('С завтраком', 'С завтраком'),
        ('3-х разовое', '3-х разовое')
    )

    hotel = models.ForeignKey(Hotel, models.CASCADE, verbose_name='Отель')
    arrival_date = models.DateField(verbose_name='Дата заезда')
    departure_date = models.DateField(verbose_name='Дата выезда')
    type_of_food = models.CharField(choices=TOUR_TYPES_OF_FOOD, max_length=100, verbose_name='Тип питания')
    cost = models.DecimalField(decimal_places=2, max_digits=32, verbose_name='Цена тура (руб.)')
    description = models.TextField(max_length=500, verbose_name='Описание тура')
    days = models.IntegerField(null=True, editable=False, verbose_name='Количество дней в отеле')
    nights = models.IntegerField(null=True, editable=False, verbose_name='Количество ночей в отеле')


    def clean(self):
        if ((self.departure_date - self.arrival_date).days <= 0):
            raise ValidationError('Дата выезда не может быть раньше даты заезда')
        if (self.cost < 0):
            raise ValidationError('Цена не может быть меньше 0 руб.')


    def save(self, *args, **kwargs) -> None:
        
        self.days = (self.departure_date - self.arrival_date).days
        self.nights = self.days - 1
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
    
    def __str__(self) -> str:
        return f"Тур в {self.hotel} по цене {self.cost_display}"

    @property
    def cost_display(self):
        return f'{self.cost} руб'


class TourClient(models.Model):
    CLIENT_TYPES = (
        ('Физическое лицо', 'Физическое лицо'),
        ('Юридическое лицо', 'Юридическое лицо')
    )
    name = models.CharField(verbose_name='Имя клиента', max_length=100)
    contact_face = models.ForeignKey(ContactFace, on_delete=models.CASCADE, verbose_name='Контактное лицо')
    client_type = models.CharField(choices=CLIENT_TYPES, max_length=100, default=CLIENT_TYPES[0], verbose_name='Тип клиента')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    def __str__(self) -> str:
        return f'Клиент: {self.name}'