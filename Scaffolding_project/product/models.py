from django.db import models
from django.urls import reverse

# Create your models here.
class ProductRegister(models.Model):
    product_Name= models.CharField(max_length=100)
    productMaterialItemCode= models.CharField(max_length=100)
    productBrandNewSellingRate= models.FloatField()
    productSecondHandSellingRate= models.FloatField()
    productLossRate=models.FloatField()
    productRepairRate=models.FloatField()
    productCleaningRate=models.FloatField()
    productDailyRentalRate=models.FloatField()
    productWeeklyRentalRate=models.FloatField()
    productMonthlyRentalRate=models.FloatField()
    productDailyHireCharge=models.FloatField()
    productWeeklyHireCharge=models.FloatField()
    productMonthlyHireCharge=models.FloatField()
    productRecordedBy=models.CharField(max_length=100)
    supplierName=models.CharField(max_length=100)
    remarks=models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id])

    def get_update_url(self):
        return reverse('product_update',args=[self.id])

    def __str__(self):
        return self.product_Name