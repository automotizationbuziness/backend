from django.db import models
from order.models import Order
from tours.models import Tour, TourClient


class TourSale(models.Model):
    sale = models.ForeignKey(Order, models.CASCADE, verbose_name='Тур')
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Стоимость тура')

    def save(self, *args, **kwargs) -> None:
        #self.total_cost = self.sale.total_cost
        self.sale.state = 'Завершен (положительно)'
        if self._state.adding:
            tour_end = TourSaleEnd()
            tour_end.client = self.sale.client
            tour_end.payment_type = self.sale.payment_type
            tour_end.save()
            for order_tour in self.sale.orders.all():
                print(order_tour)
                order_tour_end = OrderTourEnd()
                order_tour_end.tour = order_tour.tour
                order_tour_end.cost = order_tour.cost
                order_tour_end.tourist_amount = order_tour.tourist_amount
                order_tour_end.tour_endings = tour_end
                order_tour_end.save()
            tour_end.save()

        return super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = 'Оплата тура'
        verbose_name_plural = 'Оплата туров'
    
    def __str__(self) -> str:
        return f'Оплата тура: {self.sale}'


class TourSaleEnd(models.Model):
    PAYMENT_TYPES_CHOICES = (
        ('Предоплата', 'Предоплата'),
        ('Кредит', 'Кредит')
    )
    ACCEPTED_CHOICES = (
        ('Подтверждена', 'Подтверждена'),
        ('Не подтверждена', 'Не подтверждена')
    )
    has_accepted = models.CharField(choices=ACCEPTED_CHOICES, default='Не подтверждена', max_length=100, verbose_name='Бронь номеров подтверждена в отеле')
    client = models.ForeignKey(TourClient, on_delete=models.CASCADE, verbose_name='Клиент')
    payment_type = models.CharField(choices=PAYMENT_TYPES_CHOICES, max_length=100, verbose_name='Вид оплаты')
    #total_cost = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Общая стоимость заказа', editable=False, default=0)

    @property
    def total_cost(self):
        """Общая стоимость заказа"""
        return sum(map(lambda x: x.total_cost, self.orders.all()))
    
    total_cost.fget.short_description = 'Общая стоимость заказа (руб.)'

    class Meta:
        verbose_name = 'Продажа тура'
        verbose_name_plural = 'Продажа туров'
    
    # def save(self, *args, **kwargs) -> None:
    #     self.total_cost = sum(map(lambda x: x.total_cost, self.orders.all()))
    #     print(self.total_cost)
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Заказ тура у {self.client} на {self.total_cost}руб.'


class OrderTourEnd(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    cost = models.DecimalField(max_digits=100, max_length=100, decimal_places=2, verbose_name='Цена (руб.)')
    tourist_amount = models.PositiveIntegerField(verbose_name='Количество человек')
    total_cost = models.DecimalField(max_digits=100, max_length=100, decimal_places=2, verbose_name='Стоимость (руб.)', editable=False)
    tour_endings = models.ForeignKey('toursale.TourSaleEnd', on_delete=models.CASCADE, null=True, related_name='orders')

    def save(self, *args, **kwargs) -> None:
        self.total_cost = self.tourist_amount * self.cost
        return super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f''
    
    
    class Meta:
        verbose_name_plural = 'Список продаваемых туров'
        verbose_name = 'Продаваемый тур'