---
title: Parlem de complexitat, no de deute tècnic
date: 2026-04-21 00:00
status: published
description: Parlar de complexitat ens ajuda a pensar millor que usar la metàfora del deute tècnic
summary: La metàfora del deute tècnic porta associat un estigma de mala gestió que dificulta la comunicació amb equips no tècnics. Pensar en termes de complexitat — quelcom inevitable que s'acumula per causes sovint externes — ens permet raonar millor sobre el problema i justificar el temps necessari per abordar-lo.
tags: python, tooling, enginyeria
---

Fa poc més d'un any, estàvem fent un retir estratègic a l'empresa, i m'havia posat com a objectiu, garantir que tindríem temps i dedicació per a millorar el nostre codi. El que se'n diu pagar deute tècnic.

Tradicionalment, en la meva experiència, i pel que llegeixo en la de molta gent, el deute tècnic és molt difícil de gestionar:

- És difícil d'identificar
- És difícil de comptabilitzar
- És difícil de comunicar
- I per tant és difícil d'acomodar temps i esforç a reduir-lo.

Va coincidir que vaig llegir diversos articles (o veure vídeos - ja fa un any d'això) on parlaven d'un concepte diferent, la complexitat, que em va ajudar molt més a raonar sobre aquest tema i a comunicar-lo que no pas el concepte de deute tècnic.

Per això crec que és interessant deixar-ho clar i per escrit, per a mi i per a qui ho trobi.

## Les dificultats del concepte "deute tècnic"

D'alguna forma, si tens problemes per pagar un deute, se't mira com algú que no sap gestionar els seus diners. Hi ha un estigma associat al deute:

- poca planificació
- poca disciplina
- poca visió de futur
- ...

A més, la imatge mental que es té és que s'ha corregut massa i s'han fet les coses malament per arribar als terminis, i ara cal arreglar-ho.

Això fa que quan parles de deute tècnic, la gent ho vegi com un problema de gestió, i no com un problema tècnic. I això dificulta molt la comunicació amb altres departaments (producte, negoci, etc.) que no són tècnics.

Fins i tot es creu que és quelcom que l'equip tècnic ha de resoldre per si mateix, sense ajuda de ningú més, com quelcom que han d'arreglar per que no han fet bé la seva feina abans, com a penyora.

I de fet no és així. Hi ha molts motius per l'acumulació de deute tècnic. Moltes vegades per causes no pròpiament tècniques, com la impossibilitat de conèixer el problema i el mercat, a priori:

- el problema original ha canviat i ara és un altre
- les prioritats eren diferents
- el mercat ha canviat
- l'equip ha canviat
- les eines han canviat
- etc

Però tot això sembla simplement una llista d'excuses per no haver fet bé la feina. I aquí entra el concepte de complexitat.

## Pensar en termes de complexitat

Deixem de classificar el codi en bo o dolent: no usem metàfores de deute. Hi ha codi, i en principi fa el que ha de fer.

Volem que faci també alguna altra cosa? Afegim més codi. Segurament canviem una mica el codi existent per a acomodar el codi nou. Ostres!, abans aquesta abstracció pressuposava quelcom que ara ja no és cert: cal canviar tots els llocs on s'usava. Com ho testejo, això? Mirem com ho hem solucionat en altres tests... I aquest problema justament el podríem solucionar amb la nova versió de la llibreria, però, si l'actualitzo, trencaré alguna cosa?

La complexitat ens fa anar més lents per què ens costa més raonar sobre els canvis que estem introduint. Si som capaços de mantenir-ho tot alhora en el nostre cap, podem prendre decisions molt més fàcilment, però si no podem, cada canvi es converteix en una exploració i redescobriment.

Eventualment, tot projecte de programari acaba recordant l'escena famosa de Malcom In the Middle:

https://www.youtube.com/watch?v=AbSehcT19u0

## Al nostre equip li costava progressar

I és que justament això és el que ens estava passant. Constantment se'ns preguntava com ens podien costar tant les coses. Durant l'any anterior havíem estat dedicant molt de temps a una app mòbil, que semblava encallar-se constantment. El que funcionava una setmana ho deixava de fer la següent.

**Havíem arribat al límit de la complexitat que qualsevol membre de l'equip podia mantenir dins el seu cap**.

Però era molt difícil d'entendre des de fora de l'equip. Com podia ser tan complicat tot? Al final *no semblava pas que el problema que estàvem solucionant fos tan complicat*.

I aquí estava una mica el quid de la qüestió.

## No tota la complexitat és igual

Hi ha complexitat que és inherent al problema que intentem solucionar. Que correspon a l'àmbit de negoci, a la realitat. Aquesta és innegociable: És la **complexitat essencial**. Simplificar aquí seria perdre detall del problema i no seríem capaços de solucionar-lo correctament.

En canvi, hi ha complexitat que no correspon al problema en si: la **complexitat accidental**. Aquesta correspon a tot allò que no és el problema en si que volem solucionar:

- sistema de build complex
- eines massa complexes o desconegudes
- base del codi que ha canviat durant el temps i és difícil de llegir
- documentació que ha quedat obsoleta
- aquella feature que es va fer a correcuita i és massa enrevessada
- la mescla de llenguatges de programació, frameworks, llibreries i versions
- ...

> Aquesta distinció entre complexitat essencial i accidental la va formular Fred Brooks al seu assaig clàssic [*No Silver Bullet*](https://en.wikipedia.org/wiki/No_Silver_Bullet) (1986), on argumentava que no hi ha cap avenç tecnològic capaç de reduir la complexitat essencial d'un problema.

I és que amb un projecte d'una dècada de durada, es podia veure la història i l'acumulació de mil cosetes que ho feien tot molt complex.

## Per què acumulem complexitat

Ningú té com a objectiu augmentar la complexitat accidental, és més, la complexitat, a l'hora d'introduir-la, mai sembla accidental. És quelcom que passa de forma orgànica: el cert és que en el moment d'afegir complexitat estem solucionant problemes reals que tenim al projecte, i per això no ens n'adonem.

Tal com passava amb la dificultat d'avenç de l'equip, a escala individual tota persona **té un màxim nivell de complexitat que pot mantenir al seu cap**. Si la complexitat del projecte n'és inferior, té un espai de complexitat vacant. Aquesta complexitat vacant és la moneda corrent que usem per a crear features i afegir coses.

**No és bo ni dolent, és la forma en què funciona**: mentre hi hagi espai, l'anirem ocupant. Al principi, com més espai tinguem vacant de complexitat, més ràpid anirem afegint coses i fent canvis, i això és molt valuós. Però a mesura que anem omplint tot l'espai disponible, trobar racons costa molt més.

Eventualment, quan la complexitat del projecte excedeix la capacitat de la persona, li és impossible de raonar amb claredat, i això fa que sigui quasi impossible avançar, amb perill d'acabar en un punt de no retorn, on no hi ha prou espai ni per a _desfragmentar_ la complexitat existent.

## Com ho podem solucionar?

- més gent?

No serveix de res. La complexitat ens fa la punyeta de forma individual.

- gent més capaç?

Podria semblar bona idea, però és encara pitjor. Gent més capaç pot tenir un límit més gran de suportar complexitat, però això només vol dir que seran capaços d'augmentar-la més, perjudicant encara més la resta de l'equip, que es veurà desbordat.

- separant els problemes

Una possible forma és aquesta: divideix el que fas en dues o més parts independents. Això ajudarà molt si ho pots fer, però si ho pots fer potser és una mala senyal: per què la teva organització està fent dues coses totalment diferents? Segur que no estan relacionades?

> Aquest mètode era popular durant l'auge dels microserveis: solució que va néixer per a solucionar un altre problema —l'escalabilitat de serveis gegantins de núvol— que, a més, quasi ningú no tenia. Però cada part no és al final totalment independent de les altres, obligant-se a dissenyar, negociar, mantenir, comunicar i documentar tots els punts de contacte. Suposo que si tens un exèrcit d'enginyers a la teva disposició, pot ser una opció.

- **reduir complexitat!**

Al final, l'única sortida és **simplificar**. Això ho podem fer de vàries formes:

- usant menys eines, més simples i més estàndards.
- fent refactors de codi que eliminin excepcions i simplifiquin codi.
- usant blocs de construcció que facin més coses (llibreries, frameworks) o transformant codi propi en blocs de construcció ben definits.

## I, al final, explica, com va anar?

Al final, amb l'explicació de la complexitat, vaig poder definir objectius de producte de reducció complexitat, per garantir poder tenir temps per a treballar-hi. Cada setmana teníem una reunió on ens preguntàvem què era el que ens frenava, per què anàvem lents. I fèiem una llista de les coses que volíem canviar.

Després prioritzàvem aquesta llista amb una taula [RICE](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) i a cada Sprint proposàvem d'atacar algun ítem de la llista de les primeres posicions. Una de les coses més grans que vam fer va ser fer la transició de [Bazel](https://bazel.build/) a un monorepo organitzat amb [uv](https://docs.astral.sh/uv/) i [pnpm](https://pnpm.io/), ja que, al final, tenir shell scripts coordinant les eines de build tenia menys complexitat que **entendre** Bazel i mantenir-lo...

Finalment, vam poder recuperar les regnes del projecte. Vam sortir de l'espiral en la que ens trobàvem.

## Té sentit tot això en l'era de la IA?

La IA ens ajuda a operar en una complexitat molt major a la que teníem fins ara. Llavors, ens hem de preocupar de reduir la complexitat, realment?

Ja escrivia anteriorment que podem [pagar el deute tècnic amb la ia](paga-el-deute-tecnic-ia.md), i així ho hem de fer! I de fet no només ho hem de fer per a nosaltres, sinó també per a la IA!

**La IA té el mateix problema que nosaltres en termes de límit de complexitat**, i hem d'estar vigilants que no se'ns en vagi de les mans, per què llavors ens serà molt més difícil sortir a rescatar la IA d'aquesta nova complexitat que va més enllà dels nostres límits.

Així que la meva recomanació més recent és fer cas de l'olfacte: cada vegada que veiem quelcom que fa mala olor, cada vegada que ens diem a nosaltres mateixos "això hauria de ser una llibreria genèrica" o "tots aquests warnings ens petaran als nassos en algun moment", afegir-ho a una llista. I constantment treballar per reduir aquesta llista amb l'ajuda de la IA, en background.

Per què realment la IA ens accelera, i sembla ser molt més ràpida que nosaltres en afegir complexitat accidental, si no la lliguem curt, si no som exigents i perfeccionistes.
