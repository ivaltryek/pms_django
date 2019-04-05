from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class StudentDetails(models.Model):
    student_id  = models.CharField(max_length=10, default ='')
    student_cpi = models.FloatField(max_length=6, default=0.00)
    firstname = models.CharField(max_length=20,default='')
    lastname = models.CharField(max_length=20,default='')
    department = models.CharField(max_length=2,default='')
    slug = models.SlugField (
    verbose_name = "Slug",
    allow_unicode = True,
    unique=True
    )
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.student_id)
        super(StudentDetails, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}".format(self.student_id)


class RegisterdStudents(models.Model):
    registered_student = models.ForeignKey(StudentDetails,related_name = 'student_rid',on_delete = models.DO_NOTHING)

    def __str__(self):
        return "{0}".format(self.registered_student)