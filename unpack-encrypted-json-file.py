#!/usr/bin/env python

import sys
import pprint
import hashlib
import mimetypes
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode, base64url_decode

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

# show top-level keys fyi
encrypted_payload = json_decode(json_payload)
for key in encrypted_payload.keys():
    print("encrypted key: {}".format(key))

# same for private PEM
private_pem = ""
with open(private_key_file, "rb") as pf:
    private_pem = pf.read()

# create JWK
private_key = jwk.JWK.from_pem(private_pem, password)
jwetoken = jwe.JWE()
jwetoken.deserialize(json_payload, key=private_key)

payload = json_decode(jwetoken.payload.decode("utf-8"))

# the special key "attachments" is used to store base64-encoded files

for key, value in payload.items():
    if key == "attachments":
        for attached in value:
            uuid = attached["id"]
            mime = attached["mime"]
            description = attached["description"]
            base64_encoded_file = attached["file"]
            file_extension = mimetypes.guess_extension(mime)
            sha = hashlib.sha256(base64_encoded_file.encode("utf-8")).hexdigest()
            filename = f"{sha}{file_extension}"
            with open(filename, "wb") as fh:
                fh.write(base64url_decode(base64_encoded_file))
            print("wrote {} '{}' to {}".format(uuid, description, filename))
    else:
        print("{} => {}".format(key, pprint.pformat(value)))

