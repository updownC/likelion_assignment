
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    year_choices = (
        ("2019", "2019년"),
        ("2020", "2020년"),
        ("2021", "2021년"),
        ("2022", "2022년"),
        ("2023", "2023년"),
    )
    month_choices = (
        ("1", '1월'),
        ("2", '2월'),
        ("3", '3월'),
        ("4", '4월'),
        ("5", '5월'),
        ("6", '6월'),
        ("7", '7월'),
        ("8", '8월'),
        ("9", '9월'),
        ("10", '10월'),
        ("11", '11월'),
        ("12", '12월'),
    )

    date_choices=(
        ("1", '1일'),
        ("2", '2일'),
        ("3", '3일'),
        ("4", '4일'),
        ("5", '5일'),
        ("6", '6일'),
        ("7", '7일'),
        ("8", '8일'),
        ("9", '9일'),
        ("10", '10일'),
        ("11", '11일'),
        ("12", '12일'),
        ("13", '13일'),
        ("14", '14일'),
        ("15", '15일'),
        ("16", '16일'),
        ("17", '17일'),
        ("18", '18일'),
        ("19", '19일'),
        ("20", '20일'),
        ("21", '21일'),
        ("22", '22일'),
        ("23", '23일'),
        ("24", '24일'),
        ("25", '25일'),
        ("26", '26일'),
        ("27", '27일'),
        ("28", '28일'),
        ("29", '29일'),
        ("30", '30일'),
        ("31", '31일'),
    )

    img = models.FileField(null=True)
    family_choices=(
        ("과일", '과일'),
        ("야채", '야채'),
        ("유제품", '유제품'),
        ("육류", '육류'),
        ("어류", '어류'),
        ("기타", '기타'),
    )
    family = models.CharField(
        choices = family_choices,
        default = "과일",
        max_length=200,
    )
    date = models.CharField(
        choices = date_choices, 
        default = "1",
        max_length=200,
    )
    month = models.CharField(
        choices = month_choices, 
        default = "5",
        max_length=200,
    )
    year = models.CharField(
        choices = year_choices, 
        default = "2019",
        max_length=200,
    )
    memo = models.TextField(max_length = 200)
    
    
    def __str__(self):
        return self.name


class Copost(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    user_name = models.CharField(max_length=200, default=" ")
    

    def __str__(self):
        return self.cotitle
