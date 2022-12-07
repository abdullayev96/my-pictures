from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}{self.description}"
