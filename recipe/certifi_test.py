import sys
from libcloud.security import CA_CERTS_PATH
import certifi

ok = 0 if certifi.where() in CA_CERTS_PATH else 1
sys.exit(ok)
