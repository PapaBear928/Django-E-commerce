from django.conf import settings
from django.db import models
from django.urls import reverse


class ProductsMenager(models.Manager):
	def get_queryset(self):
		return super(ProductsMenager, self).get_queryset().filter(is_active=True)


class Categories(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def get_absolute_url(self):
		return reverse('store:category_list', args=[self.slug])

	def __str__(self):
		return self.name


class Products(models.Model):
	category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
	title = models.CharField(max_length=255, null=True, blank=False)
	author = models.CharField(max_length=255, default='admin')
	description = models.TextField(default="Short description. Maximum 200 signs", max_length=255, blank=True)
	price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
	product_pic = models.ImageField(upload_to="product_images/", null=True, blank=True,
	                                default='product_images/default.jpg')
	slug = models.SlugField(max_length=255)
	available = models.BooleanField(default=True)
	'''on_sale = models.BooleanField(default=True)'''
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(null=False, auto_now=True)
	updated = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	products = ProductsMenager()

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"
		ordering = ('-created',)

	def get_absolute_url(self):
		return reverse('store:product_detail', args=[self.slug])

	def __str__(self):
		return self.new_title()

	def new_title(self):
		return "Title:{}, Category:{}".format(self.title, self.category)
