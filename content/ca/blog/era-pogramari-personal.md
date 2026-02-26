---
title: L'era del programari personal
date: 2026-01-25 00:00
status: published
description: Els agents de codi ens han arrossegat de cop a una nova era on el programari és tant barat que tothom el tindrà personalitzat.
summary: "Els agents de codi han canviat l'economia del programari: crear eines ad-hoc, personalitzar projectes open source o automatitzar tasques que abans no valien la pena ja és trivial. En aquest article repasso diversos exemples pràctics d'eines que he creat o modificat amb agents, des d'automatitzacions d'onboarding fins a personalitzar programari en Rust sense saber-ne."
tags: [AI, agents, programari]
---

# L'era del programari personal

Portem una progressió d'eines molt interessant l'últim any. Primer, amb agents de langchain s'intentava el que claude code va ser el primer a aconseguir: la combinació de tools amb LLMs, amb un loop d'acció i test. Aquest 2026 tot s'està accelerant amb Ralph loops i clawdbot.

El programari s'està abaratint a xarxes forçaces i, tot i les seves limitacions, hi ha molts casos d'ús on de cop l'economia de la progamació ha quedat trastocada.

No tinc temps, ni l'habilitat, per a fer una disetació d'on ens porta tot això, però puc donar cinc centims de coses que he aconseguit fent servir agents de codi que no hagués pogut fer abans.

## Automatitxació del *long tail*

L'economia de l'automatització estava perfectament capturada per la clàssica vinyeta de XKCD:

![XKCD 1205: is it worth the time?](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

El primer cop que vaig veure aquesta vinyeta, em va quedat gravada a la retina. I he intentat no caure al forat negre de crerar codi per a automatitzar coses per a tasques que no tenen un retorn positiu en temps. Aquesta graella ja no té sentit: crear programari és tant barat (en temps) que gairebé qualsevol cosa es pot automatitzar.

### Eines d'Onboarding i offboarding

He creat un parell d'eines per a fer onboqarding i offboarding. Backups de dades de google workspace i després pujar-ho en una unitat compartida de drive? Fet! Crear els comptes nous a les diferents plataformes i assignar-los els permisos? Fet! Crear un informe amb tot el procés? Fet!

## Eines d'un sol ús

El mateix passa amb tasques que vols automatitzar **un sol cop**.
He creat tot un programari ad-hoc per a transformar **un** informe en markdown a PDF. Demanant coses extranyes, Etiquetes de colors, index maco... Ha funcionat perfectament i després d'aquest sol ús, no el faré servir mai més. Però no hauria fet manualment, no m'hauria valgut la pena.

## Personalització de programari existent

Un dels casos d'ús més interessants. Baixa't el codi d'un repo de github, demana modificacións i úsa'l. No cal ni publicar-lo.

### Tukai: aprendre tipografia

Aquest any me n'he adonat que amb els agents de codi el coll d'ampolla del desenvolupament passava a ser la velocitat amb la que podia escriure a màquina. En tants anys de dedicació a aquest aprofessió això no m'havia passat mai, normalment dedicava més temps a pensar que en escriure.

Així que, a la meva edat, em vaig posar a aprendre tipografia. I necessitava un programa per a practicar que a més funcionés en local, per a fer-lo servir en els meus viatges en tren. Vaig trobar [Tukai](https://github.com/hlsxx/tukai) i em va agradar. La pega: ni tenia llista de paraules en català.

Amb claude code (o codex, no ho recordo) en un tres i no res hem afegit diversos diccionaris en català pels diferents nivells d'aprenentatge, basats en les paraules més freqüents de la Viquipèdia, i amb presència equilibrada de totes les lletres.

### Claude Code Sleep preventer

Una cosa que em fa molta ràbia del macbook és la com d'agressiu és posant-se en repòs a la mínima que pot. I quan fas servir un agent de codi, aquest tema esdevé un problema.

Aparentment [Claude Code Sleep Preventer](https://github.com/CharlonTank/claude-code-sleep-preventer) fa exactament això, però: O forks, 0 estrelles! Així que he baixat el codi i li he fet fer una auditoria al claude code.

Aquest ja m'ha revelat una sorpresa: aparentment el programari també transcriu la veuquan li demanes que ho faci, i per a fer-ho necessita baixar i executar un model en local (whisper) de més de centenars de megues. A part d'això, el programari no sembla maliciós.

Així que amb 5 minuts de modificacions amb claude code, ja el tinc instal·lat, sense la part de transcripció de veu, i funcionant.

I tot aixpo en rust, que ni domino ni casi sé llegir!

## Jugant amb clawdbot

L'exemple més radical que he pogut experimentar és el del clawdbot. Quan vaig descobrir què era, una espècie de claude code universal que es pot fer servir com assistent personal, el vaig instal·lar: realment necessito un assistent personal.

El cas és que si li demanes si pot fer tal o qual cosa, et pot dir quelcom en la linia de: no ho puc fer, però puc programar-me un plugin per a fer-ho. I ho fa! El propi programa-assistent es crea les seves pròpies extensions. En el meu cas, volia processar informació de Notion, i pocs minuts més tard ja en podia llegir i escriure articles.

## Conclusions

Entrem en una etapa fascinant de la creació de programari. No en tinc ni idea de com serà el futur però el que sí que sé és que l'era de programes fixes, que no evolucionen, de tasques manuals acomplertes en solitari, s'ha acabat. I entrem en l'era del programari. Del programari barat i omnipresent.
