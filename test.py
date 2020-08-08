import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()

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
