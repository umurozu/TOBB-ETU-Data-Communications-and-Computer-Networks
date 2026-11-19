# TOBB ETU – Data Communications and Computer Networks (BIL452)

Assignments for the BIL452 Data Communications and Computer Networks course at TOBB University of Economics and Technology.

## Contents

### assignment-1
- **`dns_tool.py`**: A command-line DNS query tool. It builds the DNS query with `dnslib`, sends it over a raw UDP socket to port 53 and prints each record's value and TTL along with the query time in ms.
- **`MehmetUmur_OZU_211401025_wireshark_assignment_report.pdf`**: A Wireshark packet analysis report. It examines HTTP GET/response exchanges and HTML documents with embedded objects, and covers HTTP versions and headers, status codes, the TCP handshake, RTT and sequence/acknowledgment numbers.
- **`AI_Usage.txt`**: Statement on how AI tools were used in this assignment.

### assignment-2
- **`MehmetUmurOZU_Assignment2.pkt`**: Cisco Packet Tracer project file.
- **`MehmetUmuOZU_BIL452_AssignmentReport.pdf`**: A network design report for a multi-site enterprise network (headquarters and two branches), built in Cisco Packet Tracer:
  - hub-and-spoke WAN with /30 point-to-point links
  - VLAN segmentation (employees, servers, VoIP), 802.1Q trunks, router-on-a-stick inter-VLAN routing
  - OSPF (area 0) dynamic routing and hierarchical IPv4 addressing
  - DHCP (with option 150 for IP phones), DNS, web, e-mail and file servers
  - VoIP with Cisco CME

## Usage (DNS tool)

```bash
pip install dnslib
python assignment-1/dns_tool.py <domain> <record_type> [dns_server]
# example
python assignment-1/dns_tool.py example.com A 1.1.1.1
```

If `dns_server` is not given, the tool uses `8.8.8.8`.
