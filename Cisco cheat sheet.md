# Cisco cheat sheet 

## Router
1. Router>```enable```

2. Router#```conf term```

3. Router(config)#```interface G0/0/0```

4. Router(config-if)#```ip address 192.168.1.1 255.255.255.0```

5. Router(config-if)#```no shutdown```

6. Router(config-if)#```interface G0/0/1```

7. Router(config-if)#```ip address 10.10.10.1 255.255.255.0```
   
8. Router(config-if)#```no shutdown```


## Switch
1. Switch>```enable```

2. Switch#```configure```

3. Switch (config) #```interface vlan 1```

4. Switch (config-if) #```ip address 192.168.1.67 255.255.255.0```

5. Switch (config-if) #```no shutdown```

## Algemeen

* Resetten door ```reload```



# TEST ipv6 (Nog niet getest in labo)

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

## Algemeen

- Resetten door `reload`  
- IPv6‑adres tonen: `show ipv6 interface brief`  
- Routing tabel: `show ipv6 route`  
