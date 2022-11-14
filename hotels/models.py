from django.db import models


class HotelAdmin(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя администратора')
    surname = models.CharField(max_length=200, verbose_name='Фамилия администратора')
    midname = models.CharField(max_length=200, verbose_name='Отчество администратора')

    class Meta:
        verbose_name = 'Администратор отеля'
        verbose_name_plural = 'Администраторы отелей'
    
    
    def __str__(self):
        return f'{self.surname} {self.name} {self.midname}'


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название места')

    class Meta:
        verbose_name = 'Местонахождение'
        verbose_name_plural = 'Местонахождения'
    
    def __str__(self):
        return f'{self.name}'



class Hotel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название отеля')
    phone = models.CharField(max_length=100, verbose_name='Контактный телефон')
    admin = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE, verbose_name='Администратор отеля')
    description = models.TextField(verbose_name='Описание отеля')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Местонахождение отеля')

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return f'Отель: {self.name}'