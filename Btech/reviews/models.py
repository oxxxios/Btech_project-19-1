from django.db import models

class Review(models.Model):
    text = models.CharField(max_length=200)
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.tech


    class Meta:
        verbose_name = "Отзыв"
        verbose_name = "Отзывы"
