# Extra uitleg comandos

# ipv4

## ```ip address 192.168.0.1 255.255.255.0```
- 192.168.0.1 = het IP dat je aan de interface geeft
- 255.255.255.0 = subnetmask, /24 → 254 hosts in dit netwerk
- het netwerk is dan 192.168.0.0/24 (alles van .0 tot .255)

## ```ip route 0.0.0.0 0.0.0.0 10.10.10.2```
- 0.0.0.0 0.0.0.0 = default route (alles wat ik niet ken)
- 10.10.10.2 = next hop, het IP van de volgende router
- dus: "stuur alles wat je niet kent naar 10.10.10.2"

## ```ip dhcp excluded-address 192.168.0.1```
- dit adres NIET uitdelen via DHCP
- typisch het adres van de router zelf

## ```ip dhcp pool LAN```
- maakt een DHCP pool aan met naam "LAN"
- daarna stel je het netwerk, gateway en dns in

## ```default-router 192.168.0.1```
- de default gateway die DHCP-clients krijgen
- = het IP van de router interface in dat LAN

## ```dns-server 8.8.8.8```
- de DNS server die clients krijgen
- 8.8.8.8 = Google DNS

## ```ip default-gateway 192.168.1.1```
- alleen op switches
- zodat de switch zelf bereikbaar is vanuit andere netwerken
- = het IP van de router in hetzelfde VLAN

---

# VLANs

## Wat is een VLAN?
- een VLAN splitst 1 fysieke switch op in meerdere logische netwerken
- PC's in VLAN 10 kunnen NIET praten met PC's in VLAN 20 (zonder router)
- handig om groepen te scheiden (bv studenten vs personeel)

## ```vlan 10```
- maakt VLAN 10 aan op de switch
- je komt dan in config-vlan mode

## ```name Faculty/Staff```
- geeft het VLAN een naam
- puur voor leesbaarheid, maakt technisch niks uit
- namen zijn case-sensitive!

## ```switchport mode access```
- zet de poort in access mode
- = deze poort hoort bij 1 VLAN
- access = voor eindapparaten (PC, printer)

## ```switchport access vlan 10```
- koppelt de poort aan VLAN 10
- al het verkeer op die poort zit nu in VLAN 10

## ```switchport voice vlan 150```
- speciaal voor IP telefoons
- de telefoon gebruikt VLAN 150 voor spraak
- de PC achter de telefoon gebruikt het access VLAN (bv 10)
- 1 poort, 2 VLANs (data + voice)

## ```mls qos trust cos```
- vertrouwt de QoS markering van de telefoon
- zorgt dat spraakverkeer prioriteit krijgt

## ```show vlan brief```
- toont alle VLANs + welke poorten erbij horen
- handig om te checken of alles goed staat

## Waarom kunnen PC's in hetzelfde VLAN op verschillende switches niet pingen?
- de trunk link (tussen switches) staat nog op VLAN 1
- verkeer van VLAN 10/20/30 wordt niet doorgestuurd
- oplossing: trunk configureren (zie trunk sectie)

---

# ipv6

## Soorten adressen

| Type | Voorbeeld | Wat het is |
|------|-----------|------------|
| Global Unicast (GUA) | 2001:DB8:1::1/64 | publiek routeerbaar, zoals een publiek IPv4 adres |
| Link-Local (LLA) | fe80::1 | alleen geldig op de directe link, niet routeerbaar |
| Prefix | 2001:DB8:1::/64 | het netwerk-deel (eerste 64 bits) |

## ```ipv6 address 2001:DB8:1::1/64```
- geeft de interface een Global Unicast Address
- 2001:DB8:1:: = het netwerk (prefix)
- ::1 = het host-deel (de "1" aan het einde)
- /64 = prefix lengte, altijd 64 bij IPv6 LAN

## ```ipv6 unicast-routing```
- ZET IPv6 ROUTING AAN op de router
- zonder dit forwardt de router GEEN IPv6 pakketten
- vergeet dit niet!! moet op elke router

## ```ipv6 address fe80::1 link-local```
- zet een link-local adres op de interface
- fe80:: = altijd link-local
- wordt gebruikt als next-hop bij static routes tussen routers
- niet routeerbaar, alleen op die ene link

## ```ipv6 nd prefix 2001:DB8:1::/64```
- nd = Neighbor Discovery
- zegt aan de PC's: "gebruik dit prefix voor SLAAC"
- PC maakt zelf een IPv6 adres aan met dit prefix + zijn eigen MAC

## ```ipv6 nd ra dns server 2606:4700:4700::1111```
- ra = Router Advertisement
- stuurt de DNS server mee in de RA berichten
- 2606:4700:4700::1111 = Cloudflare DNS
- PC's krijgen zo automatisch een DNS server via SLAAC

## ```ipv6 nd other-config-flag```
- zet de O-flag aan in Router Advertisements
- zegt tegen PC's: "haal extra info (dns, domain) op via DHCPv6"
- het IP adres komt nog steeds via SLAAC
- alleen de extra info (dns, domain-name) komt via DHCPv6
- dit is "stateless" DHCPv6

## ```ipv6 dhcp server POOLNAAM```
- koppelt een DHCPv6 pool aan de interface
- POOLNAAM = de naam van de pool die je aanmaakt

## ```ipv6 dhcp pool POOLNAAM```
- maakt de DHCPv6 pool aan
- hierin zet je dns-server en domain-name

## ```dns-server 2606:4700:4700::1111```
- de IPv6 DNS server die clients krijgen via DHCPv6

## ```domain-name lab.local```
- de domain suffix die clients krijgen
- bv als je "ping server1" typt, zoekt hij "server1.lab.local"

## ```ipv6 route 2001:DB8:2::/64 fe80::2 G0/0/0```
- statische route naar een ander IPv6 netwerk
- 2001:DB8:2::/64 = het netwerk waar je naartoe wilt
- fe80::2 = next hop (link-local van de andere router)
- G0/0/0 = via welke interface (verplicht bij link-local next hop)

---

# Wanneer gebruik je wat?

## SLAAC-only
- PC maakt zelf een IP aan
- router stuurt prefix + DNS via RA
- geen DHCPv6 nodig
- commando's: ```ipv6 nd prefix``` + ```ipv6 nd ra dns server```

## SLAAC + Stateless DHCPv6
- PC maakt zelf een IP aan (via SLAAC)
- extra info (dns, domain) via DHCPv6
- commando's: ```ipv6 nd other-config-flag``` + ```ipv6 dhcp server``` + ```ipv6 dhcp pool```

## PC-kant
- beide gevallen: ```ipv6 autoconfig``` (in Packet Tracer)
- Windows: ```ipconfig /release6``` en ```ipconfig /renew6``` om te vernieuwen
