from tabnanny import verbose
from django.db import models
from django.urls import reverse
from vendor.models import Vendor


class Category(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    category_picture = models.ImageField(upload_to='categoryimages', default='hotel.jpg')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    def __str__(self):
        return self.category_name


class ProductItem(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productitems')
    product_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='productimages')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
