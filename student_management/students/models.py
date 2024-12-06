from django.db import models

class Students(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentsPNo(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    pno = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student.name} - {self.pno}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class Scores(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.subject_name} - {self.marks}"
