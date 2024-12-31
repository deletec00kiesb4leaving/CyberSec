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

## Finding Your IP Address

Before you can scan or work with your network, you'll need to know your current IP address. On Unix-like systems (including Linux and macOS), you can use either `ifconfig` or `iwconfig` for this purpose:

- **ifconfig**: For wired connections, open a terminal and type:
```sh
ifconfig
```

Look for your network interface (like eth0 or en0) and find the `inet addr` or `inet` field to see your IP address.

`iwconfig`: For wireless connections, you might prefer:
```sh
iwconfig
```

However, `iwconfig` mainly shows wireless settings; for the IP, you would still need to look at `ifconfig` or use `ip addr show` for more modern systems.

Both commands will display your current network configuration, including the IP address, which is crucial for understanding which private network range you're operating within.

## Scanning Private Networks with Nmap

When scanning private networks, ensure you have the necessary permissions. Scanning networks you do not own or manage can be illegal or considered intrusive. Here are `nmap` commands to scan the entire range of each private network block:

### 10.0.0.0/8

To scan the entire `10.0.0.0/8` subnet:

```sh
nmap -F 10.0.0.0/8
```

### 172.16.0.0/12

To scan the entire `172.16.0.0/12` range:

```sh
nmap -F 172.16.0.0/12
```

### 192.168.0.0/16

To scan the entire `192.168.0.0/16` subnet:

```sh
nmap -F 192.168.0.0/16
```

### 192.168.1.0/24

To scan the entire `192.168.1.0/24` subnet:

```sh
nmap -F 192.168.1.0/24
```
