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





## Switch
1. Switch>```enable```

2. Switch#```configure```

3. Switch (config) #```interface vlan 1```

4. Switch (config-if) #```ip address 192.168.1.67 255.255.255.0```

5. Switch (config-if) #```no shutdown```


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


## Switch (IPv6)

1. Switch> `enable`  
2. Switch# `configure terminal`  
3. Switch(config)# `interface vlan 1`  
4. Switch(config-if)# `ipv6 address 2001:DB8:1::67/64`  
5. Switch(config-if)# `no shutdown`  

# Algemeen
- Router resetten: ```write erase```
- Router herstarten: ```reload```
- IPv4‑interfaces tonen: ```show ip interface brief```
- IPv6‑interfaces tonen: ```show ipv6 interface brief```
- Route table ```show ip route```
- IPv6‑routingtabel: ```show ipv6 route```
- Alle poorten bekijken: ```show interfaces```
- Hostnaam instellen: ```hostname NAAM```


