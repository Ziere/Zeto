from django.db import models

# Create your models here.


class Customer(models.Model):
    email_address = models.CharField(max_length=45)
    phone_number = models.IntegerField(default=0)
    vip_customer = models.BooleanField(default=False)

    def as_json(self):
        return dict(
            customer_id=self.id,
            email_address=self.email_address,
            phone_number=self.phone_number,
            vip_customer=self.vip_customer)