#!/usr/bin/env python

from jwcrypto import jwk
from jwcrypto.common import json_decode
import sys

if len(sys.argv) < 2:
    print("usage: python gen-ec-keys.py secret")
    exit(1)

if len(sys.argv[1]) < 4:
    print("secret must be at least 4 characters")
    exit(1)

private_key_pw = sys.argv[1].encode("utf-8")

public_key = jwk.JWK()
private_key = jwk.JWK.generate(kty="EC", crv="P-256")
private_attrs = json_decode(private_key.export_public())
public_key.import_key(**private_attrs)

public_f = open("ec-public.pem", "w")
public_f.write(public_key.export_to_pem().decode("utf-8"))
public_f.close()

private_f = open("ec-private.pem", "w")
private_f.write(private_key.export_to_pem(True, private_key_pw).decode("utf-8"))
private_f.close()
