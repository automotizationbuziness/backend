from django.db import models
from tours.models import Tour, TourClient
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    PAYMENT_TYPES_CHOICES = (
        ('Предоплата', 'Предоплата'),
        ('Кредит', 'Кредит')
    )

    client = models.ForeignKey(TourClient, on_delete=models.CASCADE, verbose_name='Клиент')
    payment_type = models.CharField(choices=PAYMENT_TYPES_CHOICES, max_length=100, verbose_name='Вид оплаты')
    #total_cost = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Общая стоимость заказа', editable=False, default=0)

    @property
    def total_cost(self):
        """Общая стоимость заказа"""
        return sum(map(lambda x: x.total_cost, self.orders.all()))
    
    total_cost.fget.short_description = 'Общая стоимость заказа (руб.)'

    class Meta:
        verbose_name = 'Заказ тура'
        verbose_name_plural = 'Заказы туров'
    
    # def save(self, *args, **kwargs) -> None:
    #     self.total_cost = sum(map(lambda x: x.total_cost, self.orders.all()))
    #     print(self.total_cost)
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Заказ тура у {self.client} на {self.total_cost}руб.'


class OrderTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    cost = models.DecimalField(max_digits=100, max_length=100, decimal_places=2, verbose_name='Цена (руб.)')
    tourist_amount = models.PositiveIntegerField(verbose_name='Количество человек')
    total_cost = models.DecimalField(max_digits=100, max_length=100, decimal_places=2, verbose_name='Стоимость (руб.)', editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')

    
    def save(self, *args, **kwargs) -> None:
        self.total_cost = self.tourist_amount * self.cost
        return super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f''
    
    
    class Meta:
        verbose_name_plural = 'Список продаваемых туров'
        verbose_name = 'Продаваемый тур'


# @receiver(post_save, sender=Order)
# def save_order(sender, instance, **kwargs):
#     instance.total_cost = sum(map(lambda x: x.total_cost, instance.orders.all()))
#     print(instance, "fuck", instance.total_cost)
#     post_save.disconnect(save_order, sender=Order)
#     instance.save()
#     post_save.connect(save_order, sender=Order)
    