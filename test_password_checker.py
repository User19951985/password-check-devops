
import unittest
# import re
from password_checker import is_valid_password

class  TestMath(unittest.TestCase):

  __password = "12345Uhe?"


  # def validate_password(self,password: str):
  #   pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
  #   return bool(re.match(pattern, password))

  def test_blackbox(self):
    validate = is_valid_password(self.__password)
    self.assertTrue(validate)

  def test_too_short_password(self):
    password1 = "asuh29"
    password2 = "ASFOIAS"
    password3 = "sss34"
    
    validate1 = is_valid_password(password1)
    validate2 = is_valid_password(password2)
    validate3 = is_valid_password(password3)

    self.assertFalse(validate1)
    self.assertFalse(validate2)
    self.assertFalse(validate3)