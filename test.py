import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()


	def test_median1(self):

		solution = self.app.get('/median?X=1/2,89,23,24,1,2,3,4')
		self.assertEqual(b'3.5', solution.data)

	def test_median2(self):

		solution = self.app.get('/median?X=1/2,89,23,24')
		self.assertEqual(b'23.5', solution.data)



	def test_median3(self):

		solution = self.app.get('/median?X=1/2,89,23,24,12,9,0,2')
		self.assertEqual(b'10.5', solution.data)


	def test_median4(self):

		solution = self.app.get('median?X=1/2,89,23,24,9,8,7,4')
		self.assertEqual(b"8.5", solution.data)


if __name__ == '__main__':
	unittest.main()
