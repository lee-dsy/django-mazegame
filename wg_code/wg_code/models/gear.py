from django.db import models
from user import Character


# Gear is for realistic items, no enchanting allowed
# This template may never be able to be deleted
class GearTemplate(models.Model):
    name = models.CharField(max_length=50)
    max_durability = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Gear(models.Model):
    character_owner = models.ForeignKey(Character, on_delete=models.CASCADE) # Delete all characters if the User goes
    gear_template = models.ForeignKey(GearTemplate, on_delete=models.CASCADE)
    acqire_date = models.DateField()
    level = models.IntegerField()
    cur_durability = models.IntegerField()

    def __str__(self):
        return f"{self.gear_template} owned by {self.character_owner}"

class ItemTemplate(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"