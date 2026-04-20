# Voorbeeldexamen Raf

## Opgave

Configure with 3 VLAN's, inter-VLAN-routing, make sure all PC's can ping each other and can ping all servers

- **VLAN10:** `10.0.10.0/24` ; name STUDENT
- **VLAN20:** `10.0.20.0/24` ; name TEACHER
- **VLAN30:** `10.0.30.0/24` ; name ADMIN

- DHCP for PCs on R1
- DHCP no addresses `.0` to `.10`
- Default gateways for VLAN's are the `.1` host addresses
- Check which connection is a trunk
- Only allow the 3 defined VLAN's on the TRUNK

---

## Opstelling

```
Server 0 --- Router 0 --- Router 1 --- Router 2 --- Server 1
                              |
                           Switch 0
                              |
                        PC0, PC1, PC2
```

| Device | Interface | Adres |
|--------|-----------|-------|
| Server 0 | - | `192.168.0.14/30` |
| Server 1 | - | `192.168.0.10/30` |
| R0 | G0/0/0 | `192.168.0.5/30` |
| R0 | G0/0/1 | `192.168.0.13/30` |
| R1 | G0/0/0.10 | `10.0.10.1/24` |
| R1 | G0/0/0.20 | `10.0.20.1/24` |
| R1 | G0/0/0.30 | `10.0.30.1/24` |
| R1 | G0/0/1 | `192.168.0.6/30` |
| R1 | G0/0/2 | `192.168.0.1/30` |
| R2 | G0/0/0 | `192.168.0.2/30` |
| R2 | G0/0/1 | `192.168.0.9/30` |

| S0 poort | VLAN |
|----------|------|
| G0/1 | Trunk |
| F0/1 | VLAN 10 (STUDENT) |
| F0/9 | VLAN 20 (TEACHER) |
| F0/17 | VLAN 30 (ADMIN) |

---

## Configuratie

### Server 0

- IP address: `192.168.0.14`
- Subnet mask: `255.255.255.252`
- Default gateway: `192.168.0.13`

### Server 1

- IP address: `192.168.0.10`
- Subnet mask: `255.255.255.252`
- Default gateway: `192.168.0.9`

---

### R0

1. Router>```enable```
2. Router#```conf t```

#### Interface G0/0/0

3. R0(config)#```interface g0/0/0```
4. R0(config-if)#```ip address 192.168.0.5 255.255.255.252```
5. R0(config-if)#```no shutdown```

#### Interface G0/0/1

6. R0(config)#```interface g0/0/1```
7. R0(config-if)#```ip address 192.168.0.13 255.255.255.252```
8. R0(config-if)#```no shutdown```

#### Default route

9. R0(config)#```ip route 0.0.0.0 0.0.0.0 192.168.0.6```

---

### R1

1. Router>```enable```
2. Router#```conf t```

#### Subinterfaces (inter-VLAN routing)

3. R1(config)#```interface g0/0/0.10```
4. R1(config-subif)#```encapsulation dot1Q 10```
5. R1(config-subif)#```ip address 10.0.10.1 255.255.255.0```

6. R1(config)#```interface g0/0/0.20```
7. R1(config-subif)#```encapsulation dot1Q 20```
8. R1(config-subif)#```ip address 10.0.20.1 255.255.255.0```

9. R1(config)#```interface g0/0/0.30```
10. R1(config-subif)#```encapsulation dot1Q 30```
11. R1(config-subif)#```ip address 10.0.30.1 255.255.255.0```

#### Interface G0/0/0 activeren

12. R1(config)#```interface g0/0/0```
13. R1(config-if)#```no shutdown```

#### Interface G0/0/1

14. R1(config)#```interface g0/0/1```
15. R1(config-if)#```ip address 192.168.0.6 255.255.255.252```
16. R1(config-if)#```no shutdown```

#### Interface G0/0/2

17. R1(config)#```interface g0/0/2```
18. R1(config-if)#```ip address 192.168.0.1 255.255.255.252```
19. R1(config-if)#```no shutdown```

#### Static routes

20. R1(config)#```ip route 192.168.0.8 255.255.255.252 192.168.0.2```
21. R1(config)#```ip route 192.168.0.12 255.255.255.252 192.168.0.5```

#### DHCP

22. R1(config)#```ip dhcp excluded-address 10.0.10.0 10.0.10.10```
23. R1(config)#```ip dhcp excluded-address 10.0.20.0 10.0.20.10```
24. R1(config)#```ip dhcp excluded-address 10.0.30.0 10.0.30.10```

25. R1(config)#```ip dhcp pool VLAN10```
26. R1(dhcp-config)#```network 10.0.10.0 255.255.255.0```
27. R1(dhcp-config)#```default-router 10.0.10.1```

28. R1(config)#```ip dhcp pool VLAN20```
29. R1(dhcp-config)#```network 10.0.20.0 255.255.255.0```
30. R1(dhcp-config)#```default-router 10.0.20.1```

31. R1(config)#```ip dhcp pool VLAN30```
32. R1(dhcp-config)#```network 10.0.30.0 255.255.255.0```
33. R1(dhcp-config)#```default-router 10.0.30.1```

---

### R2

1. Router>```enable```
2. Router#```conf t```

#### Interface G0/0/0

3. R2(config)#```interface g0/0/0```
4. R2(config-if)#```ip address 192.168.0.2 255.255.255.252```
5. R2(config-if)#```no shutdown```

#### Interface G0/0/1

6. R2(config)#```interface g0/0/1```
7. R2(config-if)#```ip address 192.168.0.9 255.255.255.252```
8. R2(config-if)#```no shutdown```

#### Default route

9. R2(config)#```ip route 0.0.0.0 0.0.0.0 192.168.0.1```

---

### S0

1. Switch>```enable```
2. Switch#```conf t```

#### VLANs aanmaken

3. S0(config)#```vlan 10```
4. S0(config-vlan)#```name STUDENT```
5. S0(config-vlan)#```vlan 20```
6. S0(config-vlan)#```name TEACHER```
7. S0(config-vlan)#```vlan 30```
8. S0(config-vlan)#```name ADMIN```

#### Trunk configureren

9. S0(config)#```interface g0/1```
10. S0(config-if)#```switchport mode trunk```
11. S0(config-if)#```switchport trunk allowed vlan 10,20,30```

#### Poorten toewijzen aan VLANs

12. S0(config)#```interface f0/1```
13. S0(config-if)#```switchport mode access```
14. S0(config-if)#```switchport access vlan 10```

15. S0(config)#```interface f0/9```
16. S0(config-if)#```switchport mode access```
17. S0(config-if)#```switchport access vlan 20```

18. S0(config)#```interface f0/17```
19. S0(config-if)#```switchport mode access```
20. S0(config-if)#```switchport access vlan 30```
