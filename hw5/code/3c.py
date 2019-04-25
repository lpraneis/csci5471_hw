from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from binascii import hexlify
import string, random


key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
)

count = 1
while (True):
    count+= 1

    name_len = random.randrange(1, 20)
    domain_len = random.randrange(1, 20)
    name= ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(name_len))
    domain= ''.join(random.choice(string.ascii_uppercase) for x in range(domain_len))
    ext = ''.join(random.choice(string.ascii_uppercase) for x in range(3))

    email= name + '@' + domain +'.' + ext

    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME,u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Minnesota"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Minneapolis"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UMN"), 
        x509.NameAttribute(NameOID.COMMON_NAME, u"testsite.com"),
        ])).add_extension(
                x509.SubjectAlternativeName([
                    x509.RFC822Name(email)
                    ]),
                critical=False,
                ).sign(key, hashes.SHA256(), default_backend())

    digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
    digest.update(csr.public_bytes(serialization.Encoding.PEM))
    target = hexlify(digest.finalize())[-16:]

    
    csr2 = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME,u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Minnesota"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Minneapolis"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UMN"), 
        x509.NameAttribute(NameOID.COMMON_NAME, u"testsite.com"),
        ])).add_extension(
                x509.BasicConstraints(True,None),
                critical=True,
                    ).sign(key, hashes.SHA256(), default_backend())

    digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
    digest.update(csr2.public_bytes(serialization.Encoding.PEM))
    test = hexlify(digest.finalize())[-16:]
    if test == target:
        with open('collision.txt', 'r') as f:
            f.write(csr.public_bytes(serialization.Encoding.PEM))
            f.write(csr2.public_bytes(serialization.Encoding.PEM))
            f.write(email)
            f.write("Count: {}".format(count))
        print("Found with email: ", email)
        break


