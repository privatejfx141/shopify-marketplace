from django.test import TestCase
from api.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(title="T-Shirt", price=10.00, inventory_count=5)
        Product.objects.create(title="Pants", price=15.00, inventory_count=15)
    
    def test_get_products(self):
        tshirt = Product.objects.get(title="T-Shirt")
        pants = Product.objects.get(title="Pants")
        self.assertEqual(tshirt.price, 10.00)
        self.assertEqual(tshirt.inventory_count, 5)
        self.assertEqual(pants.price, 15.00)
        self.assertEqual(pants.inventory_count, 15)
