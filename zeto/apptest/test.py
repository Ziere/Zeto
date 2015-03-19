# -*- coding: utf-8 -*-
from django.test import TestCase
from apptest.models import Customer

class AnimalTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name='Fran',
                                address='Rivera Street n. 17',
                                email_address='fran@zeto.com',
                                phone_number=655900100,
                                vip_customer=True)
        Customer.objects.create(name='Emily',
                                address='Mephisto Road flat 3, 1B',
                                email_address='emily@zeto.com',
                                phone_number=655900101,
                                vip_customer=False)

    def customer_test(self):
        fran = Customer.objects.get(name="Fran")
        emily = Customer.objects.get(name="Emily")
        self.assertEqual(fran.name, 'Fran')
        self.assertEqual(emily.name, 'Emily')
        self.assertEqual(emily.name, 'emily@zeto.com')