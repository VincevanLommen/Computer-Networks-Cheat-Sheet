# Examenvragen Netwerken — Studiegids met Antwoorden

**Gegenereerd voor:** Vince van Lommen  
**Vak:** Computer Networks (B-UCLL-MBI08h) — 6 studiepunten  
**DLR's:** DLR 2, DLR 3, DLR 4

---

# DLR 2 — Datacommunicatie & Lagenmodellen

---

## Vraag 1

**Doelstelling:** De student kan de verschillende aspecten van datacommunicatie binnen een lagenmodel situeren.

**Vraag:** Beschrijf de drie hoofdaspecten van datacommunicatie (bron, kanaal, bestemming) en situeer deze binnen het lagenmodel. Geef voor elk aspect een voorbeeld uit het TCP/IP-model.

**Antwoord:**

Datacommunicatie bestaat uit drie hoofdaspecten:

1. **Bron (Source):** De zender die data genereert en verstuurt. In het TCP/IP-model werkt de bron op de **Application-laag** (bijv. een webbrowser die een HTTP-verzoek stuurt) en de **Transport-laag** (TCP segmenteert de data).

2. **Kanaal (Channel/Medium):** Het transmissiemedium waarover data reist. In TCP/IP komt dit overeen met de **Network Access-laag** (Ethernet-frames, Wi-Fi), die de fysieke transmissie over kabels of draadloze verbindingen verzorgt.

3. **Bestemming (Destination):** De ontvanger die de data verwerkt. Net als de bron werkt de bestemming op alle lagen: de **Network-laag** (IP-adressering zorgt dat pakketten aankomen), de **Transport-laag** (TCP herordent en bevestigt segmenten), en de **Application-laag** (de server verwerkt het verzoek).

**Samenvatting binnen TCP/IP:**

| Aspect | TCP/IP Laag | Voorbeeld |
|---|---|---|
| Bron | Application + Transport | Browser stuurt HTTP via TCP |
| Kanaal | Network Access | Ethernet-frame over kabel |
| Bestemming | Network + Transport + Application | Webserver ontvangt en verwerkt |

---

## Vraag 2

**Doelstelling:** De student kan in detail uitleggen hoe netwerken functioneren aan de hand van een lagenmodel.

**Vraag:** Verklaar hoe data door de verschillende lagen van een lagenmodel gaat. Illustreer dit met een concreet voorbeeld van het verzenden van een e-mail van computer A naar computer B.

**Antwoord:**

Data beweegt door lagen via **encapsulatie** (bij verzenden) en **decapsulatie** (bij ontvangen). Elke laag voegt eigen header-informatie toe.

**Voorbeeld: e-mail van computer A naar B**

**Verzenden (computer A) — encapsulatie:**

1. **Application-laag:** De e-mailclient maakt een SMTP-bericht aan.
2. **Transport-laag:** TCP voegt een header toe met poortnummers (poort 25 voor SMTP) en segmentnummers → **segment**.
3. **Network-laag (Internet):** IP voegt bron- en doeladres toe → **pakket**.
4. **Network Access-laag:** Ethernet voegt MAC-adressen toe en codeert de bits → **frame** → verstuurd als elektrische signalen over de kabel.

**Ontvangen (computer B) — decapsulatie:**

4. Ethernet-frame binnenkomt → controleert MAC-adres → haalt Ethernet-header eraf.
3. IP-pakket → controleert IP-adres → haalt IP-header eraf.
2. TCP-segment → herordent segmenten, bevestigt ontvangst → haalt TCP-header eraf.
1. SMTP-data → e-mailclient toont het bericht.

---

## Vraag 3

**Doelstelling:** De student kan in detail uitleggen wat het nut is van protocollen in een lagenmodel.

**Vraag:** Waarom zijn protocollen essentieel in een lagenmodel? Verklaar het doel van protocollen op minstens twee verschillende lagen.

**Antwoord:**

Protocollen zijn **afgesproken regels** die bepalen hoe communicatie verloopt. Ze zorgen voor interoperabiliteit: apparaten van verschillende fabrikanten kunnen communiceren omdat ze dezelfde regels volgen. Zonder protocollen zou elke implementatie incompatibel zijn.

