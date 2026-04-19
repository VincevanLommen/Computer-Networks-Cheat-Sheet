# Cisco cheat sheet 

# ipv4

## Router
1. Router>```enable```

2. Router#```conf term```

### Interface G0/0/0

3. Router(config)#```interface G0/0/0```

4. Router(config-if)#```ip address 192.168.0.1 255.255.255.0```

5. Router(config-if)#```no shutdown```

### Interface G0/0/1

6. Router(config-if)#```interface G0/0/1```

7. Router(config-if)#```ip address 10.10.10.1 255.255.255.0```
   
8. Router(config-if)#```no shutdown```

### Next hop

1. Router(config)#```ip route 0.0.0.0 0.0.0.0 10.10.10.2```

### DHCP

1. R1(config)#```ip dhcp excluded-address 192.168.0.1```
2. R1(config)#```ip dhcp pool LAN```
3. R1(dhcp-config)#```network 192.168.0.0 255.255.255.0```
4. R1(dhcp-config)#```default-router 192.168.0.1```
5. R1(dhcp-config)#```dns-server 8.8.8.8```


## Switch
1. Switch>```enable```

2. Switch#```conf term```

3. Switch(config)#```interface vlan 1```

4. Switch(config-if)#```ip address 192.168.1.67 255.255.255.0```

5. Switch(config-if)#```no shutdown```

### Default gateway

6. Switch(config)#```ip default-gateway 192.168.1.1```

### VLANs aanmaken

1. Switch(config)#```vlan 10```
2. Switch(config-vlan)#```name Faculty/Staff```
3. Switch(config-vlan)#```vlan 20```
4. Switch(config-vlan)#```name Students```
5. Switch(config-vlan)#```vlan 99```
6. Switch(config-vlan)#```name Management```

### Poort toewijzen aan VLAN

1. Switch(config)#```interface f0/11```
2. Switch(config-if)#```switchport mode access```
3. Switch(config-if)#```switchport access vlan 10```

### Voice VLAN

1. Switch(config)#```interface f0/11```
2. Switch(config-if)#```mls qos trust cos```
3. Switch(config-if)#```switchport voice vlan 150```

### VLANs bekijken

- ```show vlan brief```


# ipv6

## Router (IPv6)

1. Router> `enable`  
2. Router# `conf t`  

### Interface G0/0/0
3. Router(config)# `interface g0/0/0`  
4. Router(config-if)# `ipv6 address 2001:DB8:1::1/64`  
5. Router(config-if)# `no shutdown`  

### Interface G0/0/1
6. Router(config)# `interface g0/0/1`  
7. Router(config-if)# `ipv6 address 2001:DB8:2::1/64`  
8. Router(config-if)# `no shutdown`  

### IPv6 routing activeren
9. Router(config)# `ipv6 unicast-routing`  

### Link-local adres
10. Router(config-if)# `ipv6 address fe80::1 link-local`  

### SLAAC (prefix + DNS via RA)
11. Router(config-if)# `ipv6 nd prefix 2001:DB8:1::/64`  
12. Router(config-if)# `ipv6 nd ra dns server 2606:4700:4700::1111`  

### Stateless DHCPv6 op interface
13. Router(config-if)# `ipv6 nd other-config-flag`  
14. Router(config-if)# `ipv6 dhcp server POOLNAAM`  

### DHCPv6 pool
15. Router(config)# `ipv6 dhcp pool POOLNAAM`  
16. Router(config-dhcpv6)# `dns-server 2606:4700:4700::1111`  
17. Router(config-dhcpv6)# `domain-name lab.local`  

### Statische IPv6 route
18. Router(config)# `ipv6 route 2001:DB8:2::/64 fe80::2 G0/0/0`  


## Switch (IPv6)

1. Switch> `enable`  
2. Switch# `configure terminal`  
3. Switch(config)# `interface vlan 1`  
4. Switch(config-if)# `ipv6 address 2001:DB8:1::67/64`  
5. Switch(config-if)# `no shutdown`  

# Algemeen
- Router opslaan: ```wr``` of ```copy running-config startup-config```
- Router resetten: ```write erase```
- Router herstarten: ```reload```
- IPv4‑interfaces tonen: ```show ip interface brief```
- IPv6‑interfaces tonen: ```show ipv6 interface brief```
- Route table: ```show ip route```
- IPv6‑routingtabel: ```show ipv6 route```
- Alle poorten bekijken: ```show interfaces```
- Hostnaam instellen: ```hostname NAAM```
- DHCP leases bekijken: ```show ip dhcp binding```
- DHCPv6 bindings: ```show ipv6 dhcp binding```
- Running config bekijken: ```show running-config```
- VLANs bekijken: ```show vlan brief```
- Rommon recovery: ```boot```
- IPv6 vernieuwen (PC): ```ipconfig /release6``` dan ```ipconfig /renew6```