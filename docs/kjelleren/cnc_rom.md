# CNC-rom

## Stor CNC: MPCNC Lowrider4 fra v1engineering.
Arbeidsområde XYZ=1220x2450x100 mm (byggeplatestørrelse)

[Dokumentasjon hos v1e.com](https://docs.v1e.com/lowrider/)

Collet-størrelser(spennhylse/spenntange): 1/4 " og 8mm (3.175mm på vei!) **NB: 1/4" og 6mm passer ikke i samme spennhylse**

Router: Dewalt håndoverfres D26204-QS (Amerikansk modellversjon: DWP611)

### Huskeliste for bruk
- Husk å starte **og stoppe** maskina med gantry oppå blokkene, og begge "vognene" helt nederst på bordet, mot stopperne. (bilde kommer)
- styring gjøres med [http://192.168.2.59](http://192.168.2.59) når du er pålogget Tromsoskapere wifi. 
- Travel rate 5000mm/m
- Probetykkelse 0.8mm
- Anbefalt feed rate (kutte-fart) 1000mm/m
- Enkel arbeidsflyt:
  - Sørg for at gantry står oppå blokkene og helt nederst (mot deg)
  - Slå på strømmen på styringsboksen på veggen
  - Jog/styr fresestålet over materialet til planlagt null-punkt
  - Sett X0 og Y0 <img width="129" height="46" alt="image" src="https://github.com/user-attachments/assets/cf19dec7-69cd-4251-8c33-6d521a8c8cd2" />
  - Beveg fresestålet ned på materialet og sett Z0, evt bruk probefunksjon med 0.8 mm
  - Slå på fresen med manuell bryter på styringsboks, eller automatisk med GCODE.
  - Klar, ferdig, kjør!


#### Sikkerhet 🚨

-   **Obligatorisk kurs:** Du må ha gjennomført og bestått sertifiseringskurset for å bruke denne maskinen.
-   **Vernebriller er påbudt** til enhver tid i dette rommet når maskinen kjører.
-   Fest alltid materialet skikkelig. En løs del kan bli et farlig prosjektil.
-   Bruk avsugssystemet. Fint støv er helseskadelig.

## Mindre CNC: Bravo CNC BE303
Mindre arbeidsområde, fin for gravering, skjæring i plast, myke metaller ol. Foreløpig ikke liv i denne. Må enten avlese/dekode proprietær kode og bruke den på en moderne gkode-sender eller bytte ut kontrollkort med et open source alternativ.
