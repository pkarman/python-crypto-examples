#!/usr/bin/env python

import sys
import pprint
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode

usage = "{} encrypted-file.json private.pem sekrit".format(sys.argv[0])

# parse args
if len(sys.argv) < 4:
    print(usage)
    exit(1)

json_file = sys.argv[1]
private_key_file = sys.argv[2]
password = sys.argv[3].encode("utf-8")

# read the json file into a string
json_payload = ""
with open(json_file, "rb") as jf:
    json_payload = jf.read()

# same for private PEM
private_pem = ""
with open(private_key_file, "rb") as pf:
    private_pem = pf.read()

# create JWK
private_key = jwk.JWK.from_pem(private_pem, password)
jwetoken = jwe.JWE()
jwetoken.deserialize(json_payload, key=private_key)

print(jwetoken.payload.decode("utf-8"))
