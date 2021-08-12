#!/usr/bin/env python

import sys
import pprint
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode

usage = "{} file.json public.pem".format(sys.argv[0])

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
protected_header = {
    "alg": "RSA-OAEP-256",
    "enc": "A256GCM",
    "typ": "JWE",
    "kid": public_key.thumbprint(),
}
jwetoken = jwe.JWE(json_payload,
                   recipient=public_key,
                   protected=protected_header)
enc = jwetoken.serialize()

print(enc)
