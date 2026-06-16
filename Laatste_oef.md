# Overzicht adressen

> Deze versie is aangepast zodat de adressen, DHCP-pools en subnetting logisch consistent blijven in Packet Tracer.

| Device name | Port | IP |
|-------------|------|----|
| UCLL-RTR-01 | VLAN 10 | 172.16.10.1/24 |
| UCLL-RTR-01 | VLAN 20 | 172.16.20.1/24 |
| UCLL-RTR-01 | VLAN 30 | 172.16.30.1/24 |
| UCLL-RTR-01 | VLAN 10 (IPv6) | 2001:ACAD:DB8:10::1/64 |
| UCLL-RTR-01 | VLAN 20 (IPv6) | 2001:ACAD:DB8:20::1/64 |
| UCLL-RTR-01 | VLAN 30 (IPv6) | 2001:ACAD:DB8:30::1/64 |
| UCLL-RTR-01 | Se0/0/0 | 1.1.1.2/8 |
| UCLL-RTR-01 | Se0/0/1 | 2.2.2.2/8 |
| DCNT-RTR-01 | Se0/0/0 | 1.1.1.1/8 |
| DCNT-RTR-01 | G0/0 | 10.0.1.254/24 |
| DCNT-SRV-01 | Fa0 | 10.0.1.5 (DNS + DHCP-server) |

---

# VLAN’s

In het UCLL-netwerk bestaan 3 VLAN’s:

- VLAN 10: Studenten
- VLAN 20: Lectoren
- VLAN 30: Researchers

Maak deze VLAN’s overal waar nodig aan.

Zorg dat de PC’s van de studenten in VLAN 10 geplaatst worden, de lectoren in VLAN 20 en de researchers in VLAN 30.

Configureer inter-VLAN routing via de subinterfaces van UCLL-RTR-01.

---

# DHCP

## Studenten DHCP

- Gebruik lokaal op UCLL-RTR-01 een pool **VLAN10_POOL**.
- Network: `172.16.10.0/24`
- Default gateway: `172.16.10.1`
- DNS-server: `10.0.1.5`
- IPv6: configureer stateless DHCPv6 met pool **VLAN10_POOL_IPV6**.

## Lectoren DHCP

- Gebruik lokaal op UCLL-RTR-01 een pool **VLAN20_POOL**.
- Reserveer `172.16.20.1` tot `172.16.20.10` voor statische configuraties.
- Network: `172.16.20.0/24`
- Default gateway: `172.16.20.1`
- DNS-server: `10.0.1.5`
- IPv6: gebruik SLAAC.

## Researchers DHCP

- Configureer op de router-interface voor VLAN 30 een `ip helper-address 10.0.1.5`.
- De DHCP-requests worden dan doorgestuurd naar de server in het datacenter.
- IPv6: gebruik ook SLAAC of een geschikte IPv6-configuratie op de router.

---

# OSPF

Gebruik **OSPF proces 10** op beide routers.

- UCLL-RTR-01 en DCNT-RTR-01 moeten OSPF-uitwisselingen alleen over de serial links doen.
- De LAN-interfaces moeten als `passive-interface` worden ingesteld.
- Gebruik `network` statements zodat alleen de juiste netwerken in OSPF komen.

---

# NAT

Configureer NAT op UCLL-RTR-01 zodat alle 3 LAN-netwerken internettoegang krijgen via `Se0/0/0`.

1. Maak een standaard ACL die de 3 VLAN-subnets toelaat.
2. Markeer de juiste interfaces als `inside` en `outside`.
3. Activeer PAT met `ip nat inside source list 1 interface Se0/0/0 overload`.

---

# Etherchannel

Configureer een etherchannel tussen UCLL-SW-02 en UCLL-SW-03 op poorten `fa0/23` en `fa0/24`.

- Channel ID: `1`
- Mode: `active`
- Trunk alle VLAN’s 10, 20 en 30

---

# Oplossing

## 1. Basisconfiguratie van UCLL-RTR-01

```text
Router> enable
Router# configure terminal
Router(config)# ip routing
Router(config)# ipv6 unicast-routing
```

## 2. Subinterfaces voor inter-VLAN routing

