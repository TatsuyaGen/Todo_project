from django.db import models

# Create your models here.
class Plandata(models.Model):
    toki = models.DateField()
    basho = models.CharField(max_length = 50)
    naiyo = models.CharField(max_length = 100)

    def __str__(self):
        return 'Plandata: id=' + str(self.id) + ', date=' + str(self.toki) + ', location=' + self.basho + ', content=' + self.naiyo

class Completion(models.Model):
    toki = models.DateField()
    kanryo_day = models.DateField()
    basho = models.CharField(max_length = 50)
    naiyo = models.CharField(max_length = 100)

    def __str__(self):
        return 'Plandata: id=' + str(self.id) + ', date=' + str(self.toki) + ', complete_date=' + str(self.kanryo_day) + ', location=' + self.basho + ', content=' + self.naiyo