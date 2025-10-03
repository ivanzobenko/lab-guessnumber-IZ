from lab_guessnumber import main
import unittest

class TestGuessN(unittest.TestCase):
    
     def test1(self):
          self.assertEqual(main(7, 1, 10), (7, 4))
     
     def test2(self):
          self.assertEqual(main(57, 50, 100), (57, 6))

     def test3(self):
          self.assertEqual(main(100, 1, 10), 'Number is out of range')

     def test4(self):
          self.assertEqual(main(7, 1, 10, var='slow'), (7, 7))

     def test5(self):
          self.assertEqual(main(56, 50, 100, var='slow'), (56, 7))
     
     def test6(self):
          self.assertEqual(main(10, 50, 100, var='slow'), 'Number is out of range')

     def test7(self):
          self.assertEqual(main('lol', 1, 10), 'Enter a number')

     def test8(self):
          self.assertEqual(main('lol', 1, 10, 'slow'), 'Enter a number')

     

if __name__ == '__main__':
     unittest.main()