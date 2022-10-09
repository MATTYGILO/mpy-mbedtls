import x509

_cert = b"""-----BEGIN CERTIFICATE-----
MIIBqzCCAVGgAwIBAgIUBn0u9MXrKG+sQpCpRsAthZDyzHMwCgYIKoZIzj0EAwIw
MjEMMAoGA1UEBAwDRm9vMRQwEgYDVQQKDAtNaWNyb1B5dGhvbjEMMAoGA1UEAwwD
QmFyMB4XDTIyMTAwOTAxMDcwNFoXDTI3MTAwODAxMDcwNFowOjEQMA4GA1UEBAwH
VXNlckZvbzEUMBIGA1UECgwLTWljcm9QeXRob24xEDAOBgNVBAMMB1VzZXJCYXIw
WTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATTRlY2gnBiMtx59GgYnAITzUK3ZsvE
/8Bp1glf4ahyCSs6iie2aNMlNtSdJj8uyesrJQ45OtECfc9fZAAK/oq3oz0wOzA5
BgNVHREEMjAwghZ3c3M6Ly8xOTIuMTY4LjEuMTo4ODMzghZ3c3M6Ly8xOTIuMTY4
LjQuMTo4ODMzMAoGCCqGSM49BAMCA0gAMEUCIHDrlzUodNKRQg8doC0ZyUOMBJ8Q
8KtooqjD6u//t/eZAiEAkEWSiBwcWOwpOxNHLj0yOi4oGgtFzgxBSgqk8OQVxl0=
-----END CERTIFICATE-----"""


cert = x509.parse_cert(_cert)

print(cert)

print("CERT: OK")

