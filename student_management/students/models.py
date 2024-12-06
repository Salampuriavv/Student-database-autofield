from django.db import models

class Students(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentsPNo(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    pno = models.CharField(max_length=15)

    def __str__(self):
        return self.pno
