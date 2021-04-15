from Crypto.Util import number
from Crypto.Random import random

NUMBER_BIT_SIZE = 512

class DHKE:

  def __init__(self, g=5, p=None):
    self.g = g
    if p:
      self.p = p
    else:
      self.p = self.random_large_prime()
    self.a = self.random_lage_number()
    self.pub_key = self.mod_exp(self.g, self.a, self.p)
    self.ext_pub_key = None
    self.private_key = None

  def calculate_private_key(self, ext_pub_key):
    self.ext_pub_key = ext_pub_key
    self.private_key = self.mod_exp(ext_pub_key, self.a, self.p)

  def random_large_prime(self):
    return number.getPrime(NUMBER_BIT_SIZE)

  def random_lage_number(self):
    return random.getrandbits(NUMBER_BIT_SIZE)

  def mod_exp( self, x, y, N ):
    if y == 0: #base case
      return 1
    z = self.mod_exp( x, y // 2, N ) # recursive call
    if ( y % 2 ) == 0: # y is even case
      return pow( z, 2 ) % N
    else: # y is odd case
      return ( x * pow( z, 2 )) % N

