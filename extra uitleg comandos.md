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
- oplossing: trunk configureren (zie hieronder)

---

# Trunk

## Wat is een trunk?
- een trunk is een verbinding tussen 2 switches (of switch en router) die verkeer van meerdere VLANs tegelijk doorlaat
- access poort = 1 VLAN, trunk poort = meerdere VLANs
- trunk voegt een VLAN-tag toe aan elk frame (802.1Q) zodat de andere switch weet bij welk VLAN het hoort

## ```switchport mode trunk```
- zet de poort in trunk mode
- de poort laat nu verkeer van alle VLANs door

## ```switchport trunk native vlan 99```
- stelt het native VLAN in op 99
- native VLAN = verkeer dat ZONDER tag verstuurd wordt
- standaard is dit VLAN 1, maar dat is onveilig (VLAN hopping attack)
- het native VLAN moet aan beide kanten van de trunk hetzelfde zijn!

## ```switchport trunk allowed vlan 10,20,99```
- beperkt welke VLANs over de trunk mogen
- standaard zijn alle VLANs toegestaan
- best practice: alleen de VLANs toelaten die je nodig hebt

## ```show interfaces trunk```
- toont alle trunk poorten, welke VLANs erop mogen, en het native VLAN
- handig om te troubleshooten

---

# Inter-VLAN routing (router-on-a-stick)

## Wat is inter-VLAN routing?
- VLANs kunnen standaard NIET met elkaar communiceren
- je hebt een router nodig om verkeer tussen VLANs te routeren
- router-on-a-stick = 1 fysieke kabel van router naar switch, maar met subinterfaces gesplitst per VLAN
- de switch-poort naar de router moet een **trunk** zijn (anders komt alleen VLAN 1 door)

## Hoe werkt het?
- de router maakt **subinterfaces** aan op 1 fysieke poort (bv G0/0/0)
- elke subinterface krijgt een VLAN-nummer en een IP-adres
- dat IP-adres wordt de **default gateway** voor dat VLAN
- de switch stuurt getagd verkeer (802.1Q) naar de router, de router routeert het naar het juiste VLAN

## ```interface g0/0/0.10```
- maakt subinterface `.10` aan op G0/0/0
- het nummer (10) is vrij te kiezen, maar best = VLAN-nummer (voor duidelijkheid)
- je moet ook de fysieke interface (`g0/0/0`) apart activeren met `no shutdown`

## ```encapsulation dot1Q 10```
- koppelt de subinterface aan VLAN 10
- dot1Q = het 802.1Q trunk protocol (voegt VLAN-tag toe aan frames)
- dit commando is VERPLICHT op elke subinterface

## ```ip address 10.0.10.1 255.255.255.0```
- geeft de subinterface een IP-adres
- dit adres wordt de **default gateway** voor alle PC's in VLAN 10
- elk VLAN heeft zijn eigen subnet nodig

## Voorbeeld samengevat
```
Router: G0/0/0.10 → encapsulation dot1Q 10 → ip 10.0.10.1/24 (gateway VLAN 10)
Router: G0/0/0.20 → encapsulation dot1Q 20 → ip 10.0.20.1/24 (gateway VLAN 20)
Router: G0/0/0    → no shutdown (fysieke poort activeren!)

Switch: G0/1      → switchport mode trunk (naar router)
Switch: F0/1      → switchport access vlan 10 (naar PC)
Switch: F0/9      → switchport access vlan 20 (naar PC)
```

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

---

# Access List (ACL)

## Wat is een ACL?
- een ACL filtert verkeer op een router interface
- je bepaalt welk verkeer door mag (permit) of geblokkeerd wordt (deny)
- standard ACL = filtert alleen op source IP
- extended ACL = filtert op source IP, destination IP, protocol, poort
- er is altijd een onzichtbare laatste regel: **deny any** (alles wat niet matcht wordt gedropt)

## ```ip access-list standard <naam>```
- maakt een named standard ACL aan
- standard = filtert alleen op bron-adres
- `<naam>` = vrij te kiezen naam (bv BLOCK-LAN)

## ```permit 192.168.10.0 0.0.0.255```
- laat al het verkeer toe van het netwerk 192.168.10.0/24
- 0.0.0.255 = wildcard mask (omgekeerde van subnetmask)
- wildcard berekening: 255.255.255.255 - 255.255.255.0 = 0.0.0.255

## ```show access-lists```
- toont alle ACLs en hun regels
- toont ook het regelnummer (10, 20, 30...) en het aantal matches

## ```interface g0/0/0```
- selecteert de interface waarop je de ACL wilt toepassen
- standard ACL → plaats zo dicht mogelijk bij de **bestemming**

## ```ip access-group <naam> out```
- past de ACL toe op de interface
- `out` = filtert verkeer dat de interface UIT gaat
- `in` = filtert verkeer dat de interface IN komt
- per interface max 1 ACL per richting (in/out)

## Andere regels (extended ACL)

### ```permit icmp 172.22.34.96 0.0.0.15 host 172.22.34.62```
- laat ICMP (ping) toe van 172.22.34.96/28 naar host 172.22.34.62
- 0.0.0.15 = wildcard voor /28 (16 adressen)

### ```permit tcp 172.22.34.96 0.0.0.15 host 172.22.34.62 eq www```
- laat TCP verkeer toe naar poort 80 (www)
- eq www = equal to port 80
- alleen webverkeer wordt toegelaten

### ```deny udp any 10.0.0.0 0.0.0.255 lt 1000```
- blokkeer UDP verkeer van overal naar 10.0.0.0/24
- lt 1000 = less than port 1000 (poorten 0-999)
- any = elk bronadres
