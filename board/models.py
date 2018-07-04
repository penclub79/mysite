from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=1)      #조회수
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #주 키가 삭제되면 같이 함께 삭제되어라

    def __str__(self):
        return "Board(%s, %s, %s, %s, %s, %d" % \
               self.title, \
               self.name, \
               self.content,\
               self.hit, \
               str(self.regdate), \
               self.user.id