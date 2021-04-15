from dhke import DHKE

if __name__ == "__main__":
  dh = DHKE()
  print("\nUsing generator:\n%d" % (dh.g))
  print("\nPrime number p:\n%d" % (dh.p))
  print("\nPublic key g^a mod p:\n%d" % (dh.pub_key))
  ext_pub_key = int(input("\nPlease input external public key g^b mod p:\n"))
  dh.calculate_private_key(ext_pub_key)
  print("\nFinal Private Key g^(a*b) mod p is:\n%d" % (dh.private_key))