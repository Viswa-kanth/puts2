import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_median1(self):

		solution = self.app.get('/median?X=1,4,5')
		self.assertEqual(b'4.6', solution.data)

	def test_median2(self):

		solution = self.app.get('/median?X=0.5,12.23,0.23.100,1,3,12')
		self.assertEqual(b'21.878888888888888', solution.data)

	def test_median3(self):

		solution = self.app.get('/median?X=22.222,98,4,2,1,5,6,77,99,89')
		self.assertEqual(b'40.3222', solution.data)

	def test_median4(self):

		solution = self.app.get('/median?X=1/2,89,23,24')
		self.assertEqual(b'44.75', solution.data)

	def test_median5(self):

		solution = self.app.get('/median?X=30,5/2')
		self.assertEqual(b'16.25', solution.data)

	def test_median6(self):

		solution = self.app.get('/median?X=0,22,23,4,6,2')
		self.assertEqual(b'9.571428571428571', solution.data)

	def test_median7(self):

		solution = self.app.get('/median?X=22,23,24,26,27,28,100')
		self.assertEqual(b'34.375', solution.data)

	def test_median8(self):

		solution = self.app.get('median?X=1,2,5,0,100')
		self.assertEqual(b"49.5", solution.data) 

	def test_median9(self):

		solution = self.app.get('median?X=10,2,1,2,3,4,5,6,7,2,1,1,123')
		self.assertEqual(b"11.6875", solution.data)

if __name__ == '__main__':
	unittest.main()
