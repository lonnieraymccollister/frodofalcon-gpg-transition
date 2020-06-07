# falcon.py

This is a private repository implementing the signature scheme Falcon (https://falcon-sign.info/).
Falcon stands for **FA**st Fourier **L**attice-based **CO**mpact signatures over **N**TRU

## Content

This repository contains the following files (in order of dependency):
1. **generate_constants.sage** contains the code which was used to generate the constants used in this project
1. **common.py** contains shared functions and constants
1. **fft_constants.py** contains precomputed constants used in the FFT
1. **ntt_constants.py** contains precomputed constants used in the NTT
1. **fft.py** contains a stand-alone implementation of the FFT over R[x] / (x<sup>n</sup> + 1)
1. **ntt.py** contains a stand-alone implementation of the NTT over Z<sub>q</sub>[x] / (x<sup>n</sup> + 1)
1. **ntrugen.py** generate polynomials f,g,F,G in Z[x] / (x<sup>n</sup> + 1) such that f G - g F = q
1. **sampler.py** implements a Gaussian sampler over the integers
1. **ffsampling.py** implements the fast Fourier sampling algorithm
1. **falcon.py** implements Falcon
1. **test.py** implements tests to check that everything is properly implemented


## How to use

1. Generate a secret key **sk = SecretKey(n)**
1. Generate the corresponding public key **pk = PublicKey(sk)**
1. Now we can sign messages:
   - To plainly sign a message m: **sig = sk.sign(m)**
   - To sign a message m with a pre-chosen 320-bit integer salt: **sig = sk.sign(m, salt)**
1. We can also verify signatures: **pk.verify(m, sig)**

## Todo

- [ ] Compress and decompress
- [ ] Document all the docstrings


## Author

* **Thomas Prest** (thomas.prest@ens.fr)

## Disclaimer

This is work in progress. It is not to be considered suitable for production.
It can, to some extent, be considered reference code, but the "true" reference code of Falcon is on https://falcon-sign.info/.

If you find errors or flaw, I will be very happy if you report them to me at the provided address.

## License

MIT


***
***
***
Lonnie Ray McCollister
***
https://github.com/lonnieraymccollister/frodofalcon-gpg-transition/
***
===>>**First secure data with GPG4win and put in the message folder**<<===
 *** command syntax will look like *** 
 *** (qmail.py) keyname_message_to filename.gpg keyname_message_from *** 
***
wikipedia |--->> NTRU was developed in 1996 for lattice-based public-key cryptography (IEEE P1363.1) and in April 2011, NTRUEncrypt was accepted as a X9.98 Standard for use in the financial services industry. The NIST has initiated a quantum-secure cryptographic standardization process and hopes to publish the standardization documents by 2024.  This may become a FIPS or NIST Special Publication.  GPG is a free-software replacement for Symantec's PGP and compliant with RFC 4880. GPG uses a public key infrastructure (PKI)(RSA and ECC are not Quantum resistant.) that vouches for the identities assigned to specific private keys and vulnerabilities are patched or corrected. <<---| FrodoKEM-1344-SHAKE settings worked well using Anaconda3/gpg4win/gpg in the python3 folder of the repository on windows 10 and ubuntu 20.04 lts.  I  added files(qmail.py/pyemail.bat/pyemail.py/pyemailub.py) and python/windows files with 2 directories to get the gpg drop-in. To run - go to the the python3 directory in the cmd prompt and run either the pyton(qmail.py/pyemail.bat/pyemail.py/pyemailub.py) version. Tutorial(https://youtu.be/cjCJUd3PW1w) (The cmd menu differs slightly in the tutorial for frodo and for qmail.py you need to place the files in the message directory.) - goto https://youtu.be/vxfNoEAakcY -- I am very pleased with what the Mirosoft - LWEKE team and Thomas Prest team have done.  I recomend using the standard gpg implimentation first to secure your data. qmail.py should work with (windows/ubuntu/MacOs). Use python pip to install the cryptography module for frodo and any other modules needed.  In qmail.py the menue items(5,6) were added so that you could increase security(512 bit key) by independently encrypting the xor message and key.  for video tutorials - goto https://youtu.be/TiwkzWs0vgM and https://youtu.be/FotW07rVDTI  
*** 
***
***

