from django.db import models
from django.contrib.auth.models import User


class Catalogue(models.Model):
    class Meta:
        verbose_name_plural = "Catalogue"
    isbn = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.DateField()
    cover = models.ImageField(null=True)
    callno = models.ForeignKey(
        "callnumber", blank=True, on_delete=models.PROTECT)
    author = models.ForeignKey("author", blank=True, on_delete=models.PROTECT)
    publisher = models.ForeignKey(
        "publisher", blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.name


class CallNumber(models.Model):
    class Meta:
        verbose_name_plural = "Call Number"
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CheckOut(models.Model):
    options = [
        ("YES", "YES"),
        ("NO", "NO"),
    ]
    book = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    issuedate = models.DateField(auto_now_add=True)
    duedate = models.DateField()
    CheckedIn = models.CharField(max_length=3, choices=options)
    fine = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return self.CheckedIn


class Subject(models.Model):
    class Meta:
        verbose_name_plural = "Subject"
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
