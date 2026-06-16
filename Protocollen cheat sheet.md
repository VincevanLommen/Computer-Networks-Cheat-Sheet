# Protocollen uit OSI model
| Laag | Protocol | Afkorting | Korte toelichting |
|---|----|-------------------|-----------------------------|
| 4 | TCP | Transmission Control Protocol | Informatie betrouwbaar doorsturen. Vaak poort 443 of 80. Gebruik bij bestanden, web en SSH. |
| 4 | UDP | User Datagram Protocol | Veel informatie snel doorsturen zonder bevestiging. Gebruik bij DNS, DHCP en streaming. |
| 3 | ICMPv6 Neighbor Discovery | ND | In IPv6 nodig voor adresvinding, routerontdekking en controle van buren. |
| 2 | ARP | Address Resolution Protocol | IP omzetten naar MAC op IPv4-netwerken. |

# IPv6 Neighbor Discovery (ND)

ND is een onderdeel van **ICMPv6** en vervangt bij IPv6 veel van wat ARP bij IPv4 doet. Het helpt apparaten om andere hosts, routers en adressen te vinden en te controleren.

## Belangrijkste ND-berichten

| Bericht | Doel | Wat gebeurt er? |
|---|---|---|
| **RS** (Router Solicitation) | Router zoeken | Een host vraagt aan een router: “Heb jij informatie voor mij?” |
| **RA** (Router Advertisement) | Routerinformatie verspreiden | Een router stuurt prefix, default gateway en soms DNS-info |
| **NS** (Neighbor Solicitation) | Buren zoeken | Een host vraagt: “Welke MAC/Link-layer hoort bij dit IPv6-adres?” |
| **NA** (Neighbor Advertisement) | Antwoord op NS | Een host of router antwoordt met de juiste link-layer informatie |
| **Redirect** | Beter pad aangeven | Een router zegt: “Voor deze bestemming is een andere router beter” |

## Waarom is ND belangrijk?

- **Adresconfiguratie**: helpt bij SLAAC en DHCPv6
- **Routerdetectie**: hosts weten welke router als default gateway werkt
- **Buren controleren**: apparaten zien of een buur nog bereikbaar is
- **Duplicate Address Detection (DAD)**: een host kan checken of een zelf gekozen IPv6-adres al in gebruik is

## ND vs ARP

| Aspect | ARP | ND |
|---|---|---|
| IP-versie | IPv4 | IPv6 |
| Protocol | Broadcast-gebaseerd | ICMPv6-gebaseerd |
| Extra taken | Alleen adresresolutie | Routerdetectie, prefix-info, DAD, redirect |

# Applicatie-protocollen

| Applicatie | Protocol | Korte toelichting |
|-----------|----------|-------------------|
| Web browsing | HTTP | Verstuurt webpagina’s tussen browser en server. |
| email | SMTP / IMAP / POP3 | SMTP verzendt mails; IMAP/POP3 haalt mails op. |
| File sharing | FTP / SMB / NFS | FTP voor bestandsoverdracht; SMB voor gedeelde mappen in netwerken. |
| automatic host config | DHCP | Deelt automatisch IP‑adressen uit. |
| Name resolution | DNS | Zet domeinnamen om naar IP‑adressen. |

