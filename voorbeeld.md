# CN Les 13 – Labo Cheat Sheet
## Static Routing + SVI + DHCP (IPv4)

---

## Topologie

```
PC1 ──── SW1 ──── R1 ──── R2 ──── SW2 ──── PC2
```

| Segment     | Netwerk            | Device  | Interface | IP-adres        |
|-------------|--------------------|---------|-----------|-----------------|
| LAN 1       | 192.168.1.0/24     | R1      | G0/0/0    | 192.168.1.1     |
| LAN 1       | 192.168.1.0/24     | SW1     | VLAN 1    | 192.168.1.2     |
| LAN 1       | 192.168.1.0/24     | PC1     | NIC       | DHCP            |
| WAN         | 10.0.0.0/30        | R1      | G0/0/1    | 10.0.0.1        |
| WAN         | 10.0.0.0/30        | R2      | G0/0/1    | 10.0.0.2        |
| LAN 2       | 192.168.2.0/24     | R2      | G0/0/0    | 192.168.2.1     |
| LAN 2       | 192.168.2.0/24     | SW2     | VLAN 1    | 192.168.2.2     |
| LAN 2       | 192.168.2.0/24     | PC2     | NIC       | DHCP            |

---

## Router 1 (R1)

1. `Router> enable`
2. `Router# conf t`
3. `Router(config)# hostname R1`

### Interface G0/0/0 (naar SW1 / LAN1)

4. `R1(config)# interface G0/0/0`
5. `R1(config-if)# ip address 192.168.1.1 255.255.255.0`
6. `R1(config-if)# no shutdown`

### Interface G0/0/1 (WAN naar R2)

7. `R1(config-if)# interface G0/0/1`
8. `R1(config-if)# ip address 10.0.0.1 255.255.255.252`
9. `R1(config-if)# no shutdown`

### Static route naar LAN2

10. `R1(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2`

### DHCP voor LAN1

11. `R1(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10`
12. `R1(config)# ip dhcp pool LAN1`
13. `R1(dhcp-config)# network 192.168.1.0 255.255.255.0`
14. `R1(dhcp-config)# default-router 192.168.1.1`
15. `R1(dhcp-config)# exit`

### Opslaan

16. `R1(config)# exit`
17. `R1# wr`

---

## Router 2 (R2)

1. `Router> enable`
2. `Router# conf t`
3. `Router(config)# hostname R2`

### Interface G0/0/0 (naar SW2 / LAN2)

4. `R2(config)# interface G0/0/0`
5. `R2(config-if)# ip address 192.168.2.1 255.255.255.0`
6. `R2(config-if)# no shutdown`

### Interface G0/0/1 (WAN naar R1)

7. `R2(config-if)# interface G0/0/1`
8. `R2(config-if)# ip address 10.0.0.2 255.255.255.252`
9. `R2(config-if)# no shutdown`

### Static route naar LAN1

10. `R2(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1`

### DHCP voor LAN2

11. `R2(config)# ip dhcp excluded-address 192.168.2.1 192.168.2.10`
12. `R2(config)# ip dhcp pool LAN2`
13. `R2(dhcp-config)# network 192.168.2.0 255.255.255.0`
14. `R2(dhcp-config)# default-router 192.168.2.1`
15. `R2(dhcp-config)# exit`

### Opslaan

16. `R2(config)# exit`
17. `R2# wr`

---

## Switch 1 (SW1)

1. `Switch> enable`
2. `Switch# conf t`
3. `Switch(config)# hostname SW1`

### SVI (management-IP)

4. `SW1(config)# interface vlan 1`
5. `SW1(config-if)# ip address 192.168.1.2 255.255.255.0`
6. `SW1(config-if)# no shutdown`
7. `SW1(config-if)# exit`

### Default gateway (om SW1 bereikbaar te maken van andere netten)

8. `SW1(config)# ip default-gateway 192.168.1.1`

### Opslaan

9. `SW1(config)# exit`
10. `SW1# wr`

---

## Switch 2 (SW2)

1. `Switch> enable`
2. `Switch# conf t`
3. `Switch(config)# hostname SW2`

### SVI (management-IP)

4. `SW2(config)# interface vlan 1`
5. `SW2(config-if)# ip address 192.168.2.2 255.255.255.0`
6. `SW2(config-if)# no shutdown`
7. `SW2(config-if)# exit`

### Default gateway

8. `SW2(config)# ip default-gateway 192.168.2.1`

### Opslaan

9. `SW2(config)# exit`
10. `SW2# wr`

---

## Testen / Foutopsporing

### Stap-voor-stap testplan

| Stap | Test                                          | Commando (op device)                          |
|------|-----------------------------------------------|-----------------------------------------------|
| 1    | Interfaces actief op R1?                      | `show ip interface brief`                     |
| 2    | Interfaces actief op R2?                      | `show ip interface brief`                     |
| 3    | Ping R1 → R2 (WAN-link)                       | `ping 10.0.0.2`                               |
| 4    | Ping R1 → SW1 (SVI)                           | `ping 192.168.1.2`                            |
| 5    | Ping R2 → SW2 (SVI)                           | `ping 192.168.2.2`                            |
| 6    | PC1 krijgt IP via DHCP?                       | `ipconfig` (Windows) of `ip a` (Linux)        |
| 7    | Ping PC1 → R1                                 | `ping 192.168.1.1`                            |
| 8    | Ping PC1 → R2 (via static route)             | `ping 192.168.2.1`                            |
| 9    | Ping PC1 → PC2 (end-to-end)                  | `ping 192.168.2.x`                            |
| 10   | Routetabel controleren                        | `show ip route`                               |
| 11   | DHCP-leases bekijken                          | `show ip dhcp binding`                        |
| 12   | SSH naar SW1 vanaf PC1 (optioneel)            | `ssh -l admin 192.168.1.2`                    |

---

## Algemeen

- Opslaan: `wr` of `copy running-config startup-config`
- Resetten: `write erase` → `reload`
- Interfaces tonen: `show ip interface brief`
- Routetabel: `show ip route`
- Alle poorten: `show interfaces`
- DHCP bindings: `show ip dhcp binding`
- Hostnaam instellen: `hostname NAAM`