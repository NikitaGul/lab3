from django.db import models

class Server(models.Model):
    name = models.CharField("Name server", max_length=100)
    alert_time = models.TimeField("Time alert")

    NOTIFICATION_TYPES = [
        ("email", "Email"),
        ("sms", "SMS"),
        ("push", "Push-message"),
    ]

    notification_type = models.CharField("Type alert", max_length=10, choices=NOTIFICATION_TYPES)
    email = models.EmailField("Email adress")
    server_group = models.CharField("Servers group", max_length=100)
    server_group_type = models.CharField("Type group servers")
    location = models.CharField("Location server", max_length=200)

    def __str__(self):
        return f"{self.name} ({self.server_group} - {self.server_group_type})"

# Create your models here.
