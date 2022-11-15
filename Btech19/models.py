from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PodCategories(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Modeli_tovarov(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ForeignKey(PodCategories, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name