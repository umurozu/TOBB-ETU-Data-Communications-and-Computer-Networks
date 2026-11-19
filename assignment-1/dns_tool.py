import sys
import socket
import time
from dnslib import DNSRecord, DNSQuestion, QTYPE

domain = sys.argv[1]
record_type = sys.argv[2].upper()

# 4 tane parametre varsa sonuncu dns server yap yoksa default
if len(sys.argv) >= 4:
    dns_server = sys.argv[3]
else:
    dns_server = "8.8.8.8"

question = DNSQuestion(domain, getattr(QTYPE, record_type))
query = DNSRecord(q=question)
data = query.pack()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

start_time = time.time()

sock.sendto(data, (dns_server, 53))
response_data, _ = sock.recvfrom(4096)

end_time = time.time()

response = DNSRecord.parse(response_data)

print("Domain:", domain)
print("Record Type:", record_type)
print("---------------------------")

for rr in response.rr:
    print("Value:", rr.rdata)
    print("TTL:", rr.ttl)
    print("---------------------------")

# ms donusturucu
query_time_ms = (end_time - start_time) * 1000
print("Query time:", round(query_time_ms, 2), "ms")

sock.close()
