from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    details = models.TextField()
    top_image = models.FileField(upload_to='top_images', null=True, blank=True)
    is_top_sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreignkeys
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ('-created',)

    def __str__(self):
        return self.title
    

class Media(models.Model):
    property_image = models.FileField(upload_to='property_images')
    house_property = models.ForeignKey(Property, related_name='property', on_delete=models.CASCADE)

    def __str__(self):
        return self.house_property.title
