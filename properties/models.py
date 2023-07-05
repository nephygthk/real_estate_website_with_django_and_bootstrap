from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs): 
        name_slug = self.name[:50]
        self.slug = slugify(name_slug)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("properties:category_list", args=[self.slug])

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    bedroom = models.CharField(max_length=30, null=True, blank=True)
    bathroom = models.CharField(max_length=30, null=True, blank=True)
    details = models.TextField()
    top_image = models.FileField(upload_to='top_images', null=True, blank=True)
    is_top_sale = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreignkeys
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            title_slug = self.title[:50]
            self.slug = slugify(title_slug)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Media(models.Model):
    property_image = models.FileField(upload_to='property_images')
    house_property = models.ForeignKey(Property, related_name='property', on_delete=models.CASCADE)

    def __str__(self):
        return self.house_property.title
