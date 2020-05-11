# Creative Commons Zero v1.0 Universal
# SPDX-License-Identifier: CC0-1.0
# Created by Douglas Stebila
import pickle
from frodokem import FrodoKEM

class NISTKAT(object):
    
    def run(kem):
        with open('sk.txt', 'rb') as filehandle:
        # read the data as binary data stream
	        sk = pickle.load(filehandle)
        with open('ct.txt', 'rb') as filehandle:
        # read the data as binary data stream
	        ct = pickle.load(filehandle)
        ss_d = kem.kem_decaps(sk, ct)
        print("ss =", ss_d.hex().upper())

if __name__ == "__main__":
    # Run KATs for all supported FrodoKEM variants
    NISTKAT.run(FrodoKEM('FrodoKEM-1344-SHAKE'))
