* Max poort nr is 16 bits. Ongeveer 64.000
* Router is op laag 3, dus ip
* /32 host route
* Eerst gebeurt altijd de DNS‑controle, pas daarna kan er een HTTP‑GET verstuurd worden. 
* Fe:80 is link local
* 2000 global unicast
# Subnetten berekenen

## Voorbeeld

Hoeveel subnetten kan je maken van het 172.16.0.0/16 als je /21 subnet gebruikt?

### /16

| 8 bits | 8 bits | 8 bits | 8 bits |
|--------|--------|--------|--------|
| Netwerk | Netwerk | Host | Host |
| ← 16 bits netwerk → | | ← 16 bits host → | |

### /21

| 8 bits | 8 bits | 5 bits | 3 bits | 8 bits |
|--------|--------|--------|--------|--------|
| Netwerk | Netwerk | Netwerk | Host | Host |
| ← 21 bits netwerk → | | | ← 11 bits host → | |

### Berekening

- Verschil: 21 - 16 = **5 bits**
- Van `00000` tot `11111`
- Aantal subnetten: 2^5 = **32 mogelijke subnetten**

# Netwerkadres berekenen

- Netwerkadres eindigt altijd op 0 (host-bits worden 0)

## Voorbeeld

Hostadres: `10.5.19.67/23` → 32 - 23 = **9 host-bits**

| 8 bits | 8 bits | 7 bits | 1 bit | 8 bits |
|--------|--------|--------|-------|--------|
| 10 | 5 | Netwerk | Host | Host |
| Netwerk | Netwerk | ← 23 bits → | ← 9 bits host → | |

**Stap 1:** 3e octet (19) bepaalt de grens → `19` in binair = `0001001`**`1`**

**Stap 2:** Laatste bit zit in het host-deel → wordt 0 → `00010010` = **18**

**Stap 3:** 4e octet (67) zit volledig in host-deel → wordt **0**

**Resultaat:** Netwerkadres = `10.5.18.0/23`


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

* Met dad checken als zijn IPv6 adress uniek is



- broadcast storm, lus van nutteloze broadcast pakketjes
- bridge is een oud woord voor switch
- met vlans apparte stp conf




• VLAN attacks
• countermeasure = disable DTP


• STP attacks
• countermeasure = enable BPDUguard



# LACP
* Link aggregatie → 2 kabels laten samenwerken