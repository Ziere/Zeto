from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    phone_number = models.IntegerField(default=0)
    vip_customer = models.BooleanField(default=False)
    #added address before create the fisrt steps in the database
    address = models.CharField(max_length=100, blank=True)

    def as_json(self):
        return dict(
            customer_id=self.id,
            name=self.name,
            address=self.address,
            email_address=self.email_address,
            phone_number=self.phone_number,
            vip_customer=self.vip_customer)