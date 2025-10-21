# Dokumentasjon for Skogstua
Dette repoet inneholder dokumentasjonen for Skogstua fellesverksted, drevet av foreningen Tromsøskapere.

Hver gang en fil endres/slettes/legges til kjører Github en "action" som oversetter filene til en statisk webside. Denne ligger på https://tromsoskapere.github.io/mkdocs-skogstua/ **<-Husk å oppdater denne**

Dette repoet er bygd opp av /docs/ som inneholder mappene og filene som utgjør hver enkelt web-side. Mappestrukturen danner hierarkiet for menyene og innholdet på siden. mkdocs.yml i rotmappen er instillingene til siden, og ./github/workflows/ci.yml er workflowen for action'en som lager pages. Innstillingene for pages ligger på Settings->Pages.
