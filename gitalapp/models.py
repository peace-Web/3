from django.db import models

# Create your models here.


class Package(models.Model):
    type = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    feature1 = models.CharField(max_length=200, null=True)
    feature2 = models.CharField(max_length=200, null=True)
    feature3 = models.CharField(max_length=200, null=True)
    feature4 = models.CharField(max_length=200, null=True)
    feature5 = models.CharField(max_length=200, null=True)
    feature6 = models.CharField(max_length=200, null=True)
    feature7 = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.type


class Order(models.Model):
    PACKAGE = (("package1", "package2"), ("package2", "package2"), ("package3",
               "package3"), ("package4", "package4"), ("package5", "package5"))
    PAY = (("paypal", "paypal"), ("creditCard", "creditCard"))
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    # package = models.ForeignKey(Package, null=True, on_delete=models.SET_NULL)
    package = models.CharField(max_length=100, null=True)
    pay_gateway = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.first_name
