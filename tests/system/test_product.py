from unittest import TestCase

from mypage2 import app
import json
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), [{"price":75542.5,"productId":1,"productName":"Iphone13","rating":4.8},{"price":70000.0,"productId":2,"productName":"Iphone12","rating":4.7},{"price":"10000","productId":"132","productName":"realme","rating":"5"},{"price":"20000","productId":"1919","productName":"samsung","rating":"5"}])

