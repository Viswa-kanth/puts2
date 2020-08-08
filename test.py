import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

	def test_average1(self):

		solution = self.app.get('/average?X=1,4,5,6,7')
		self.assertEqual(b'4.6', solution.data)

	def test_average2(self):

		solution = self.app.get('/average?X=0.5,12.23,0.08,22,123,23.100,1,3,12')
		self.assertEqual(b'21.878888888888888', solution.data)

	def test_mean1(self):

		solution = self.app.get('/mean?X=22.222,98,4,2,1,5,6,77,99,89')
		self.assertEqual(b'40.3222', solution.data)

	def test_mean2(self):

		solution = self.app.get('/mean?X=1/2,89')
		self.assertEqual(b'44.75', solution.data)

	def test_mean3(self):

		solution = self.app.get('/mean?X=30,5/2')
		self.assertEqual(b'16.25', solution.data)

	def test_avg1(self):

		solution = self.app.get('/avg?X=0,22,23,10,4,6,2')
		self.assertEqual(b'9.571428571428571', solution.data)

	def test_avg2(self):

		solution = self.app.get('/avg?X=22,23,24,25,26,27,28,100')
		self.assertEqual(b'34.375', solution.data)

	def test_avg3(self):

		solution = self.app.get('avg?X=1,98')
		self.assertEqual(b"49.5", solution.data) 

	def test_avg4(self):

		solution = self.app.get('avg?X=10,2,1,2,3,4,5,6,7,8,9,3,2,1,1,123')
		self.assertEqual(b"11.6875", solution.data)


if __name__ == '__main__':
	unittest.main()
