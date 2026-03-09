* Max poort nr is 16 bits. Ongeveer 64.000


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

## Lease

- Enkel request en ACK
- Bekijken via ```ipconfig /all```
  * ```Lease Obtained. . . . . . . . . . : Monday, 9 March 2026 10:06:36```
  * ```Lease Expires . . . . . . . . . . : Monday, 9 March 2026 10:36:54```