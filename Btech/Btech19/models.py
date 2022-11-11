from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)     # категория
    image = models.ImageField(upload_to='')                                         # фото продукта
    product_name = models.CharField(max_length=100)                                 # имя продукта
    installment = models.TextField(blank=True, null=True)                           # рассрочка
    title = models.CharField(max_length=80, null=True, blank=False)                 # название
    description = models.TextField(max_length=50, null=True, blank=False)           # описание
    price = models.TextField(max_length=20, blank=True, null=True)                  # цена
    cpu = models.CharField(max_length=50, null=True, blank=False)                   # процессор
    main_camera = models.CharField(max_length=50, null=True, blank=True)            # основная камера
    front_camera = models.CharField(max_length=50, null=True, blank=True)           # фронтальная камера
    memory = models.PositiveIntegerField(null=True, blank=False)                    # память
    ram = models.PositiveIntegerField(null=True, blank=False)                       # оперативная память

    def __str__(self):
        return self.title


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")


