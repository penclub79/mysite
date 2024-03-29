from django.db import models

# Create your models here.
class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    content = models.CharField(max_length=2000)
    regdate = models.DateTimeField(auto_now=True)   #자동 시스템시간을 넣겟다.

    def __str__(self):
        return 'Guestbook(%s, %s, %s, %s)' % (self.name, self.password, self.contents, self.regdate)

