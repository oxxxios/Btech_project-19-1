from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='', null=True)
    title = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Название'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(max_length=20, null=True, blank=True, verbose_name='цена')
    cpu = models.CharField(max_length=50, null=True, blank=False)
    main_camera = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='основная камера'
    )
    front_camera = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='фронтальная камера'
    )
    memory = models.PositiveIntegerField(null=True, blank=False, verbose_name='память')
    ram = models.PositiveIntegerField(null=True, blank=False, verbose_name='оперативная память')
    is_active = models.BooleanField(default=True)
    is_hit = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
