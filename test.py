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

	def test_median1(self):

		solution = self.app.get('/median?X=22.222,98,4,2,1,5,6,77,99,89')
		self.assertEqual(b'14.111', solution.data)

	def test_median2(self):

		solution = self.app.get('/median?X=1/2,89')
		self.assertEqual(b'44.75', solution.data)

	def test_median3(self):

		solution = self.app.get('/median?X=30,5/2')
		self.assertEqual(b'16.25', solution.data)

	def test_median4(self):

		solution = self.app.get('/median?X=22,23,24,25,26,27,28,100')
		self.assertEqual(b'25.5', solution.data)

	def test_median5(self):

		solution = self.app.get('median?X=1,98')
		self.assertEqual(b"49.5", solution.data) 

	def test_median6(self):

		solution = self.app.get('median?X=10,2,1,2,3,4,5,6,7,8,9,3,2,1,1,123')
		self.assertEqual(b"3.5", solution.data)

	def test_min1(self):

		solution = self.app.get('/min?X=0,-1,-12,23,44,2,22,23')
		self.assertEqual(b'-12', solution.data)

	def test_min2(self):

		solution = self.app.get('/min?X=1/2,-89,-233,4,2,1,23,4,999')
		self.assertEqual(b'-233', solution.data)

	def test_min3(self):

		solution = self.app.get('/min?X=30,5/2')
		self.assertEqual(b'2.0', solution.data)

	def test_min4(self):

		solution = self.app.get('/min?X=22,23,24,25,26,27,28,100')
		self.assertEqual(b'22', solution.data)

	def test_min5(self):

		solution = self.app.get('min?X=1,98,1,2,-3,4,5,6,7')
		self.assertEqual(b"-3", solution.data) 

	def test_min6(self):

		solution = self.app.get('min?X=-1000,2,1,2,3,4,5,6,7,8,9,3,2,1,1,1238999')
		self.assertEqual(b"-1000", solution.data)

if __name__ == '__main__':
	unittest.main()
