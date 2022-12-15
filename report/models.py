from django.db import models
from tours.models import Tour
from order.models import OrderTour
from django.db.models.signals import post_save
from django.dispatch import receiver


class Report(models.Model):
    period_lte = models.DateField(verbose_name='Дата (начало отчета)')
    period_gte = models.DateField(verbose_name='Дата (конец отчета)')
    payed_sum = models.DecimalField(editable=False, max_digits=100, decimal_places=2, verbose_name='Остаток на счете', null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return f"Отчет с {self.period_lte} по {self.period_gte}"

    def save(self, *args, **kwargs) -> None:
        if self._state.adding == True:
            payed_sum = 0
            raised_sum = 0
            tours = Tour.objects.filter(created__gte=self.period_lte, created__lte=self.period_gte)
            for tour in tours:
                rt = ReportTable()
                rt.tour = tour
                is_offer = len(OrderTour.objects.filter(tour=tour))
                rt.has_offer = 'Да' if is_offer else 'Нет'
                if is_offer:
                    is_payed = OrderTour.objects.filter(tour=tour, order__state='Завершен (положительно)')
                    rt.has_payed = 'Да' if is_payed else 'Нет'
                    payed_sum += sum(map(lambda x: x.total_cost, OrderTour.objects.filter(tour=tour, order__state='Действует'))) + sum(map(lambda x: x.total_cost, OrderTour.objects.filter(tour=tour, order__state='Завершен (положительно)')))
                    raised_sum += sum(map(lambda x: x.total_cost, OrderTour.objects.filter(tour=tour, order__state='Завершен (положительно)')))
                if not is_offer: rt.has_payed = 'Нет'
                #rt.save()
            self.payed_sum = raised_sum - payed_sum
        return super().save(*args, **kwargs)



class ReportTable(models.Model):
    TABLE_CHOICES = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )

    class Meta:
        verbose_name = 'Список туров'
        verbose_name_plural = 'Списки туров'

    def save(self, *args, **kwargs) -> None:
        self.report = Report.objects.all().last()
        return super().save(*args, **kwargs)

    tour = models.ForeignKey(Tour, verbose_name='Тур', on_delete=models.CASCADE, null=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    has_offer = models.CharField(verbose_name='Заказан', choices=TABLE_CHOICES, max_length=100)
    has_payed = models.CharField(verbose_name='Продан', choices=TABLE_CHOICES, max_length=100)

    def __str__(self):
        return ""

@receiver(post_save, sender=Report)
def cr(sender, instance, **kwargs):
    payed_sum = 0
    raised_sum = 0
    tours = Tour.objects.filter(created__gte=instance.period_lte, created__lte=instance.period_gte)
    for tour in tours:
        rt = ReportTable()
        rt.tour = tour
        is_offer = len(OrderTour.objects.filter(tour=tour))
        rt.has_offer = 'Да' if is_offer else 'Нет'
        if is_offer:
            is_payed = OrderTour.objects.filter(tour=tour, order__state='Завершен (положительно)')
            rt.has_payed = 'Да' if is_payed else 'Нет'
            payed_sum += sum(map(lambda x: x.total_cost, OrderTour.objects.filter(tour=tour, order__state='Действует')))
            raised_sum += sum(map(lambda x: x.total_cost, OrderTour.objects.filter(tour=tour, order__state='Завершен (положительно)')))
        else: rt.has_payed = 'Нет'
        rt.save()
    
            