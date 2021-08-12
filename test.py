#!/usr/bin/env python

# https://jwcrypto.readthedocs.io/en/latest/jwe.html

import pprint

from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode
key = jwk.JWK.generate(kty='oct', size=256)
payload = {
  "firstname": "some",
  "lastname": "one",
  "ssn": 666001234,
  "dob": "2000-02-03",
}
payload_encoded = json_encode(payload)
jwetoken = jwe.JWE(payload_encoded,
                   json_encode({"alg": "A256KW",
                                "enc": "A256GCM"}))
jwetoken.add_recipient(key)
enc = jwetoken.serialize()

print("key={} jwe={} enc={}".format(key, pprint.pformat(json_decode(enc)), enc))

jwetoken = jwe.JWE()
jwetoken.deserialize(enc)
jwetoken.decrypt(key)
payload_out = jwetoken.payload

print("payload={} payload_out={}".format(payload, payload_out))

public_key = jwk.JWK()
private_key = jwk.JWK.generate(kty='RSA', size=4096)
private_attrs = json_decode(private_key.export_public())
public_key.import_key(**private_attrs)

print("private key attrs {}".format(pprint.pformat(private_attrs)))

protected_header = {
    "alg": "RSA-OAEP-256",
    "enc": "A256GCM",
    "typ": "JWE",
    "kid": public_key.thumbprint(),
}
jwetoken = jwe.JWE(payload_encoded,
                   recipient=public_key,
                   protected=protected_header)
enc = jwetoken.serialize()

print("asym\npublic={}\nprivate={}\nenc={}".format(pprint.pformat(json_decode(public_key.export())), pprint.pformat(json_decode(private_key.export())), pprint.pformat(json_decode(enc))))

jwetoken = jwe.JWE()
jwetoken.deserialize(enc, key=private_key)

print("asym decoded={}".format(json_decode(jwetoken.payload)))
