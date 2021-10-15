#!/usr/bin/env python

# create a JWT and sign it with a private key, creating a JWS

import sys
import pprint
from jwcrypto import jwk, jws
from jwcrypto.common import json_encode

usage = "{} private-key.pem sekrit payload.json".format(sys.argv[0])

# parse args
if len(sys.argv) < 4:
    print(usage)
    exit(1)

json_file = sys.argv[3]
private_key_file = sys.argv[1]
password = sys.argv[2].encode("utf-8")

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

jwstoken = jws.JWS(json_payload)
protected_headers = json_encode({
    "alg": "RS256",
})
optional_headers = json_encode({
    "kid": private_key.thumbprint(),
})
jwstoken.add_signature(private_key, None, protected_headers, optional_headers)

print(jwstoken.serialize())
