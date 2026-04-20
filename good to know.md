* Max poort nr is 16 bits. Ongeveer 64.000
* Router is op laag 3, dus ip
* /32 host route
  
  
# IPv4 Autoconfig

- Draait op applicatielaag
- Gebruikt broadcast (255.255.255.255)

## Wat het instelt

- IPv4‑adres → inclusief subnetmask of prefix  
- DNS‑server  
- Default gateway  
- Domain suffix  

## 4 DHCPv4‑messages (DORA)

- Discover 
- Offer 
- Request
- ACK (Acknowledge)

## DNS Snooping

- in DHCP pakketjes kijken

## Lease

- Enkel request en ACK
- Bekijken via ```ipconfig /all```
  * ```Lease Obtained. . . . . . . . . . : Monday, 9 March 2026 10:06:36```
  * ```Lease Expires . . . . . . . . . . : Monday, 9 March 2026 10:36:54```

# IPv6

* SLAAC(-only)
* SLAAC + statless DHCPv6
* statefull DHCPv6

# protocollen

* SLAAC
* DHCPv6
* ICMPv6 → NDP
* RA/RS
* A vlag → stateless

* MEt dad checken als zijn IPv6 adress uniek is



- broadcast storm, lus van nutteloze broadcast pakketjes
- bridge is een oud woord voor switch
- met vlans apparte stp conf




• VLAN attacks
• countermeasure = disable DTP


• STP attacks
• countermeasure = enable BPDUguard



# LACP
* Link aggregatie → 2 kabels laten samenwerken