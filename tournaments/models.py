from django.db import models
from django.contrib.auth.models import User

# Tournament types
TOURNAMENT_TYPES = (
    ('T20', 'Twenty20'),
    ('TEST', 'Test Match'),
    ('ODI', 'One Day International'),
)

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='tournaments_images/', blank=True, null=True)
    tournament_type = models.CharField(max_length=4, choices=TOURNAMENT_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    registration_deadline = models.DateField()
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_tournament_type_display()})"

    @property
    def is_registration_open(self):
        from datetime import date
        return date.today() <= self.registration_deadline
