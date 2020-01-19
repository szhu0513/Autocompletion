from djongo import models

class Text(models.Model):
    text = models.CharField(max_length=100)

class Prefix(models.Model):
    prefix = models.CharField(max_length=100)
    next_char = models.ArrayField(model_container=Text)
