import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_max1(self):

		solution = self.app.get('/max?X=1,2,77,99,89')
		self.assertEqual(b'99', solution.data)

	def test_max2(self):

		solution = self.app.get('/max?X=1/2,89,233,4,2,1,23,4,999')
		self.assertEqual(b'999', solution.data)

	def test_max3(self):

		solution = self.app.get('/max?X=30,5/2')
		self.assertEqual(b'30', solution.data)

	def test_max4(self):

		solution = self.app.get('/max?X=22,23,24,25,26,27,28,100')
		self.assertEqual(b'100', solution.data)

	def test_max5(self):

		solution = self.app.get('max?X=1,98')
		self.assertEqual(b"98", solution.data) 

	def test_max6(self):

		solution = self.app.get('max?X=10,2,1,2,3,4,5,6,7,8,9,3,2,1,1,123')
		self.assertEqual(b"123", solution.data)

if __name__ == '__main__':
	unittest.main()
