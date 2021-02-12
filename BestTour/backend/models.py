from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    sum = models.PositiveSmallIntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.job.name


class RoomType(models.Model):
    name = models.CharField("Тип номера", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип номера"
        verbose_name_plural = "Типы номеров"


class MealType(models.Model):
    name = models.CharField("Тип питания", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Типы питания"
        verbose_name = "Тип питания"


class Hotel(models.Model):
    name = models.CharField("Наименование", max_length=60)
    city = models.CharField("Город", max_length=20)
    roomType = models.ForeignKey(RoomType, verbose_name="Тип номера", on_delete=models.CASCADE,
                                 related_name='room_type')
    rating = models.PositiveSmallIntegerField("Количество звезд", default=1)

    def __str__(self):
        return f"{self.name}, {self.city} {self.rating}*"

    class Meta:
        verbose_name_plural = "Отели"
        verbose_name = "Отель"


class Tour(models.Model):
    destinationCountry = models.CharField("Страна назначения", max_length=20)
    departure = models.CharField("Город отправления", max_length=20)
    dayCount = models.PositiveSmallIntegerField("Количество ночей", default=1)
    date = models.DateField("Дата вылета", default=date.today)
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", on_delete=models.CASCADE, related_name='hotel_tour',
                              default=8)
    mealType = models.ForeignKey(MealType, verbose_name="Тип питания", on_delete=models.CASCADE,
                                 related_name='meal_tour', default=1)
    price = models.PositiveIntegerField("Цена", default=0)
    image = models.ImageField("Изображение", upload_to="images", blank=True, null=True, default='images/anapa.png')
    HotTour = models.BooleanField("Горящий тур", default=False)
    description = models.TextField("Описание", default="")

    def __str__(self):
        return self.destinationCountry

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class Status(models.Model):
    status = models.CharField("Статус", max_length=20)

    def __str__(self):
        return self.status


class BookedTour(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, verbose_name='Забронированый тур', on_delete=models.CASCADE, default=1)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Заброннированный тур"
        verbose_name_plural = "Забронированные туры"


class Request(models.Model):
    name = models.CharField("Имя", max_length=100)
    mail = models.EmailField("Почта", max_length=100)
    phone = models.CharField("Телефон", max_length=15)
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE, default=1,
                               related_name='status_req')

    def __str__(self):
        return self.name
