# Private IP Address Ranges (RFC 1918)

RFC 1918 defines the following IP address ranges for use in private networks:

- **10.0.0.0 - 10.255.255.255** (`10.0.0.0/8`)
  - **Total Addresses**: 16,777,216
  - **Use**: Large networks, enterprise environments.

- **172.16.0.0 - 172.31.255.255** (`172.16.0.0/12`)
  - **Total Addresses**: 1,048,576
  - **Use**: Medium-sized networks, often used in business settings.

- **192.168.0.0 - 192.168.255.255** (`192.168.0.0/16`)
  - **Total Addresses**: 65,536
  - **Use**: Small networks, home networks, and small office/home office (SOHO) environments.

## Scanning Private Networks with Nmap

When scanning private networks, ensure you have the necessary permissions. Scanning networks you do not own or manage can be illegal or considered intrusive. Here are `nmap` commands to scan the entire range of each private network block:

### 10.0.0.0/8

To scan the entire `10.0.0.0/8` subnet:

```sh
nmap -F 10.0.0.0/8
```

