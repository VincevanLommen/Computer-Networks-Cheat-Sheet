

# 🔵 **R1 – LINKER NETWERK (SLAAC‑ONLY)**

## **G0/0/1 – SLAAC‑only + DNS via RA**
```
interface GigabitEthernet0/0/1
 ipv6 address 2001:acad::1/64
 ipv6 nd prefix 2001:acad::/64
 ipv6 nd ra dns server 2606:4700:4700::1111
 no shutdown
```

## **G0/0/0 – Link naar R2 (LLA only)**
```
interface GigabitEthernet0/0/0
 ipv6 address fe80::1 link-local
 no shutdown
```

## **Statische IPv6 route naar rechter LAN**
```
ipv6 route 2003:cafe::/64 fe80::2 GigabitEthernet0/0/0
```

---

# 🟢 **R2 – RECHTER NETWERK (SLAAC + STATELESS DHCPv6)**

## **G0/0/1 – SLAAC + Stateless DHCPv6**
```
interface GigabitEthernet0/0/1
 ipv6 address 2003:cafe::1/64
 ipv6 nd prefix 2003:cafe::/64
 ipv6 nd other-config-flag
 ipv6 dhcp server DHCPv6-CAFE
 no shutdown
```

## **Stateless DHCPv6 pool**
```
ipv6 dhcp pool DHCPv6-CAFE
 dns-server 2606:4700:4700::1111
 domain-name lab.local
```

## **G0/0/0 – Link naar R1 (LLA only)**
```
interface GigabitEthernet0/0/0
 ipv6 address fe80::2 link-local
 no shutdown
```

## **Statische IPv6 route naar linker LAN**
```
ipv6 route 2001:acad::/64 fe80::1 GigabitEthernet0/0/0
```

---

# 🖥️ **PC0 – SLAAC‑only**
```
ipv6 autoconfig
```

# 🖥️ **PC1 – SLAAC + Stateless DHCPv6**
```
ipv6 autoconfig
```

---
+


ipv6 unicast-routing