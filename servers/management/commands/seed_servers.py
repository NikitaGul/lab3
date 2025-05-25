from django.core.management.base import BaseCommand
from servers.models import Server
from datetime import time

class Command(BaseCommand):
    help = "create servers"

    def handle(self, *args, **kwargs):
        data = [
            {
                "name": "Web 1", "alert_time": time(9, 0), "notification_type": "email",
                "email": "web1@example.com", "server_group": "Web", "server_group_type": "Production", "location": "Kyiv"
            },
            {
                "name": "Web 2", "alert_time": time(10, 0), "notification_type": "sms",
                "email": "web2@example.com", "server_group": "Web", "server_group_type": "Production", "location": "Lviv"
            },
            {
                "name": "DB 1", "alert_time": time(12, 30), "notification_type": "push",
                "email": "db1@example.com", "server_group": "BD", "server_group_type": "Test", "location": "Odesa"
            },
            {
                "name": "Monitor", "alert_time": time(8, 45), "notification_type": "email",
                "email": "monitor@example.com", "server_group": "Infrastructure", "server_group_type": "Monitoring", "location": "Kharkiv"
            },
            {
                "name": "Backup", "alert_time": time(23, 0), "notification_type": "email",
                "email": "backup@example.com", "server_group": "Security", "server_group_type": "Backups", "location": "Dnipro"
            },
        ]

        for entry in data:
            Server.objects.create(**entry)

        self.stdout.write(self.style.SUCCESS('success added servers.'))
