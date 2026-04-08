---
title: Paga el deute tècnic amb IA
date: 2026-03-13 15:55
status: published
description: Usa l'augment de productivitat de la IA per a pagar deute tècnic.
summary: El deute tècnic és allò que sabem que hem de canviar però que l'usuari no veu. En aquest article explico com, gràcies als agents de codi, vaig poder portar el nostre programari més antic —Mapping Tool— de Mac Intel a Apple Silicon, modernitzant dependències de fa més de 10 anys amb Codex i Claude, i sense comprometre el roadmap de l'empresa.
tags: AI, agents, deute tècnic, C++
---

Ja comentava a l'[article anterior](era-pogramari-personal.md) que l'economia de la programació ha canviat radicalment amb els agents de codi. I això també ha afectat el deute tècnic.

Definim el deute tècnic com tot allò que sabem que hem de canviar, que ens fa anar més lents, que augmenta la complexitat; però que l'usuari no veu, i per tant és difícil de justificar el temps que cal invertir-hi.

No em centraré en el deute tècnic avui (ja tinc un article a mitges sobre això). El que vull és parlar de com els agents de codi ens poden ajudar a pagar-lo, amb un exemple pràctic: portar el nostre programari més antic —[Mapping Tool](https://www.protopixel.io/product/mapping-tool)— de Mac Intel a Apple Silicon.

## El deute que vaig contraure

Durant el màster i el doctorat, m'interessava molt l'art digital i la programació creativa. El que estava de moda en aquells cercles era openFrameworks, un framework que feia fàcil la creació d'aplicacions interactives en C++. M'hi vaig llançar de cap: el feia servir en les pràctiques dels meus estudiants i en projectes del màster i del doctorat.

Quan vaig començar a treballar en el programari que més tard es convertiria en Mapping Tool, naturalment el vaig fer en c++ i openFrameworks. I en el moment va ser una bona elecció: ens va permetre crear ràpidament solucions que podíem iterar molt ràpidament.

I, de fet, per a poder iterar més ràpidament encara i fer-lo més flexible, hi vaig [encastar el runtime de python exposant-hi tot openFrameworks](https://github.com/chaosct/ofxPython). Així, els usuaris -nosaltres, en aquell moment- podíem crear nous continguts luminics interactius sense haver de tocar c++, de forma dinàmica.

En aquell moment no ho sabia, però acabava de contraure un deute tècnic que m'aniria perseguint durant els següents anys: la filosofia de openFrameworks era de trencar la seva API interna sense por, i jo em veia atrapat a una versió concreta d'openFrameworks, però no trencar tot el codi d'usuari que podia estar corrent a casa dels clients.

Per més complicació, openFrameworks venia amb una sèrie de llibreries de tercers pre-compilades, en versions específiques amb pedaços dels propis autors de oF. Només poder navegar la compatibilitat amb els canvis dels compiladors (com el position independent code a linux) ja era un maldecap: vam acabar mantenint un fork privat de oF on hi anàvem aplicant els pedaços que necessitàvem perquè el Mapping Tool seguís funcionant.

## No es pot tirar sempre la pilota endavant

A poc a poc, vam anar perdent l'habilitat de compilar Mapping tool en les nostres màquines personals: al principi per tenir versions massa noves del Sistema Operatiu, i després per tenir una arquitectura totalment diferent: Apple silicon, basada en ARM. Però a tot problema s'hi troba una solució, en el nostre cas, mantenir un mac mini antic amb mac intel com a builder.

I el que semblava simplement un inconvenient constant, però portable, es va convertir de cop en un gran problema: Apple va anunciar que deixaria de donar suport a mac intel. A partir d'algun release del proper any, el Mapping Tool no funcionaria a les màquines dels clients. I estavem atrapats amb un framework i llibreries de fa més de 10 anys, algunes discontinuades, sense suport per a un maquinari que encara no existia.

Així que ja teniem una data límit. Però podiem permetre'ns dedicar tant d'esforç a una cosa que no generava valor nou? Per als usuaris, que el programari segueixi funcionant és quelcom que es presuposa. No podíem tornar al cap d'un any dient "Us portem la nova versió de Mapping tool, amb exactament les mateixes capacitats i mancances, però que continua funcionant".

A més a més, per la situació de la companyia i el roadmap que havíem de tirar endavant, resultava clar que continuaríem tirant la pilota endavant fins a l'últim moment, tret que trobéssim una solució imaginativa que ens permetés d'avançar sense comprometre el nostre roadmap.

## Codex al rescat

Començo a investigar amb Codex quina seria la forma moderna de gestionar les llibreries. La idea era que si podia substituir les llibreries pre-compilades per altres que es poguessin compilar en ARM, podria compilar tot el binari per Apple Silicon. I per a fer-ho, necessitaria un sistema modern de gestió de dependències. Codex proposa conan, i en fem un petit PoC: passar una sola dependencia, una que havia introduit jo posteriorment i que coneixia bé, `pugixml` a conan.

Amb el PoC funcionant, li demano a Codex que faci una auditoria de totes les llibreries a substituir, i que creï un document amb tota la informació necessària per, a poc a poc, anar-les atacant d'una en una.

Amb el document de base, es tractava d'obrir una sessió de Codex, demanar que es llegís la documentació i que ataqués la substitució de la llibreria que li semblés més factible. I que apuntés tot el que canviava i havia après al mateix document. Aquest procés dura mesos, en els que vaig treballant entre tasques i fora d'hores. De vegades fent ssh des del mòbil a una màquina on tenia l'agent corrent, per a donar-li indicacions.

Algunes de les llibreries existeixen a conan amb la mateixa versió, algunes amb una versió posterior, i d'altres simplement ja no existeixen i han de ser substituïdes per d'altres. Tot això ho aconsegueix resoldre Codex.

Finalment, després de modernitzar totes les llibreries de base, sóc capaç d'intentar -i succeir- compilar el Mapping Tool per Apple Silicon.

## El que vaig fer era gairebé un Ralph Loop

Si heu estat atents a l'actualitat de IA, un [ralph loop](https://ghuntley.com/ralph/) justament fa això, però d'una forma una mica més autònoma. No és sorprenent que tothom vagi arribant a les mateixes conclusions sobre com operar amb agents de codi de forma efectiva: és molt important donar a l'agent de codi una forma de comprovar els resultats, de compilar i veure els errors. Així pot iterar sol molt millor i durant més temps.

Inicialment passava els errors manualment des del log del CI a Codex, però més tard vaig donar-li un script per a baixar-se tot el resultat de la compilació i trobar els logs del que havia fallat. Això va millorar bastant l'ergonomia.

## Claude és millor debugant

No tot ho va fer Codex. Claude va resoldre un problema de violació de segment a Linux. No era senzill, ja que usem tecnologia d'AppImage per empaquetar llibreries del sistema com glibc. Ho va fer entrant per SSH en un ordinador on fallava, per debugar-lo en remot. Vaig quedar genuïnament impressionat.

## Al final, pagar deute tècnic sí que tenia valor

Després de fer el port, la versió de Mapping Tool no només funciona fent el mateix. Només pel fet d'estar corrent de forma nativa, ja va molt més ràpid, amb guanys espectaculars. A més, ara hem recuperat la capacitat de fer profiling, i amb una sessió curta hem pogut optimitzar la càrrega de projectes. Entre els dos guanys, projectes que tardaven minuts en carregar, ara carreguen en escassos segons.

## Som massa productius

Si bé és cert que he pogut esquivar un gran problema gràcies a l'augment de productivitat que ens dónen els agents de codi i la IA en general, també ho és que això ens crea una pressió molt forta a ser més productius: quan cada minut compta de forma significativa, és molt difícil parar i no fer res.

Quan vaig impulsar el sistema de CI/CD intern per a compilar els productes (en aquell moment amb builds de 1 o 2 hores), sentia que si no estavem fent build tota l'estona - dia i nit - estavem perdent el temps. El mateix em passa ara: la pressió de "hauriem de tenir agents de codi treballant de forma continua dia i nit" és cada cop més present. La tinc i la llegeixo a gent del sector.

Perquè com em deien avui a l'oficina, el programari no s'acaba. Sempre hi ha coses per pulir, eines per fer, casos d'ús per descobrir. I **deute tècnic per pagar**.

En aquest món tan ràpidament canviant, almenys en aquest moment, estem tots en una espiral de productivitat que haurem d'aprendre a combatre i gestionar. I si ja és tot tant intens ara, imaginem-nos amb els avenços els propers mesos i anys i l'adveniment de la IAG...
