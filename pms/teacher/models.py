import datetime

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.



class AddPlacement(models.Model):
    department = models.CharField(max_length=2, default ='')
    company = models.CharField(default = '', max_length=25)
    due_date = models.DateField(default = datetime.date.today, verbose_name='Due Date')
    company_url = models.URLField(default = '')
    criteria = models.CharField(max_length=500,default='')


    def __str__(self):
        return '{0} , {1}'.format(self.company, self.department)

    def get_absolute_url(self):
        return reverse("superuser:detail",kwargs={'pk':self.pk})