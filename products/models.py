from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	featured = models.ImageField(null=True)
	price = models.DecimalField(max_digits=100, decimal_places=2,null=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.featured.url
		except:
			url = ''
		print('URL:', url)
		return url
	


class Image(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	image = models.ImageField()

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		print('URL:', url)
		return url
