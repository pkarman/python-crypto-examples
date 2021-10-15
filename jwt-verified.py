#!/usr/bin/env python

# verify a signed JWT (JWS)

import sys
import pprint
from jwcrypto import jwk, jws

usage = "{} jws.json public.pem".format(sys.argv[0])

# parse args
if len(sys.argv) < 3:
    print(usage)
    exit(1)

json_file = sys.argv[1]
public_key_file = sys.argv[2]

# read the json file into a string
json_payload = ""
with open(json_file, "rb") as jf:
    json_payload = jf.read()

# same for public PEM
public_pem = ""
with open(public_key_file, "rb") as pf:
    public_pem = pf.read()

# create JWK
public_key = jwk.JWK.from_pem(public_pem)

jwstoken = jws.JWS()
jwstoken.deserialize(json_payload)
jwstoken.verify(public_key)
print(jwstoken.payload)
