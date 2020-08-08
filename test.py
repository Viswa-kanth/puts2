import unittest
import main


class TestCalculator(unittest.TestCase):
	
	def setUp(self):
		main.app.testing = True
		self.app = main.app.test_client()


	def test_max1(self):

		solution = self.app.get('/max?X=1,2,5,0,100')
		self.assertEqual(b'3.5 \n', solution.data)

if __name__ == '__main__':
	unittest.main()