**Transport-laag — TCP (Transmission Control Protocol):**
- Regelt betrouwbare datatransmissie via three-way handshake, bevestigingen (ACK's), en hertransmissie bij verlies.
- Zorgt voor flow control en congestion control.
- Zonder TCP zou er geen garantie zijn dat data volledig en in de juiste volgorde aankomt.

**Network-laag — IP (Internet Protocol):**
- Regelt logische adressering (IP-adressen) en routering van pakketten van bron naar bestemming, ook over meerdere netwerken heen.
- Bepaalt de beste route via routeringstabellen.
- Zonder IP zouden pakketten niet weten waar ze naartoe moeten.

**Conclusie:** Protocollen per laag zorgen voor **modulariteit**: elke laag kan onafhankelijk worden bijgewerkt zonder de andere lagen te breken.

---

## Vraag 4

**Doelstelling:** De student kan in detail uitleggen hoe netwerken functioneren aan de hand van het OSI-referentiemodel én het TCP/IP-model.

**Vraag:** Teken en beschrijf beide modellen (OSI en TCP/IP). Welke zijn de overeenkomsten en verschillen?

**Antwoord:**

**OSI-model (7 lagen):**

```
7 - Application       → Gebruikersinterface (HTTP, FTP, SMTP)
6 - Presentation      → Data-opmaak, encryptie, compressie
5 - Session           → Sessiebeheer, synchronisatie
4 - Transport         → Betrouwbare/onbetrouwbare transmissie (TCP/UDP)
3 - Network           → Routering, logische adressering (IP)
2 - Data Link         → Framing, MAC-adressering, foutdetectie
1 - Physical          → Bits over medium (kabels, signalen)
```

**TCP/IP-model (4 lagen):**

```
4 - Application       → OSI lagen 5, 6, 7 gecombineerd
3 - Transport         → OSI laag 4 (TCP, UDP)
2 - Internet          → OSI laag 3 (IP, ICMP)
1 - Network Access    → OSI lagen 1 en 2 gecombineerd
```

**Overeenkomsten:**
- Beide zijn gelaagde modellen met encapsulatie/decapsulatie.
- Beide scheiden de verantwoordelijkheden van netwerkcommunicatie.
- Transport- en Network-lagen (Internet) zijn bijna identiek.

**Verschillen:**

| | OSI | TCP/IP |
|---|---|---|
| Aantal lagen | 7 | 4 |
| Gebruik | Referentiemodel (theoretisch) | Praktisch implementatiemodel |
| Application | 3 aparte lagen (5, 6, 7) | 1 gecombineerde laag |
| Physical + Data Link | Aparte lagen | Gecombineerd in Network Access |
| Ontwikkeld door | ISO | DoD (US Defensie) |

---

## Vraag 5

**Doelstelling:** De student kan de verschillende lagen van het OSI- en TCP/IP-model en hun functie uitleggen en onderling vergelijken.

**Vraag:** Voor elk van de 7 OSI-lagen en de 4 TCP/IP-lagen: zeg de naam, geef de functie en noem minstens 2 protocollen. Vergelijk de TCP/IP Application-laag met OSI-lagen 5, 6 en 7.

**Antwoord:**

**OSI-lagen:**

| Laag | Naam | Functie | Protocollen |
|---|---|---|---|
| 7 | Application | Gebruikersinterface, netwerkapplicaties | HTTP, FTP, SMTP, DNS |
| 6 | Presentation | Data-opmaak, encryptie, compressie | SSL/TLS, JPEG, ASCII |
| 5 | Session | Sessiebeheer, openen/sluiten sessies | NetBIOS, RPC |
| 4 | Transport | Betrouwbare overdracht, segmentatie | TCP, UDP |
| 3 | Network | Routering, logische adressering | IP, ICMP, OSPF |
| 2 | Data Link | Framing, MAC-adressering, foutdetectie | Ethernet, Wi-Fi (802.11) |
| 1 | Physical | Bits over transmissiemedium | USB, Bluetooth, DSL |

**TCP/IP-lagen:**

| Laag | Naam | Functie | Protocollen |
|---|---|---|---|
| 4 | Application | Applicatiecommunicatie, gebruikersinterface | HTTP, DNS, DHCP, FTP |
| 3 | Transport | Segmentatie, betrouwbaarheid | TCP, UDP |
| 2 | Internet | Routering, IP-adressering | IP, ICMP, ARP |
| 1 | Network Access | Fysieke transmissie, MAC | Ethernet, Wi-Fi |

**Vergelijking TCP/IP Application vs. OSI 5, 6, 7:**

- **OSI Laag 7 (Application):** Definieert protocollen voor applicaties (HTTP, FTP).
- **OSI Laag 6 (Presentation):** Regelt data-opmaak en encryptie (SSL/TLS zit hier in het OSI-model).
- **OSI Laag 5 (Session):** Beheert sessies en verbindingen.
- **TCP/IP Application:** Combineert alle drie. In de praktijk regelt SSL/TLS encryptie en HTTP sessies — het onderscheid tussen de drie OSI-lagen bestaat niet expliciet in TCP/IP.

---

## Vraag 6

**Doelstelling:** De student kan het doel van iedere laag in een netwerk-referentiemodel uitleggen.

**Vraag:** Leg uit waarom netwerken in lagen zijn ingedeeld. Wat zou er gebeuren als we geen lagenmodel hadden? Beschrijf het doel van minstens drie verschillende lagen.

**Antwoord:**

**Waarom lagen?**

Lagen bieden **modulariteit, abstractie en interoperabiliteit**. Elke laag heeft een duidelijke verantwoordelijkheid en communiceert alleen met de lagen direct boven en onder zich via gedefinieerde interfaces.

**Zonder lagenmodel:**
- Elke netwerkimplementatie zou volledig proprietary zijn.
- Een Cisco-router zou niet communiceren met een Juniper-router.
- Aanpassingen aan één onderdeel (bijv. nieuw encryptieprotocol) vereisen herschrijving van alle software.
- Foutopsporing wordt onmogelijk complex.

**Doel van drie lagen:**

1. **Transport-laag:** Zorgt voor betrouwbare end-to-end communicatie. TCP garandeert dat alle segmenten aankomen, in de juiste volgorde, zonder corruptie — ongeacht het onderliggende netwerk.

2. **Network-laag:** Verzorgt routering. IP bepaalt het beste pad van bron naar bestemming, zelfs over meerdere netwerken en routers heen. Zonder deze laag is internetcommunicatie onmogelijk.

3. **Data Link-laag:** Verzorgt de betrouwbare overdracht van frames tussen twee direct verbonden apparaten. Voegt MAC-adressering en foutdetectie (CRC) toe. Zonder deze laag zouden frames op de kabel niet correct kunnen worden geïdentificeerd.

---

## Vraag 7

**Doelstelling:** De student kan een netwerk schematisch voorstellen en de verschillende onderdelen benoemen/labelen.

**Vraag:** Teken een schematisch diagram van een klein bedrijfsnetwerk met minstens: een router, twee switches, vier computers, een server en een internetverbinding. Label alle onderdelen.

**Antwoord:**

```
                        INTERNET
                           |
                        [Router]          ← Laag 3 (Network): IP-routering
                        /      \
                [Switch 1]    [Switch 2]  ← Laag 2 (Data Link): MAC-switching
               /    \            /    \
            [PC1]  [PC2]      [PC3]  [PC4]  ← Laag 3-7: End-hosts
                               |
                           [Server]       ← Laag 3-7: DNS/DHCP/Web

Verbindingen: UTP Cat6 kabel (Laag 1 — Physical)
```

**Labeling:**

| Onderdeel | Functie | Laag |
|---|---|---|
| Router | Verbindt intern netwerk met internet, routeert pakketten op basis van IP | Laag 3 |
| Switch 1/2 | Verbindt hosts binnen hetzelfde netwerk via MAC-adrestabellen | Laag 2 |
| PC 1–4 | Eindgebruikers, genereren en ontvangen verkeer | Laag 2–7 |
| Server | Biedt diensten aan (DNS, DHCP, web) | Laag 2–7 |
| Kabels | Fysieke verbindingen (UTP Cat6) | Laag 1 |

---

# DLR 3 — Ethernet, Protocollen & Beveiliging

---

## Vraag 1

**Doelstelling:** De student kan uitleggen hoe een Ethernet-netwerk functioneert.

**Vraag:** Beschrijf het Ethernet-protocol in detail. Hoe wordt media access geregeld? Verklaar de CSMA/CD-methode en beschrijf hoe frames eruit zien.

**Antwoord:**

**Ethernet** is het dominante LAN-protocol (IEEE 802.3) dat werkt op de Data Link-laag.

**Media Access Control — CSMA/CD:**

CSMA/CD (Carrier Sense Multiple Access with Collision Detection) wordt gebruikt in half-duplex Ethernet:

1. **Carrier Sense:** Apparaat luistert of het medium vrij is.
2. **Multiple Access:** Meerdere apparaten delen hetzelfde medium.
3. **Transmit:** Als medium vrij is, begint transmissie.
4. **Collision Detection:** Als twee apparaten gelijktijdig zenden → botsing gedetecteerd.
5. **Jam signal:** Beide apparaten sturen een jam-signaal.
6. **Backoff:** Beide wachten een willekeurige tijd (exponential backoff) en proberen opnieuw.

> In modern full-duplex Ethernet (met switches) is CSMA/CD niet meer nodig omdat elk apparaat een eigen dedicated verbinding heeft.

**Ethernet Frame-structuur:**

```
| Preamble | SFD | Dst MAC | Src MAC | Type/Length | Data (Payload) | FCS |
|  7 bytes | 1B  |  6 bytes |  6 bytes |    2 bytes   |   46-1500 bytes | 4B  |
```

- **Preamble:** Synchronisatie (1010... patroon).
- **SFD (Start Frame Delimiter):** Markeert begin van frame.
- **Destination/Source MAC:** 48-bit hardware-adressen.
- **Type/EtherType:** Protocol van payload (bijv. 0x0800 = IPv4).
- **Data:** Payload (min. 46 bytes, max. 1500 bytes).
- **FCS (Frame Check Sequence):** CRC-32 foutdetectie.

---

## Vraag 2

**Doelstelling:** De student kan uitleggen hoe hosts en netwerkapparatuur gebruikt worden in hedendaagse computernetwerken.

**Vraag:** Beschrijf de rol van hosts en netwerkapparatuur (switches, routers, etc.) in een modern netwerk.

**Antwoord:**

**Hosts (End Devices):**
- Genereren en consumeren data (PC's, smartphones, servers, IoT-apparaten).
- Implementeren de volledige protocol-stack (lagen 1–7).
- Communiceren via netwerkinterfaces (NIC) met het netwerk.

**Switches (Laag 2):**
- Verbinden apparaten binnen hetzelfde LAN.
- Leren MAC-adressen via de **MAC address table** (CAM-tabel).
- Sturen frames gericht door naar de juiste poort (unicast) — geen broadcasting naar alle poorten.
- Creëren full-duplex verbindingen → geen CSMA/CD nodig.

**Routers (Laag 3):**
- Verbinden verschillende netwerken (LAN–WAN, LAN–internet).
- Nemen routeringsbeslissingen op basis van IP-adressen en routeringstabellen.
- Werken op de Network-laag.

**Access Points (Laag 2):**
- Bieden draadloze verbinding (Wi-Fi / 802.11).
- Fungeren als brug tussen draadloos en bekabeld netwerk.

**Samenwerking:** Host → Switch (Laag 2, MAC) → Router (Laag 3, IP) → Internet.

---

## Vraag 3

**Doelstelling:** De student kan de werkingsprincipes van netwerkapparatuur uitleggen.

**Vraag:** Leg uit hoe switches en routers werken. Beschrijf de verschillen in hun functionaliteit.

**Antwoord:**

**Hoe een switch werkt:**

1. Frame binnenkomt op poort X met bron-MAC `AA:BB:CC`.
2. Switch slaat op: `AA:BB:CC → poort X` in MAC-tabel.
3. Switch zoekt doel-MAC in tabel.
   - **Gevonden:** Stuur frame alleen naar die poort (unicast).
   - **Niet gevonden:** Stuur naar alle poorten behalve de bronpoort (flooding).
   - **Broadcast (FF:FF:FF:FF:FF:FF):** Altijd naar alle poorten.
4. Werkt op **Laag 2** — kijkt alleen naar MAC-adressen.

**Hoe een router werkt:**

1. Pakket binnenkomt op interface.
2. Router bekijkt doel-IP-adres.
3. Zoekt langste match in **routeringstabel**.
4. Stuurt pakket via de juiste interface door (next-hop).
5. Past MAC-adressen aan voor elk segment (nieuwe Ethernet-frames per hop).
6. Werkt op **Laag 3** — kijkt naar IP-adressen.

**Vergelijking:**

| | Switch | Router |
|---|---|---|
| OSI-laag | Laag 2 | Laag 3 |
| Adressering | MAC-adressen | IP-adressen |
| Bereik | Binnen één netwerk | Tussen netwerken |
| Tabel | MAC-adrestabel | Routeringstabel |
| Broadcasts | Worden doorgestuurd | Worden geblokkeerd |

---

## Vraag 4

**Doelstelling:** De student kan de functie en structuur van MAC- en IPv4/IPv6-adressen uitleggen.

**Vraag:** Beschrijf de structuur van MAC-adressen en IPv4/IPv6-adressen. Waarom hebben we beide nodig?

**Antwoord:**

**MAC-adres (Media Access Control):**
- 48-bit (6 bytes), geschreven als `AA:BB:CC:DD:EE:FF`.
- Wereldwijd uniek, ingebrand in NIC door fabrikant (burned-in address).
- Eerste 3 bytes: OUI (Organizationally Unique Identifier) — fabrikant.
- Laatste 3 bytes: Apparaat-specifiek.
- Gebruikt voor communicatie **binnen één netwerk** (Laag 2).

**IPv4-adres:**
- 32-bit, geschreven als `192.168.1.10` (vier octetten van 0–255).
- Bestaat uit **netwerk-deel** en **host-deel** (bepaald door subnetmasker).
- Hiërarchisch en routeerbaar over internet.
- Voorbeeld: `192.168.1.10 / 255.255.255.0` = netwerk `192.168.1.0`.

**IPv6-adres:**
- 128-bit, geschreven als `2001:0db8:85a3::8a2e:0370:7334`.
- Oplossing voor IPv4-adrestekort (~340 undeciljoen adressen).
- Ingebouwde auto-configuratie (SLAAC) en betere beveiliging (IPsec).

**Waarom beide nodig?**
- **MAC** is lokaal: identificeert het apparaat binnen het LAN, werkt frame-per-frame.
- **IP** is globaal: identificeert de locatie in het netwerk, werkt end-to-end.
- Een router vervangt bij elke hop de MAC-adressen (nieuw frame), maar behoudt de IP-adressen (zelfde pakket).
- Zonder MAC: geen lokale communicatie. Zonder IP: geen routering over netwerken.

---

## Vraag 5

**Doelstelling:** De student kan het doel van het ARP en ND protocol in detail toelichten.

**Vraag:** Wat doen ARP en ND? Waarom zijn zij nodig? Beschrijf het proces.

**Antwoord:**

**ARP (Address Resolution Protocol) — IPv4:**

ARP lost IP-adressen op naar MAC-adressen binnen een lokaal netwerk.

**Waarom nodig?** Een host kent het IP-adres van de bestemming, maar heeft het MAC-adres nodig om een Ethernet-frame te maken.

**ARP-proces:**
1. Host A wil `192.168.1.5` bereiken, kent MAC niet.
2. Stuurt **ARP Request** (broadcast): *"Wie heeft IP 192.168.1.5? Vertel het aan 192.168.1.1."*
3. Host B heeft dit IP → stuurt **ARP Reply** (unicast): *"192.168.1.5 is aan MAC `BB:CC:DD:EE:FF:00`."*
4. Host A slaat MAC op in **ARP-cache** voor toekomstig gebruik.

**ND (Neighbor Discovery) — IPv6:**

ND is het IPv6-equivalent van ARP, maar uitgebreid. Gebruikt **ICMPv6**-berichten.

Functies:
- **Neighbor Solicitation / Advertisement:** Equivalent van ARP Request/Reply.
- **Router Discovery:** Clients ontdekken routers en het standaard gateway-adres.
- **SLAAC:** Stateless Address Autoconfiguration — hosts configureren zichzelf.
- **Duplicate Address Detection (DAD):** Controleert of een IPv6-adres al in gebruik is.

**Laagmodel:** ARP en ND opereren tussen Laag 2 (MAC) en Laag 3 (IP) — ze overbruggen de kloof.

---

## Vraag 6

**Doelstelling:** De student kan aan de hand van gecapteerd netwerkverkeer de werking van netwerkprotocollen uitleggen.

**Vraag:** Je hebt een Wireshark-capture van een HTTP-verzoek. Beschrijf welke protocollen je zou zien.

**Antwoord:**

Bij een HTTP-verzoek zie je in Wireshark de volgende protocollen (van laag naar laag):

**Laag 1 — Physical (niet zichtbaar in Wireshark):**
- Elektrische signalen / lichtpulsen over kabel/fiber.

**Laag 2 — Ethernet:**
- Bron- en doel-MAC-adres.
- EtherType: `0x0800` (IPv4).
- FCS voor foutdetectie.

**Laag 3 — IP:**
- Bron-IP en doel-IP.
- TTL (Time To Live), protocol-veld (`6` = TCP).
- Fragmentatie-informatie.

**Laag 4 — TCP:**
- Bronpoort (willekeurig hoge poort, bijv. 54321) en doelpoort (80 voor HTTP).
- Three-way handshake: `SYN → SYN-ACK → ACK`.
- Volgnummers (Sequence Numbers) en bevestigingsnummers (ACK Numbers).

**Laag 7 — HTTP:**
- `GET /index.html HTTP/1.1`
- Headers: `Host: example.com`, `User-Agent`, `Accept`.
- Response: `HTTP/1.1 200 OK` + HTML-inhoud.

**Wireshark-filter voor HTTP:** `http` of `tcp.port == 80`

---

## Vraag 7

**Doelstelling:** De student kan het doel en het functioneren van routeringsprotocollen uitleggen.

**Vraag:** Wat zijn routeringsprotocollen? Verschil tussen statische en dynamische routering? Hoe werkt OSPF?

**Antwoord:**

**Routeringsprotocollen** bepalen hoe routers informatie over netwerken uitwisselen en de beste route naar een bestemming kiezen.

**Statische routering:**
- Routes worden handmatig geconfigureerd door de beheerder.
- Voordelen: eenvoudig, voorspelbaar, geen overhead.
- Nadelen: schaalt niet, geen automatische aanpassing bij storingen.
- Gebruik: kleine netwerken, standaard gateway.

**Dynamische routering:**
- Routers wisselen automatisch route-informatie uit.
- Passen zich aan bij wijzigingen (link down, nieuwe netwerken).
- Voorbeelden: RIP, OSPF, EIGRP, BGP.

**OSPF (Open Shortest Path First) — link-state protocol:**

1. **Neighbor Discovery:** Routers sturen Hello-pakketten en bouwen een lijst van buren op.
2. **Database Exchange:** Routers wisselen **LSA's (Link State Advertisements)** uit — informatie over hun interfaces en verbindingen.
3. **LSDB (Link State Database):** Elke router bouwt een volledige kaart van het netwerk op.
4. **SPF-algoritme (Dijkstra):** Elke router berekent de kortste route naar elk netwerk op basis van **cost** (bandbreedte).
5. **Routeringstabel:** De beste routes worden in de tabel gezet.

**Na een link-failure:** OSPF detecteert dit via Hello-timeouts → verstuurt nieuwe LSA's → alle routers herbereken hun routes (convergentie).

---

## Vraag 8

**Doelstelling:** De student kan beveiligingstechnieken voor netwerkverkeer uitleggen.

**Vraag:** Beschrijf drie beveiligingstechnieken voor netwerkverkeer.

**Antwoord:**

**1. Firewall (Laag 3–7):**
- Filtert netwerkverkeer op basis van regels.
- Blokkeert ongewenst verkeer (bijv. onbekende bronIP's, bepaalde poorten).
- Typen: stateless (eenvoudige pakketfiltering), stateful (volgt verbindingsstatus), applicatie-laag (DPI).

**2. VPN / IPsec (Laag 3):**
- Versleutelt verkeer tussen twee endpoints via een beveiligde tunnel.
- IPsec gebruikt **AH** (authenticatie) en **ESP** (encryptie + authenticatie).
- Beschermt data-in-transit tegen afluisteren en manipulatie.
- Gebruik: remote werken, site-to-site verbindingen.

**3. TLS/SSL (Laag 4–7):**
- Versleutelt verbindingen op transport/applicatieniveau (HTTPS, SMTPS).
- Gebruikt asymmetrische encryptie voor sleuteluitwisseling, daarna symmetrische encryptie voor data.
- Biedt authenticatie (via certificaten), vertrouwelijkheid en integriteit.
- Zonder TLS: HTTP-verkeer is leesbaar voor iedereen op het netwerk.

---

## Vraag 9

**Doelstelling:** De student kan uitleggen hoe servers en clients communiceren op basis van TCP/IP.

**Vraag:** Beschrijf het volledige communicatieproces tussen client en server, inclusief TCP three-way handshake.

**Antwoord:**

**1. TCP Three-Way Handshake (verbinding openen):**

```
Client                          Server
  |── SYN (seq=100) ──────────→ |   Client wil verbinding
  |← SYN-ACK (seq=200, ack=101)─|   Server accepteert, stuurt eigen seq
  |── ACK (ack=201) ────────────→|   Client bevestigt → verbinding open
```

**2. Data transfer:**
- Client stuurt HTTP GET-verzoek → in TCP-segmenten.
- Server bevestigt elk segment met ACK.
- Bij verlies: hertransmissie.
- Flow control via **window size** (ontvanger bepaalt hoeveel data tegelijk).

**3. Verbinding sluiten (Four-Way Termination):**

```
Client                          Server
  |── FIN ─────────────────────→|   Client klaar met sturen
  |← ACK ──────────────────────|   Server bevestigt
  |← FIN ──────────────────────|   Server ook klaar
  |── ACK ─────────────────────→|   Client bevestigt → verbinding gesloten
```

**Poorten:**
- Client gebruikt een willekeurige **ephemeral port** (bijv. 54321).
- Server luistert op een **well-known port** (80 = HTTP, 443 = HTTPS, 22 = SSH).

---

## Vraag 10

**Doelstelling:** De student kan het doel en functioneren van cryptografie in functie van VPN-toepassingen uitleggen.

**Vraag:** Leg uit hoe cryptografie in VPN's werkt. Beschrijf symmetrische en asymmetrische encryptie.

**Antwoord:**

**Symmetrische encryptie:**
- Zender en ontvanger gebruiken **dezelfde sleutel** voor encryptie en decryptie.
- Snel en efficiënt voor grote hoeveelheden data.
- Algoritmen: AES-256, 3DES.
- Probleem: hoe deel je de sleutel veilig uit? → oplossing: asymmetrische encryptie.

**Asymmetrische encryptie:**
- Gebruikt een **sleutelpaar**: publieke sleutel (iedereen mag die kennen) en private sleutel (geheim).
- Data versleuteld met publieke sleutel → alleen te ontsleutelen met private sleutel.
- Traag → alleen gebruikt voor sleuteluitwisseling en authenticatie.
- Algoritmen: RSA, Diffie-Hellman, ECC.

**Hoe een VPN-tunnel werkt (bijv. IPsec):**

1. **Fase 1 — IKE (Internet Key Exchange):**
   - Asymmetrische encryptie (Diffie-Hellman) om veilig een gedeeld geheim uit te wisselen.
   - Authenticatie via pre-shared key of certificaten.

2. **Fase 2 — IPsec Tunnel:**
   - Symmetrische sleutel (afgeleid van fase 1) wordt gebruikt voor AES-encryptie van alle data.
   - ESP (Encapsulating Security Payload) encapsuleert en versleutelt IP-pakketten.
   - Data reist versleuteld door het internet → niemand kan meelezen.

**Samengevat:** Asymmetrische encryptie lost het sleuteldistributieprobleem op; symmetrische encryptie versleutelt daarna efficiënt de datastroom.

---

## Vraag 11

**Doelstelling:** De student kan de werking van de belangrijkste netwerkprotocollen van de TCP/IP-familie uitleggen.

**Vraag:** Kies vijf netwerkprotocollen. Beschrijf doel, functie, laag en praktisch voorbeeld.

**Antwoord:**

**1. DNS (Domain Name System) — Application-laag:**
- **Doel:** Vertaalt domeinnamen naar IP-adressen.
- **Functie:** Client stuurt query naar DNS-server; server antwoordt met IP. Hiërarchisch systeem (root → TLD → authoritative).
- **Voorbeeld:** `ping google.com` → DNS lost op naar `142.250.x.x`.

**2. DHCP (Dynamic Host Configuration Protocol) — Application-laag:**
- **Doel:** Kent automatisch IP-adressen toe aan clients.
- **Functie:** DORA-proces: Discover → Offer → Request → Acknowledge.
- **Voorbeeld:** Laptop verbindt met Wi-Fi → krijgt automatisch `192.168.1.100` toegewezen.

**3. HTTP/HTTPS (HyperText Transfer Protocol) — Application-laag:**
- **Doel:** Webverkeer — verzoeken en antwoorden van webpagina's.
- **Functie:** Client stuurt `GET /index.html` → server antwoordt `200 OK` + HTML.
- **Voorbeeld:** Browser laadt `https://ucll.be` → HTTPS = HTTP over TLS.

**4. ICMP (Internet Control Message Protocol) — Network-laag:**
- **Doel:** Foutmeldingen en diagnostiek.
- **Functie:** `ping` stuurt ICMP Echo Request → ontvanger stuurt Echo Reply. `traceroute` gebruikt ICMP TTL-exceeded berichten.
- **Voorbeeld:** `ping 8.8.8.8` test bereikbaarheid van Google DNS.

**5. TCP (Transmission Control Protocol) — Transport-laag:**
- **Doel:** Betrouwbare, verbindingsgerichte datatransmissie.
- **Functie:** Segmentatie, three-way handshake, ACK's, hertransmissie bij verlies, flow control.
- **Voorbeeld:** Downloaden van een bestand — elk segment wordt bevestigd en opnieuw verzonden indien nodig.

---

## Vraag 12

**Doelstelling:** De student kan het doel en de functie van een firewall uitleggen.

**Vraag:** Wat is een firewall? Beschrijf minstens twee soorten firewalls.

**Antwoord:**

Een **firewall** is een beveiligingssysteem dat inkomend en uitgaand netwerkverkeer monitort en filtert op basis van vooraf gedefinieerde regels.

**1. Stateless Packet Filter (Laag 3–4):**
- Bekijkt elk pakket afzonderlijk: bron-IP, doel-IP, protocol, poort.
- Geen geheugen van eerdere pakketten of verbindingsstatus.
- Snel maar beperkt — kan geen context bijhouden.
- Voorbeeld: blokkeert alle pakketten van IP `10.0.0.5`.

**2. Stateful Firewall (Laag 3–4):**
- Houdt de **verbindingsstatus** bij in een state table.
- Kent het verschil tussen een nieuw verzoek en een antwoord op een bestaande verbinding.
- Laat return-traffic automatisch door voor established connections.
- Blokkert paketten die niet tot een bekende verbinding behoren.

**3. Application Layer Firewall / Next-Gen Firewall (Laag 7):**
- Inspecteert de inhoud van pakketten (Deep Packet Inspection).
- Kan specifieke applicaties herkennen en blokkeren (bijv. BitTorrent, Facebook).
- Detecteert malware en aanvallen op applicatieniveau.

**Hoe regels werken:**
- Regels worden sequentieel geëvalueerd (top naar bottom).
- Eerste match wint.
- Standaard: impliciete `deny all` aan het einde (default deny-policy).

---

# DLR 4 — Configuratie, Subnetting & Troubleshooting

---

## Vraag 1

**Doelstelling:** De student kan fysiek netwerkmateriaal installeren, onderhouden en vervangen.

**Vraag:** Beschrijf het stappenplan voor de installatie van Ethernet-kabels in een patchpaneel.

**Antwoord:**

**Benodigde tools:** Kabelstripper, punchdown-tool (110-blok), RJ45-crimper, kabelkapper, netwerktester.

**Stappen:**

1. **Planning:** Bepaal de kabelroute en label alle kabels (bijv. A01–A24).
2. **Kabel intrekken:** Trek UTP-kabel van het patchpaneel naar de wanddoos.
3. **Isolatie strippen:** Strip ~3 cm buitenmantel — niet te diep (beschadigt paren).
4. **Paren scheiden:** Separeer de vier kabelpaartjes. Verwijder zo weinig mogelijk van de twist (max. 1,3 cm).
5. **Kleurvolgorde aanhouden:** Gebruik **T568B** (of T568A, maar consistent):
   - T568B: Wit/Oranje, Oranje, Wit/Groen, Blauw, Wit/Blauw, Groen, Wit/Bruin, Bruin.
6. **Punchdown:** Duw elke ader in het juiste slot met de punchdown-tool (afsnijden automatisch).
7. **Herhaal** voor wanddoos of andere zijde.
8. **Afwerking:** Sluit het patchpaneel af, bevestig kabels met kabelbinders.
9. **Testen:** Gebruik een kabelkwaliteitstester:
   - Controleer continuïteit (alle 8 aders).
   - Controleer op kruisverbindingen (miswiring).
   - Optioneel: certificationtester voor lengte en signaalintegriteit.

**Veelgemaakte fouten:**
- Te veel twist verwijderd → crosstalk.
- Verkeerde kleurvolgorde → miswiring.
- Buitenmantel niet ver genoeg ingebracht → trekbelasting op aders.
- T568A aan één kant en T568B aan de andere → crossover-kabel (onbedoeld).

---

## Vraag 2

**Doelstelling:** De student kan IP-adressering, subnetting en VLSM toepassen.

**Vraag:** Je hebt netwerk 192.168.10.0/24. Verdeel in drie subnetten voor 50, 30 en 20 hosts.

**Antwoord:**

**Formule:** Aantal hosts = 2^n - 2 (n = hostbits). Altijd afronden naar volgende macht van 2.

**Subnet 1 — 50 hosts:**
- Nodig: 2^6 - 2 = 62 hosts → /26 (subnetmasker: 255.255.255.192)
- **Netwerkadres:** `192.168.10.0/26`
- **Broadcastadres:** `192.168.10.63`
- **DHCP-bereik:** `192.168.10.1` – `192.168.10.62`

**Subnet 2 — 30 hosts:**
- Nodig: 2^5 - 2 = 30 hosts → /27 (subnetmasker: 255.255.255.224)
- **Netwerkadres:** `192.168.10.64/27`
- **Broadcastadres:** `192.168.10.95`
- **DHCP-bereik:** `192.168.10.65` – `192.168.10.94`

**Subnet 3 — 20 hosts:**
- Nodig: 2^5 - 2 = 30 hosts → /27 (subnetmasker: 255.255.255.224)
- **Netwerkadres:** `192.168.10.96/27`
- **Broadcastadres:** `192.168.10.127`
- **DHCP-bereik:** `192.168.10.97` – `192.168.10.126`

**Samenvatting:**

| Subnet | Netwerkadres | Broadcast | DHCP Bereik | Hosts |
|---|---|---|---|---|
| Afdeling 1 (50) | 192.168.10.0/26 | 192.168.10.63 | .1 – .62 | 62 |
| Afdeling 2 (30) | 192.168.10.64/27 | 192.168.10.95 | .65 – .94 | 30 |
| Afdeling 3 (20) | 192.168.10.96/27 | 192.168.10.127 | .97 – .126 | 30 |

---

## Vraag 3

**Doelstelling:** De student kan een client in een TCP/IP-netwerk correct configureren.

**Vraag:** Beschrijf hoe je een Windows- en Linux-computer configureert in een TCP/IP-netwerk.

**Antwoord:**

**Te configureren parameters:**
- IP-adres
- Subnetmasker
- Standaard gateway
- DNS-server(s)

**Windows:**

1. `Instellingen → Netwerk en internet → Ethernet → IP-instellingen wijzigen`
2. Stel in op "Handmatig" (of DHCP voor automatisch).
3. Vul IP, subnetmasker, gateway, DNS in.
4. Verifieer:
   ```
   ipconfig /all          → toont alle parameters
   ping 192.168.1.1       → test gateway
   ping 8.8.8.8           → test internetconnectiviteit
   nslookup google.com    → test DNS
   ```

**Linux (via NetworkManager / ip-commando):**

```bash
# Tijdelijke configuratie (verdwijnt na reboot):
ip addr add 192.168.1.10/24 dev eth0
ip route add default via 192.168.1.1
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Permanente configuratie (bijv. Debian/Ubuntu via netplan):
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      addresses: [192.168.1.10/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]

sudo netplan apply
```

**Verificatie Linux:**
```bash
ip addr show            # IP-adres
ip route show           # routeringstabel
ping 192.168.1.1        # gateway testen
dig google.com          # DNS testen
```

---

## Vraag 4

**Doelstelling:** De student kan netwerkverkeer capteren.

**Vraag:** Leg uit hoe je Wireshark gebruikt om netwerkverkeer te capteren.

**Antwoord:**

**Starten van een capture:**
1. Open Wireshark.
2. Selecteer de juiste netwerkinterface (bijv. `eth0`, `Wi-Fi`).
3. Klik op de blauwe haaienvinfknop (Start capturing).

**Stoppen:**
- Klik op de rode vierkantknop (Stop).

**Filters:**

*Capture filters* (vóór capture, BPF-syntax):
```
host 192.168.1.10       → alleen verkeer van/naar dit IP
port 80                 → alleen HTTP
tcp                     → alleen TCP-verkeer
```

*Display filters* (tijdens/na capture):
```
ip.addr == 192.168.1.10
tcp.port == 443
http
dns
tcp.flags.syn == 1      → alleen SYN-pakketten
```

**Opslaan:**
- `File → Save As` → kies `.pcapng` of `.pcap` formaat.

**Laden:**
- `File → Open` → selecteer capture-bestand.

**Handige features:**
- **Follow TCP Stream:** rechtsklik op pakket → volledig gesprek in leesbare tekst.
- **Statistics → Protocol Hierarchy:** overzicht van protocollen.
- **Statistics → IO Graph:** bandbreedte over tijd.

---

## Vraag 5

**Doelstelling:** De student kan DHCP installeren en configureren.

**Vraag:** Beschrijf hoe je een DHCP-server installeert op Windows Server.

**Antwoord:**

**Installatie:**
1. `Server Manager → Add Roles and Features → DHCP Server`.
2. Post-installatie: `Complete DHCP Configuration` wizard.

**DORA-proces:**
1. **Discover:** Client broadcast `DHCPDISCOVER` (src: 0.0.0.0, dst: 255.255.255.255).
2. **Offer:** Server biedt IP aan via `DHCPOFFER`.
3. **Request:** Client vraagt het aangeboden IP op via `DHCPREQUEST`.
4. **Acknowledge:** Server bevestigt met `DHCPACK` — client heeft nu IP.

**Scope aanmaken (Windows Server):**
1. Open `DHCP Manager`.
2. Rechtsklik op `IPv4 → New Scope`.
3. Configureer:
   - Naam en beschrijving.
   - **IP-bereik:** bijv. `192.168.1.100` – `192.168.1.200`.
   - **Subnetmasker:** `255.255.255.0`.
   - **Exclusies:** bijv. `192.168.1.100` – `192.168.1.110` voor servers.
   - **Lease duur:** standaard 8 dagen.
   - **Default Gateway:** `192.168.1.1`.
   - **DNS-servers:** `8.8.8.8`.
4. Activeer de scope.

**Verificatie:**
- Op client: `ipconfig /release` gevolgd door `ipconfig /renew`.
- Op server: `DHCP Manager → Address Leases` → controleer toegewezen IP's.

---

## Vraag 6

**Doelstelling:** De student kan OSPF configureren, onderhouden en analyseren.

**Vraag:** Teken een topologie met 4 routers en configureer OSPF volledig.

**Antwoord:**

**Topologie:**
```
R1 (10.0.12.1) ──── R2 (10.0.12.2)
  |                       |
(10.0.13.1)         (10.0.24.2)
  |                       |
R3 (10.0.13.3) ──── R4 (10.0.34.4)
     (10.0.34.3)
```

**Cisco IOS OSPF-configuratie (voorbeeld R1):**

```
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 10.0.12.0 0.0.0.255 area 0
R1(config-router)# network 10.0.13.0 0.0.0.255 area 0
R1(config-router)# network 192.168.1.0 0.0.0.255 area 0
```

**OSPF werking:**

1. **Hello-pakketten:** Routers sturen Hellos → ontdekken buren → vormen **adjacency**.
2. **LSA-uitwisseling:** Elke router adverteert zijn links (netwerken, kosten).
3. **LSDB:** Elke router bouwt een identieke database op van het netwerk.
4. **Dijkstra (SPF):** Berekent kortste pad op basis van **cost** (= 10^8 / bandbreedte).
5. **Routeringstabel:** Beste routes worden geïnstalleerd.

**Cost-berekening:**
- 1 Gbps: cost = 1
- 100 Mbps: cost = 1 (standaard referentie)
- 10 Mbps: cost = 10

**Na link-failure:**
- Hello-timeout → router verwijdert buur.
- Nieuwe LSA's worden verstuurd (flooding).
- Alle routers herberekenen SPF → nieuwe routes in tabel.
- Convergentietijd: typisch 1–5 seconden.

---

## Vraag 7

**Doelstelling:** De student kan ACLs installeren, onderhouden en analyseren.

**Vraag:** Maak een standaard ACL dat verkeer van 10.0.1.0/24 blokkeert maar 10.0.2.0/24 toestaat.

**Antwoord:**

**Standaard ACL (filtert op bron-IP):**

```
R1(config)# access-list 10 deny 10.0.1.0 0.0.0.255
R1(config)# access-list 10 permit 10.0.2.0 0.0.0.255
R1(config)# access-list 10 deny any
```

**ACL toepassen op interface (zo dicht mogelijk bij bron):**

```
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip access-group 10 in
```

**Werking:**
- Regel 1: Blokkeert alle pakketten van `10.0.1.0/24`.
- Regel 2: Staat pakketten van `10.0.2.0/24` toe.
- Regel 3: Impliciete `deny any` (explicieter gemaakt).
- Regels worden top-down geëvalueerd, eerste match wint.

**Extended ACL (filtert op bron, bestemming, protocol, poort):**

```
R1(config)# ip access-list extended BLOCK_SUBNET1
R1(config-ext-nacl)# deny ip 10.0.1.0 0.0.0.255 any
R1(config-ext-nacl)# permit ip 10.0.2.0 0.0.0.255 any
R1(config-ext-nacl)# permit ip any any
```

**Voordeel extended ACL:** Kan filteren op doel-IP, protocol (TCP/UDP/ICMP) en poortnummer. Extended ACL's worden zo dicht mogelijk bij de **bron** geplaatst; standaard ACL's zo dicht mogelijk bij de **bestemming**.

---

## Vraag 8

**Doelstelling:** De student kan fouten in een netwerk opsporen en herstellen.

**Vraag:** Een gebruiker kan geen internet bereiken. Beschrijf je troubleshooting-aanpak.

**Antwoord:**

**Methodologie: bottom-up (laag 1 naar laag 7)**

**Stap 1 — Laag 1 (Physical):**
```
- Controleer kabelverbinding (zit de kabel erin?)
- Controleer LED-indicatoren op NIC en switch
- Probeer een andere kabel/poort
```

**Stap 2 — Laag 2 (Data Link):**
```
ipconfig /all (Windows) of ip addr (Linux)
→ Heeft de NIC een IP-adres?
→ Is de NIC actief (UP)?
```

**Stap 3 — Laag 3 (Network) — IP-configuratie:**
```
ipconfig /all
→ Correct IP-adres? (niet 169.254.x.x — APIPA = DHCP mislukt)
→ Correct subnetmasker?
→ Default gateway ingesteld?
```

**Stap 4 — Laag 3 — Connectiviteit testen:**
```
ping 127.0.0.1          → loopback (test TCP/IP stack)
ping 192.168.1.10       → eigen IP
ping 192.168.1.1        → default gateway
ping 8.8.8.8            → internet (bypasses DNS)
ping google.com         → test DNS
```

**Stap 5 — DNS:**
```
nslookup google.com     → DNS werkend?
ipconfig /flushdns       → cache leegmaken
```

**Stap 6 — Routering:**
```
tracert 8.8.8.8 (Windows) / traceroute 8.8.8.8 (Linux)
→ Waar stopt de route?
```

**Meest waarschijnlijke oorzaken:**
- DHCP-server niet bereikbaar → geen IP.
- Verkeerde gateway ingesteld.
- DNS-server onbereikbaar.
- Firewall blokkeert uitgaand verkeer.
- ISP-probleem (andere gebruikers testen dit).

---

## Vraag 9

**Doelstelling:** De student kan een netwerk effectief analyseren om fouten op te sporen.

**Vraag:** Je krijgt een Wireshark-capture met hoge latency. Hoe analyseer je dit?

**Antwoord:**

**Stap 1 — Eerste beoordeling:**
```
Statistics → Summary          → algemene statistieken (duur, pakketaantal)
Statistics → Protocol Hierarchy → welke protocollen domineren?
Statistics → IO Graph         → is er een piek in verkeer?
```

**Stap 2 — Retransmissions detecteren:**
```
Display filter: tcp.analysis.retransmission
→ Veel retransmissions = pakketverlies → slechte link of overbelasting
```

**Stap 3 — Hoge latency/RTT:**
```
Statistics → TCP Stream Graphs → Round Trip Time
→ Hoge RTT-pieken = congestieproblemen of slechte routering

Display filter: tcp.analysis.ack_rtt > 0.1
→ ACK's die meer dan 100ms duren
```

**Stap 4 — Broadcast storm detecteren:**
```
Statistics → Protocol Hierarchy → hoog percentage broadcast
Display filter: eth.dst == ff:ff:ff:ff:ff:ff
→ Te veel broadcasts = loop in netwerk (geen STP?) of misconfiguratie
```

**Stap 5 — Specifieke verbinding analyseren:**
```
Rechtsklik op pakket → Follow TCP Stream
→ Bekijk de volledige conversatie
→ Zijn er lange vertragingen tussen verzoek en antwoord?
```

**Conclusie-aanpak:**

| Symptoom | Oorzaak | Oplossing |
|---|---|---|
| Veel retransmissions | Pakketverlies, slechte kabel | Kabel vervangen, switch testen |
| Hoge RTT | Congestie, slechte route | QoS instellen, route optimaliseren |
| Broadcast storm | STP-loop | STP controleren/inschakelen |
| DNS-timeouts | DNS-server overbelast | DNS-server controleren |