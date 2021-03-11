from django.db import models

class Org(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = True
        db_table = 'Org'
    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    org = models.ForeignKey('Org', models.DO_NOTHING, verbose_name="Organization")
    max_capacity = models.IntegerField(verbose_name="Maximum Capacity")
    current_capacity = models.IntegerField(verbose_name="Current Capacity", default=0)

    class Meta:
        managed = True
        db_table = 'Room'
    def __str__(self):
        return self.name
    def vn(self,field):
        return self._meta.get_field(field).verbose_name
    def headers(self):
        return['ID', self.vn('name'),self.vn('max_capacity')]
    def details(self):
        return[self.id, self.name,self.max_capacity]


class User(models.Model):
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    uname = models.CharField(max_length=100, unique=True, verbose_name="Username")
    password = models.CharField(max_length=1023)
    email = models.CharField(max_length=250, verbose_name="Email")
    admin = models.BooleanField()
    active = models.BooleanField()
    org = models.ForeignKey('Org', models.DO_NOTHING, blank=True, null=True)
    rooms = models.ManyToManyField('Room',through='UserRoomAccess',blank=True, null=True,verbose_name='Rooms')
    #note, admin users have default access to all rooms, room list will appear empty

    class Meta:
        managed = True
        db_table = 'User'
    def __str__(self):
        return self.fname + " " + self.lname
    def vn(self,field):
        return self._meta.get_field(field).verbose_name
    def headers(self):
        return["ID",self.vn('fname'),self.vn('lname'),self.vn('uname'),self.vn('email'),self.vn('admin'),self.vn('active'),self.vn('rooms')]
    def details(self):
        return[self.id,self.fname,self.lname,self.uname,self.email,self.admin,self.active,', '.join(self.getRoomNames())]
    def getRoomNames(self):
        if self.admin:
            return ['all']
        return [e.name for e in self.getRooms()]
    def getRooms(self):
        access = UserRoomAccess.objects.filter(user=self.id)
        rms = []
        for e in access:
            rms.append(e.room)
        return rms

class UserRoomAccess(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    room = models.ForeignKey(Room, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'UserRoom'
    def __str__(self):
        return self.user + "-" + self.room