```text
Router(config)# interface g0/0/0
Router(config-if)# no shutdown

Router(config)# interface g0/0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 172.16.10.1 255.255.255.0
Router(config-subif)# ipv6 address 2001:ACAD:DB8:10::1/64
Router(config-subif)# ipv6 nd prefix 2001:ACAD:DB8:10::/64
Router(config-subif)# ipv6 nd other-config-flag
Router(config-subif)# ipv6 dhcp server VLAN10_POOL_IPV6
Router(config-subif)# no shutdown

Router(config)# interface g0/0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 172.16.20.1 255.255.255.0
Router(config-subif)# ipv6 address 2001:ACAD:DB8:20::1/64
Router(config-subif)# ipv6 nd prefix 2001:ACAD:DB8:20::/64
Router(config-subif)# no shutdown

Router(config)# interface g0/0/0.30
Router(config-subif)# encapsulation dot1Q 30
Router(config-subif)# ip address 172.16.30.1 255.255.255.0
Router(config-subif)# ipv6 address 2001:ACAD:DB8:30::1/64
Router(config-subif)# ipv6 nd prefix 2001:ACAD:DB8:30::/64
Router(config-subif)# ip helper-address 10.0.1.5
Router(config-subif)# no shutdown
```

## 3. Serial interfaces

```text
Router(config)# interface se0/0/0
Router(config-if)# ip address 1.1.1.2 255.0.0.0
Router(config-if)# no shutdown

Router(config)# interface se0/0/1
Router(config-if)# ip address 2.2.2.2 255.0.0.0
Router(config-if)# no shutdown
```

## 4. DHCP op UCLL-RTR-01

```text
Router(config)# ip dhcp excluded-address 172.16.10.1
Router(config)# ip dhcp pool VLAN10_POOL
Router(dhcp-config)# network 172.16.10.0 255.255.255.0
Router(dhcp-config)# default-router 172.16.10.1
Router(dhcp-config)# dns-server 10.0.1.5

Router(config)# ip dhcp excluded-address 172.16.20.1 172.16.20.10
Router(config)# ip dhcp pool VLAN20_POOL
Router(dhcp-config)# network 172.16.20.0 255.255.255.0
Router(dhcp-config)# default-router 172.16.20.1
Router(dhcp-config)# dns-server 10.0.1.5

Router(config)# ipv6 dhcp pool VLAN10_POOL_IPV6
Router(config-dhcpv6)# dns-server 2001:4860:4860::8888
Router(config-dhcpv6)# domain-name lab.local
```

## 5. OSPF configureren

```text
Router(config)# router ospf 10
Router(config-router)# router-id 2.2.2.2
Router(config-router)# network 1.0.0.0 0.255.255.255 area 0
Router(config-router)# network 2.0.0.0 0.255.255.255 area 0
Router(config-router)# passive-interface g0/0/0.10
Router(config-router)# passive-interface g0/0/0.20
Router(config-router)# passive-interface g0/0/0.30
```

## 6. NAT configureren

```text
Router(config)# access-list 1 permit 172.16.10.0 0.0.0.255
Router(config)# access-list 1 permit 172.16.20.0 0.0.0.255
Router(config)# access-list 1 permit 172.16.30.0 0.0.0.255

Router(config)# interface g0/0/0.10
Router(config-subif)# ip nat inside

Router(config)# interface g0/0/0.20
Router(config-subif)# ip nat inside

Router(config)# interface g0/0/0.30
Router(config-subif)# ip nat inside

Router(config)# interface se0/0/0
Router(config-if)# ip nat outside

Router(config)# ip nat inside source list 1 interface se0/0/0 overload
```

## 7. DCNT-RTR-01

```text
Router> enable
Router# configure terminal
Router(config)# interface se0/0/0
Router(config-if)# ip address 1.1.1.1 255.0.0.0
Router(config-if)# no shutdown

Router(config)# interface g0/0
Router(config-if)# ip address 10.0.1.254 255.255.255.0
Router(config-if)# no shutdown

Router(config)# router ospf 10
Router(config-router)# router-id 1.1.1.1
Router(config-router)# network 1.0.0.0 0.255.255.255 area 0
Router(config-router)# network 10.0.1.0 0.0.0.255 area 0
Router(config-router)# passive-interface g0/0
```

## 8. Switches en Etherchannel

```text
Switch(config)# vlan 10
Switch(config-vlan)# name Studenten
Switch(config)# vlan 20
Switch(config-vlan)# name Lectoren
Switch(config)# vlan 30
Switch(config-vlan)# name Researchers

Switch(config)# interface range fa0/23 - 24
Switch(config-if-range)# switchport mode trunk
Switch(config-if-range)# channel-group 1 mode active

Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

## 9. Access-poorten per VLAN

```text
Switch(config)# interface f0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

Switch(config)# interface f0/2
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20

Switch(config)# interface f0/3
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 30
```

## 10. Extra controle

Gebruik deze checks om te zien of alles werkt:

- `show ip interface brief`
- `show ip route`
- `show ip ospf neighbor`
- `show ip nat translations`
- `show ip dhcp binding`
- `show ipv6 interface brief`
