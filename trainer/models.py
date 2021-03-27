from django.db import models


class Student(models.Model):
    name = models.CharField("Name", max_length=30)
    email = models.EmailField("Email", max_length=50)
    comment = models.TextField("Comment", max_length=1000)

    def __str__(self):
        return f"{self.email}"


class User(models.Model):
    first_name = models.CharField("First name", max_length=30)
    second_name = models.CharField("Second name", max_length=30)
    login = models.CharField("Login", max_length=30)
    email = models.EmailField("Email", max_length=50)
    password = models.CharField("Password", max_length=30)

    def __str__(self):
        return f"{self.login} {self.password}"
