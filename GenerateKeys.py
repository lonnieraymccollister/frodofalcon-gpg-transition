import pickle
import binascii

"""
This file implements tests for various parts of the Falcon.py library.

Test the code with:
> make test
"""
from common import q, sqnorm
from fft import add, sub, mul, div, neg, fft, ifft
from ntt import mul_zq, div_zq
from sampler import sampler_z
from ffsampling import ffldl, ffldl_fft, ffnp, ffnp_fft
from ffsampling import gram
from random import randint, random, gauss
from math import pi, sqrt, floor, ceil, exp
from ntrugen import karamul, ntru_gen, gs_norm
from falcon import SecretKey, PublicKey
from encoding import compress, decompress
import sys
if sys.version_info >= (3, 4):
    from importlib import reload  # Python 3.4+ only.

######################################################
sk = SecretKey(1024)
placesList = sk
with open('sk.txt', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(placesList, filehandle)

pk = PublicKey(sk)
placesList1 = pk
with open('pk.txt', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(placesList1, filehandle)
######################################################
######################################################

#with open('sk.txt', 'rb') as filehandle:
    # read the data as binary data stream
#    placesList = pickle.load(filehandle)
#sk = placesList
#f = open('test.py.sig', 'rb').read()
#m = binascii.hexlify(f).decode('utf-8')
#sig = sk.sign(m)
#placesList = sig
#with open('test.py.sig.sig', 'wb') as filehandle:
    # store the data as binary data stream
#    pickle.dump(placesList, filehandle)
#print (" Message signed ")

######################################################
######################################################
#with open('pk.txt', 'rb') as filehandle:
    # read the data as binary data stream
#    placesList = pickle.load(filehandle)
#pk = placesList
#f = open('test.py.sig', 'rb').read()
#m = binascii.hexlify(f).decode('utf-8')
#with open('test.py.sig.sig', 'rb') as filehandle:
    # read the data as binary data stream
#    placesList = pickle.load(filehandle)
#sig = placesList
#verifysig = pk.verify(m, sig)
#print ("Valid Signature: ", verifysig)

######################################################

#placesList = sig
#with open('signature.txt', 'wb') as filehandle:
    # store the data as binary data stream
#    pickle.dump(placesList, filehandle)

#with open('signature.txt', 'rb') as filehandle:
    # read the data as binary data stream
#    placesList = pickle.load(filehandle)
#signature = placesList

#print ("verifysig: ", verifysig)
#check = cryptovinaigrette.rainbowKeygen.verify('cvPub.pub', signature, 'test/testFile.txt')
#print ("Check: ", check)
#check = cryptovinaigrette.rainbowKeygen.verify('cvPub.pub', signature, 'test/testFile2.txt')
#print ("Check: ", check)