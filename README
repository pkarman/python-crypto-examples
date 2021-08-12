# Explorations in Python crypto

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
