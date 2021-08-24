# Explorations in Python crypto

[JSON Web Encryption](https://datatracker.ietf.org/doc/html/rfc7516) experiments.

## Reading list

* [https://jwcrypto.readthedocs.io/en/latest/jwe.html](https://jwcrypto.readthedocs.io/en/latest/jwe.html)
* [https://jwcrypto.readthedocs.io/en/latest/jwk.html](https://jwcrypto.readthedocs.io/en/latest/jwk.html)
* [Layperson's guide to JWE etc](https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3)

## Generate RSA public/private PEM files

```
python gen-keys.py sekrit
```

## Verify public key matches private key

```
openssl rsa -pubout -in private.pem | diff public.pem -
```

No difference means the public key was generated from matching private key.

## Encrypt a JSON file with a public key

```
python encrypt-json-file.py my-pii.json public.pem > encrypted-pii.json
```

## Decrypt a JSON file with a private key

```
python decrypt-json-file.py encrypted-pii.json private.pem sekrit
```

## Unpack encoded attachments to files

```
python unpack-encrypted-json-file.py encrypted-pii.json private.pem sekrit
```

