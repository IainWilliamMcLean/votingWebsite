from django.db import models


class GoodPoll(models.Model):
    option_1 = models.IntegerField(default=0)
    option_2 = models.IntegerField(default=0)
    option_3 = models.IntegerField(default=0)
    option_4 = models.IntegerField(default=0)
    option_5 = models.IntegerField(default=0)
    option_6 = models.IntegerField(default=0)
    option_7 = models.IntegerField(default=0)
    option_8 = models.IntegerField(default=0)


class BadPoll(models.Model):
    option_1 = models.IntegerField(default=0)
    option_2 = models.IntegerField(default=0)
    option_3 = models.IntegerField(default=0)
    option_4 = models.IntegerField(default=0)
    option_5 = models.IntegerField(default=0)
    option_6 = models.IntegerField(default=0)
    option_7 = models.IntegerField(default=0)
    option_8 = models.IntegerField(default=0)

