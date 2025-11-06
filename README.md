# Dokumentasjon for 🏡 Skogstua fellesverksted 🏡

Velkommen! Dette er "lageret" (repoet) for all dokumentasjon på [docs.tromsoskapere.no](https://docs.tromsoskapere.no)

Målet er at alle i foreningen skal kunne bidra med oppdatering av dokumentasjonen for verkstedet. Du trenger ikke installere egen programvare for å gjøre enkle tekstendringer. Ved å redigere filer på github vil dette oppdatere hjemmesiden, etter en admin har godkjent endringen.

Navigasjonsstrukturen på dockumentasjonssiden er en direkte avspeiling av katalogstrukturen i /docs/. Filene er lagret i [markdown-format](https://www.markdownguide.org/basic-syntax/), med .md endelse. Hver fil blir en egen html side. Alle .md filer må starte med `# Tittel`. Bilder laster du opp i samme mappe og legger inn med `![Bildetekst](eksempelbilde.png)`

---

## Veiledning

### 🛑 Før du starter: GitHub-bruker og tilgang

For å kunne foreslå endringer som beskrevet i guiden under, må du ha en gratis GitHub-bruker.

1.  **Opprett bruker:** Gå til [github.com](https://github.com) for å registrere deg hvis du ikke har en bruker fra før.
2.  **Be om tilgang:** Send en melding til en administrator (Alf eller Torbjørn, eller i Discord-kanalen) med GitHub-brukernavnet ditt. Du må legges til som medlem i organisasjonen vår før du kan lagre endringer.

Når du har fått tilgang, kan du følge guiden under. *(For erfarne github brukere: Det er også mulig å clone repoet og jobbe på en ekstern PR som kan merges.)*

---

## ✏️ Slik gjør du en endring

Den enkleste måten å redigere på er å bruke GitHubs egen innebygde fil-editor. Du kan også bruke VSCODE (Web) hvis du foretrekker det.

### 1. Finn filen du vil endre

* Alle sidene på nettsiden ligger i **`docs/`**-mappen.
* Bruk filutforskeren på denne siden til å navigere deg frem til riktig fil (f.eks. `docs/kjelleren/maskinrom/pussemaskin.md`).
* Klikk på filnavnet for å åpne og lese filen.

### 2. Åpne editoren

* Oppe til høyre over filinnholdet, klikk på **blyant-ikonet** (✏️) for å "Edit this file".

### 3. Gjør endringen

* Du er nå i en enkel teksteditor.
* Rediger teksten akkurat som i et vanlig tekstdokument. Husk å start teksten med `# Tittel` Sidene er skrevet i [Markdown](https://www.markdownguide.org/basic-syntax/). 

### 4. Lagre endringen ("Propose changes")

Når du er fornøyd, må du lagre endringen din.

1.  Scroll helt **nederst** på siden til du ser en boks som heter **"Commit changes"**.
2.  I den første tekstboksen, skriv en **kort melding** om HVA du gjorde (f.eks. "Oppdaterte info om pussemaskin").
3.  La "Create a new branch..."-valget stå (dette er påkrevd).
4.  Trykk på den grønne knappen **"Propose changes"**.

### 5. Opprett en "Pull Request" (PR)

Du har nå lagret endringen din på en "kladd". Nå må du formelt be om at den blir en del av den endelige nettsiden.

1.  GitHub tar deg automatisk til en ny side som heter "Open a pull request".
2.  Du trenger ikke fylle ut noe mer. Bare trykk på den store, grønne knappen **"Create pull request"**.

**Ferdig!** Du har nå sendt inn et endringsforslag. Det eneste som gjenstår er at en administrator godkjenner den.

---

### For admins
1. Hvis det ligger pull requests inne må disse godkjennes.
2. Alle endringer på main blir publisert når du kjører workflowen "🚀 Deploy docs.tromsoskapere.no". Dette gjør du med Actions -> velg workflow -> Run workflow
