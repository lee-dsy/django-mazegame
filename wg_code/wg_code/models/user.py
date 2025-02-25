from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100) # Eventually bcrypted
    acc_create_date = models.DateField()
    last_login = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Delete all characters if the User goes
    name = models.CharField(max_length=50)
    create_date = models.DateField() # Should be read only
    description = models.TextField()
    level = models.IntegerField() # Cap at 100
    expierence_to_next_level = models.IntegerField()
    effects = models.Aggregate # Array, somewhere here ?... Oh, no array in SQLite :(

    def __str__(self):
        return f"{self.name}"


class Health(models.Model): # Health module, not much more needed here
    health = models.IntegerField()
    max_health = models.IntegerField()

    def __str__(self):
        return f"{self.health} / {self.max_health}"