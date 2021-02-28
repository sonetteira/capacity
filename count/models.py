from django.db import models

class Org(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = True
        db_table = 'Org'
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    org = models.ForeignKey('Org', models.DO_NOTHING)
    max_capacity = models.IntegerField()
    current_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Room'
    def __str__(self):
        return self.name


class User(models.Model):
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    password = models.CharField(max_length=1023)
    admin = models.BooleanField()
    active = models.BooleanField()
    org = models.ForeignKey('Org', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'User'
        unique_together = ('fname', 'lname')
    def __str__(self):
        return self.fname + " " + self.lname

class UserRoomAccess(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    room = models.ForeignKey(Room, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'UserRoom'
    def __str__(self):
        return self.user + "-" + self.room