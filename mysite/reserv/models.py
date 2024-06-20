from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Stolik {self.number}"

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)  # Dodanie kolumny ID
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in hours")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', default=1)


    def __str__(self):
        return f"Rezerwacja na imię {self.name} w dniu {self.date} o godzinie {self.time}, na {self.duration} godz."

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name