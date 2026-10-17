# Ha guanyat la segona millor solució — notes

Estat: material de treball d’un article en esborrany, fora del contingut publicable.

## Criteri de treball

- Document de notes, no esborrany de l'article.
- Conservar les idees, els fets i els matisos aportats durant el dictat.
- Organitzar la informació principalment en punts breus.
- Distingir entre:
  - informació aportada per l'autor;
  - informació contrastada amb fonts externes;
  - interpretacions o hipòtesis;
  - dubtes, llacunes i elements pendents de verificar.
- No convertir les notes en prosa final sense una petició explícita.

## Fragments del dictat

<!-- Registre acumulatiu del contingut aportat, preservant-ne el sentit. -->

### Fragment 1 — detonant d'actualitat i pregunta central

- L'article parteix d'un fet d'actualitat: un descobriment o una refutació relacionats amb el problema del mil·lenni de Navier–Stokes, atribuïts inicialment a OpenAI.
- Aquest fet convida a pensar en el futur de la recerca.
- Pregunta principal: la recerca —en matemàtiques o en qualsevol altre camp— es desplaçarà de les institucions tradicionals, com les universitats, cap a empreses privades?
- L'autor aportarà després experiències i antecedents personals que ja l'havien portat a pensar en aquesta qüestió.

### Fragment 2 — formació acadèmica i posició inicial sobre el *machine learning*

- El *background* i la carrera acadèmica de l'autor se situen en la interacció persona-ordinador.
- Especialització concreta en la vessant més tangible de la disciplina: interacció tangible i interfícies tangibles.
- Una part important de la recerca —o, més precisament en aquest cas, del desenvolupament— es va centrar en la detecció de gestos.
- En aquell moment, l'autor mantenia una posició molt contrària al *machine learning*.
- Convicció metodològica inicial: sempre era molt preferible trobar una solució completament analítica.

### Fragment 3 — el boom del *machine learning* i el cas dels directors d'orquestra

- Aquesta etapa va coincidir amb un boom del *machine learning* al departament i, concretament, al Music Technology Group (MTG) de la Universitat Pompeu Fabra.
- En l'àmbit de l'àudio i la música s'hi incorporaven moltes tècniques d'aprenentatge automàtic:
  - tècniques traslladades des d'altres camps, com el processament d'imatges;
  - tècniques pròpies o adaptades específicament a l'àudio i la música.
- Era una explosió de noves aplicacions i constituïa la tendència dominant del moment, però no acabava de convèncer l'autor.
- Formulació de l'autor en aquella època: les solucions de *machine learning* eren «la segona millor solució de tot».
  - Podien aproximar pràcticament qualsevol cosa.
  - Precisament perquè l'aproximaven, no oferien la certesa d'una solució purament analítica.
  - Una solució analítica permetia saber amb certesa si un esdeveniment o un gest s'havia produït o no.
- Cas concret de recerca: reconeixement dels gestos dels directors d'orquestra fets amb la batuta o amb la mà.
- Mètode de treball de l'autor:
  - observar i analitzar personalment la forma del gest;
  - intentar entendre'n la intenció;
  - descompondre el moviment de la mà o la batuta;
  - identificar una seqüència explícita de condicions: si passen A, B, C i D en aquest ordre, es tracta d'un tipus determinat de gest.
- Fer servir *machine learning* per resoldre aquest reconeixement li semblava, d'alguna manera, «fer trampa».
- A més del desacord conceptual, l'aprenentatge automàtic podia introduir problemes o comportaments que no s'havien anticipat.
- Exemple contemporani que queda obert: Microsoft Kinect, la imatge de profunditat i un classificador relacionat amb la detecció o identificació de les mans o de parts del cos.

### Fragment 4 — Kinect, persones esquerranes i una drecera inesperada

- L'exemple del Kinect era rellevant per una dificultat descrita en un escrit tècnic sobre el desenvolupament del sistema.
- Funcionament físic recordat per l'autor:
  - una càmera o sensor d'infraroig;
  - al costat, un projector que emet un patró de punts infrarojos;
  - la diferència entre el patró projectat i el capturat permet calcular la profunditat;
  - com que projector i càmera ocupen posicions diferents, les oclusions o «ombres» apareixen sistemàticament cap a un costat.
- Segons el record de l'autor, el classificador s'havia entrenat amb imatges de mans i del cos, principalment o exclusivament de persones dretanes.
- En començar les proves amb persones externes, el sistema no funcionava amb persones esquerranes.
- Explicació recordada: l'ombra apareixia invertida i el model l'havia incorporada, sense que els desenvolupadors ho pretenguessin, com una característica per decidir:
  - si l'objecte era una mà;
  - quina postura tenia la mà.
- Aquesta ombra no era una característica necessària ni semànticament rellevant per entendre la mà; era un artefacte del sistema de captura.
- L'exemple va contribuir a formar la visió crítica de l'autor sobre el *machine learning*: un model pot arribar a la resposta mitjançant indicis que el dissenyador no havia previst i que no representen el fenomen que es vol comprendre.

### Fragment 5 — exclusió deliberada del *machine learning* de la tesi i visita australiana

- Al llarg de pràcticament tota la tesi doctoral, l'autor no va utilitzar *machine learning* ni mètodes semblants.
- Aquesta absència va ser gairebé voluntària: responia a una elecció metodològica, no només a una falta d'oportunitat o de coneixement.
- Sí que va experimentar puntualment amb algunes eines:
  - programari relativament agnòstic respecte del tipus de dades;
  - possibilitat de redirigir-hi senyals d'entrada;
  - etiquetatge manual d'algunes postures;
  - aprenentatge posterior d'aquestes postures per part del sistema.
- Tot i aquesta experimentació, l'enfocament li plantejava un «problema de puresa» metodològica.
- En aquella època, un investigador principal d'una universitat australiana va visitar el despatx o grup amb la intenció de fer contacte i explicar la seva recerca.
- Aquest investigador va parlar del projecte d'un doctorand seu que estava acabant la tesi doctoral.
- Record provisional del projecte del doctorand:
  - sistema de reconeixement de la posició o dels gestos de les mans;
  - objectiu de reconstruir les mans en 3D davant d'una càmera convencional;
  - l'autor adverteix que pot estar barrejant aquest projecte amb un altre.
- El relat sobre aquesta visita continua en el fragment següent; encara no se n'ha d'extreure cap conclusió.

### Fragment 6 — una tesi avançada per una startup i retorn al present

- El doctorand de l'investigador visitant estava a punt d'acabar la tesi i havia fet, segons el relat, una feina molt bona.
- El sistema podia estimar o reconstruir la posició 3D de la mà a partir d'una sola imatge.
- Record tècnic, encara incert:
  - ús d'un guant amb diferents colors per identificar diverses parts de la mà;
  - càmera convencional;
  - reconstrucció de la postura tridimensional;
  - rendiment aproximat recordat d'uns cinc fotogrames per segon.
- Just abans de la defensa de la tesi es va anunciar un dispositiu comercial, de nom recordat vagament com «NUI» o semblant.
- El dispositiu permetia posar la mà a sobre del sensor i reconstruir-la en 3D amb facilitat i a una velocitat molt superior.
- Reflexió que en va fer l'investigador principal:
  - quina posició ocupen les universitats quan la innovació ja no es produeix principalment dins seu?
  - un doctorand o un grup acadèmic petit no pot competir amb startups que disposen de milions d'inversió;
  - una empresa pot presentar sobtadament un producte que deixa molt enrere anys de treball doctoral, fins i tot si aquell treball era bo i rigorós.
- Aquesta experiència torna a la memòria de l'autor arran del cas d'OpenAI i Navier–Stokes.
- Revisió de la posició inicial sobre el *machine learning*:
  - l'autor creu, des de fa temps, que estava equivocat;
  - havia pensat en una escala massa petita;
  - comparava sistemes petits, amb poques dades i entrenaments limitats;
  - no havia projectat què podia passar amb models, conjunts de dades i pressupostos d'entrenament molt més grans;
  - el funcionament actual de la IA li hauria semblat totalment irreal deu anys abans.
- Les grans empreses poden avançar la ciència fora de l'acadèmia, encara que una part de la motivació sigui propagandística o comercial.
- Risc associat: es poden produir resultats científics sense construir al mateix ritme la comprensió humana, els experts i els camins pedagògics que hi condueixen.
- Record de la reflexió recent de Terence Tao:
  - si grans col·lectius d'agents d'IA fan avançar el coneixement matemàtic, es poden generar moltes proves o resultats;
  - la comunitat humana pot no tenir temps o capacitat per digerir-los;
  - poden quedar «forats» de comprensió, àrees sense experts humans capaços d'explicar com s'hi ha arribat o d'integrar el resultat en una teoria compartida.
- L'arc irònic o significatiu de l'experiència personal:
  - primer, considerar el *machine learning* una moda o una solució inferior;
  - després, observar que la combinació de *machine learning*, grans conjunts de dades, capital i infraestructura permet a les empreses superar la capacitat de l'acadèmia.
- Connexió amb el futur de les professions i de la recerca:
  - si avançar en un camp exigeix gastar milions de dòlars només en inferència, només les grans empreses podran fer determinats experiments;
  - doctorands, investigadors i grups sense grans pressupostos en quedaran exclosos;
  - el problema s'agreuja en àrees sense un retorn econòmic evident que justifiqui una inversió privada tan gran.

### Fragment 7 — final de l'etapa analítica i arribada de la IA generativa

- El canvi d'opinió sobre el *machine learning* no va ser una evolució contínua ni una conversió provocada per un únic esdeveniment.
- Durant molt de temps, després de la tesi, l'autor pràcticament no va pensar en la qüestió.
- Conclusió retrospectiva principal sobre la tesi doctoral i les interfícies tangibles:
  - les interfícies tangibles van néixer en una època en què encara no hi havia prou capacitat, eines ni conceptes per fer-les realment útils;
  - la tesi de l'autor se situa al final d'aquell període;
  - malgrat la voluntat de fer-les útils, el seu moment d'interès central ja havia passat;
  - l'atenció tecnològica començava a desplaçar-se cap al paradigma *multitouch*, que durant molt de temps havia estat estretament relacionat amb les interfícies tangibles.
- Sensació personal en acabar la tesi: haver arribat tard a l'onada de les interfícies tangibles.
- Aquesta experiència va donar a l'autor una perspectiva cíclica sobre les tecnologies:
  - una tecnologia pot semblar esgotada o morta i tornar quan les condicions materials i conceptuals són adequades;
  - paral·lel amb la primera onada de realitat virtual, que havia semblat completament morta abans d'una nova explosió pocs anys després de la tesi;
  - les interfícies tangibles podien haver estat igualment una primera onada prematura.
- La interacció tangible, almenys tal com es treballava al grup, seguia un enfocament essencialment analític:
  - regles explícites per interpretar què significava moure un objecte;
  - regles per acostar-lo, allunyar-lo o fer-lo rotar;
  - correspondències definides entre acció física i comportament del sistema;
  - no semblava un camp que es pogués abordar fàcilment amb *machine learning*.
- Al final de la tesi, l'autor accepta simbòlicament el fracàs o l'esgotament de l'enfocament analític davant del *machine learning*.
- Sentiment d'aquell moment: «sóc l'últim» que afronta aquests problemes d'aquesta manera.
- El nou enfocament no guanyava necessàriament perquè oferís la solució més elegant, pura o exacta, sinó perquè funcionava millor a la pràctica.
- Reformulació de «la segona millor solució de tot»:
  - no val la pena invertir tot l'esforç necessari per arribar a la millor solució analítica si una solució apresa, teòricament segona, ja funciona prou bé;
  - l'avantatge decisiu pot ser assolir fàcilment una solució útil i general, no trobar la solució òptima per a cada cas.
- Després de deixar l'acadèmia i passar a l'empresa, la qüestió queda en suspens durant una etapa.
- La percepció canvia amb la nova onada d'intel·ligència artificial i, particularment, amb aplicacions generatives:
  - *inpainting*;
  - transferència de textures o d'estil;
  - DeepDream de Google;
  - primers *transformers* i interfícies conversacionals.
- Aquestes aplicacions mostren una capacitat qualitativament diferent de la simple classificació o de l'aprenentatge d'una tasca concreta: el sistema pot generar.
- El caràcter generatiu convenç l'autor que la tecnologia té una utilitat i un potencial nous.
- Projecte intern anomenat provisionalment **Product Pixel** —nom pendent de confirmar— que no es va arribar a publicar o llançar:
  - intentava imaginar com seria el futur aprofitant aquestes noves tecnologies;
  - llegit avui resulta premonitori en diversos aspectes;
  - anticipava interfícies conversacionals;
  - anticipava la generació de contingut;
  - proposava passar de la declaració explícita o construcció manual al control o direcció de la generació.
- La direcció del projecte només s'entén per la influència de la nova onada d'IA que començava a entrar en productes i interfícies.
- Situació actual: la utilitat de la IA ja no sembla discutible; la pregunta s'ha desplaçat cap als seus efectes, l'escala i qui controla la capacitat de fer recerca amb aquestes eines.

### Fragment 8 — epicicles com a imatge de l'aproximació universal

- Per explicar què entenia per una solució «millor», l'autor proposa una analogia amb la història de l'astronomia.
- Imatge mental de l'autor:
  - el model geocèntric podia ajustar el moviment observat dels astres afegint successivament rodes sobre rodes;
  - aquest mecanisme podia refinar-se amb més termes per aproximar les observacions cada vegada millor;
  - la construcció recorda conceptualment una sèrie o transformada de Fourier: una combinació de components simples capaç d'aproximar una trajectòria complexa;
  - davant d'això, una llei analítica adequada encaixa les dades històriques amb una estructura molt més simple i permet predir amb precisió.
- El nom que l'autor intentava recordar és el sistema d'**epicicles i deferents** associat al model ptolemaic; també hi intervenien excèntriques i l'*equant*.
- En la concepció que l'autor tenia durant la tesi, el *machine learning* s'assemblava als epicicles:
  - era una mena d'aproximador universal;
  - se'n podia augmentar arbitràriament la precisió afegint dades, complexitat o termes;
  - malgrat això, continuava sent una aproximació i no la descripció exacta del mecanisme.
- La solució analítica representava, en canvi, la llei subjacent:
  - exacta per definició dins del model;
  - compacta;
  - capaç d'explicar i predir;
  - no limitada a reproduir les observacions disponibles.
- Matís històric per a una futura redacció:
  - Copèrnic va canviar el centre del sistema i va explicar el moviment retrògrad com un efecte aparent, però encara va conservar epicicles;
  - Kepler va substituir les trajectòries circulars i els epicicles per òrbites el·líptiques i va formular lleis precises del moviment planetari;
  - Newton va aportar posteriorment una explicació dinàmica unificada mitjançant les lleis del moviment i la gravitació;
  - per tant, l'analogia més precisa és «epicicles ptolemaics/copernicans versus Kepler i Newton», no simplement «Copèrnic versus Ptolemeu».

### Fragment 9 — exactitud, aproximació i problemes que admeten ambigüitat

- L'autor continua pensant que hi ha molts problemes amb una solució analítica absolutament precisa i que aquestes solucions tenen un valor molt gran.
- El canvi de posició no consisteix a negar l'exactitud ni la possibilitat de definir determinats problemes de manera estricta.
- El matís adquirit amb el temps és que també hi ha molts problemes que no tenen una resposta absolutament precisa:
  - són massa complexos;
  - poden estar insuficientment definits;
  - incorporen context, interpretació o ambigüitat;
  - en aquests casos, el que importa és obtenir una aproximació útil.
- Moltes aplicacions actuals de la intel·ligència artificial no busquen una resposta exacta, sinó una resposta «direccionalment correcta».
- «Direccionalment correcta»:
  - no garanteix el resultat perfecte o únic;
  - situa l'usuari o el procés en una zona útil de l'espai de solucions;
  - sovint n'hi ha prou per complir l'objectiu pràctic.
- Aquesta tolerància a l'aproximació no és aliena a la intel·ligència humana: les persones també operen habitualment amb interpretacions, heurístiques, context i respostes prou bones.
- El *machine learning* té una aplicació especialment bona quan coincideixen:
  - un model prou bo;
  - un problema difícil de definir exhaustivament;
  - un domini que tolera l'ambigüitat;
  - un criteri d'èxit pràctic que no exigeix certesa absoluta.
- Posició actual de l'autor:
  - preservar les solucions estrictes allà on el problema les permet i són valuoses;
  - acceptar l'aproximació allà on la naturalesa del problema fa més important la utilitat, la direcció o l'adequació contextual que no pas l'exactitud absoluta.

### Fragment 10 — acotació cronològica de la tesi, els gestos i la visita

- L'autor va presentar la tesi doctoral el 2014.
- El treball sobre reconeixement de gestos de directors d'orquestra se situa probablement entre 2012 i 2013.
- La visita de l'investigador que va parlar del projecte del doctorand va tenir lloc aproximadament en la mateixa etapa.
- L'autor considera més probable que la visita fos el 2012 que no pas el 2013.
- Les dates del treball de gestos i de la visita són aproximades i s'han de conservar com a records, no com a dates documentades definitivament.

### Fragment 11 — vinculació del treball de gestos amb la tesi i un projecte europeu

- L'autor confirma que el treball sobre reconeixement de gestos de directors d'orquestra formava part directament de la seva tesi doctoral.
- El treball també s'emmarcava en un projecte europeu que recorda provisionalment amb el nom «Fènix»; el nom exacte i la grafia queden pendents de confirmar.
- L'autor indica que la tesi hauria de contenir les referències necessàries per documentar el projecte i el treball de gestos.
- Ara mateix no té la tesi ni la documentació a mà i no sap on localitzar-les; les buscarà més endavant per completar les referències.
- La vinculació amb la tesi és una confirmació personal de l'autor; la identificació del projecte europeu i les referències bibliogràfiques encara no s'han contrastat documentalment.

### Fragment 12 — documentació dels gestos i enriquiment de l'experiència dels concerts

- Finalitat del sistema de gestos, segons l'autor: documentar els gestos dels directors d'orquestra, enregistrar-los i etiquetar-los per poder-ne extreure informació.
- Les converses amb directors d'orquestra havien permès distingir:
  - gestos més o menys estàndards, que l'autor associa sobretot al context dels assajos;
  - gestos més diversos i expressius, que traslladen al moviment l'emoció que es vol transmetre amb la música.
- L'autor destaca l'interès d'aquesta traducció de la intenció emocional a moviment corporal.
- L'abast concret del treball era identificar i etiquetar els gestos per poder-los correlacionar amb altres elements o dades.
- En aquell treball no s'havia definit una pregunta d'estudi posterior concreta per a les dades recollides; no s'ha de presentar com un sistema que interpretava automàticament l'emoció ni com un mecanisme de control musical.
- [Record provisional de l'autor] L'objectiu més ampli del projecte europeu era «augmentar» els concerts de música clàssica, en el sentit d'enriquir l'experiència del públic.
- Exemple recordat d'aquesta experiència: els assistents podrien utilitzar una tauleta o un dispositiu semblant durant el concert per rebre explicacions sobre la música, els detalls i els moviments.
- La relació exacta entre les etiquetes de gestos i les explicacions al públic no queda especificada; tampoc no s'ha confirmat documentalment l'abast del projecte europeu.

### Fragment 13 — límit del record i pausa en l'exploració del projecte de gestos

- L'autor no recorda si el treball va arribar prou lluny per fer una anàlisi semàntica dels gestos; no s'ha de donar per fet que aquesta anàlisi es fes.
- El text del treball es conserva com un capítol de la tesi doctoral.
- L'autor prefereix no aprofundir més ara en aquest projecte concret.
- Decisió per a l'entrevista: deixar en pausa les preguntes de detall sobre aquest projecte fins a recuperar el capítol de la tesi; aleshores es podran completar els buits amb documentació.
- Continuar l'entrevista pels altres fils de l'article, sense exigir que l'autor reconstrueixi ara aquests detalls de memòria.

### Fragment 14 — observació del desplaçament de la recerca i accés als recursos

- L'autor precisa que el desplaçament de la recerca cap a empreses no li generava especialment por o preocupació: era sobretot una observació. Cal corregir qualsevol enfocament de l'entrevista que pressuposi una denúncia o una pèrdua que l'autor vulgui defensar.
- [Percepció de l'autor sobre l'acadèmia] Les coses van molt lentes i sovint es confon voler fer recerca amb aconseguir mantenir l'activitat acadèmica.
- Es dedica molt de temps a obtenir finançament i a fer encaixar projectes; les línies de recerca s'acaben configurant segons el finançament i l'encaix entre els diferents participants del projecte.
- L'autor considera natural que una empresa acumuli recursos i capacitat per avançar en una tecnologia o un camp de recerca quan s'hi entreveu una aplicació pràctica.
- Distinció percebuda entre dues formes de treballar:
  - a l'acadèmia, avançar publicant, discutint i presentant resultats;
  - a l'empresa, avançar amb més aïllament, de manera que investigadors externs no es poden recolzar igualment en aquell treball per progressar. [Matís posterior, fragment 16] L'autor observa publicació i mobilitat entre els laboratoris d'IA actuals, amb una pol·linització creuada important.
- Des de feia temps, l'autor tampoc no considerava necessària o definitivament consolidada la unió de recerca i educació dins de les universitats. És una organització que ha funcionat, però podria canviar en el futur sense que això sigui necessàriament un problema.
- L'autor situa aquesta reflexió sobre recerca i educació fora del tema principal de l'article; no desenvolupar-la com una tesi central.
- No hi ha una valoració global de progrés o pèrdua: alguns aspectes poden millorar i altres empitjorar.
- La sensació personal més propera és «quina llàstima»: voler treballar en un camp de recerca i trobar-se molt més limitat si no es forma part d'una empresa que hi dedica prou recursos.
- Les empreses han d'investigar en àmbits on esperen retorn; això deixa una funció per a la universitat i pot donar lloc a una divisió entre actors que no és necessàriament problemàtica.
- Observació central: en determinats camps amb aplicació pràctica, la recerca es desplaça cap a grans empreses o empreses amb finançament important capaces de concentrar-se en aquells problemes.
- Conseqüència per a l'investigador que en queda fora: «si estaves fora, estaves fora». El nucli és l'accés efectiu a la capacitat de fer recerca en aquell camp, no una por general a l'empresa privada.

### Fragment 15 — pressupost, intel·ligència com a recurs i incentius de la recerca

- L'autor veu la situació actual com un aprofundiment del mateix procés, ara molt més directe i evident: la recerca independent, oberta o pública pot quedar en segon terme davant d'entitats amb molt més pressupost.
- [Interpretació de l'autor] La relació entre tenir més pressupost i poder avançar més en recerca es fa més directa amb la IA.
- Abans era especialment important atraure talent humà concret. Si una part d'aquesta capacitat es pot obtenir mitjançant models d'IA, el pressupost i la computació esdevenen restriccions més determinants.
- L'autor no nega la necessitat d'expertesa humana, però considera que pot no ser el principal coll d'ampolla en l'etapa actual. És una valoració situada i provisional, no una afirmació universal sobre tota la recerca.
- Alhora, la IA obre un ventall enorme de possibilitats per a tothom.
- Si els camps de coneixement són, en algun sentit, infinits, sempre poden aparèixer espais nous per explorar. En aquest context, l'originalitat a l'hora de trobar preguntes pot adquirir més valor que competir per resoldre problemes evidents o ja identificats.
- [Percepció de l'autor] L'acadèmia ja anava quedant enrere en camps on les empreses tenien incentius per fer avançar el coneixement; la IA accentua i fa visible aquesta dinàmica.
- Possible qüestió institucional: repensar el paper i l'organització de l'acadèmia, però també com hauria de canviar l'empresa per ser «també acadèmia». No limitar la reflexió a exigir adaptacions només a les universitats.
- [Afirmació d'actualitat aportada per l'autor, pendent de contrastar] Des que va començar a preparar l'article, OpenAI hauria publicat centenars de solucions a problemes matemàtics oberts. No hi ha encara una font identificada ni una xifra confirmada; no presentar-ho com a fet verificat.
- [Percepció de l'autor, pendent de documentar amb testimonis] Aquests avenços tenen un gran impacte en la comunitat matemàtica i generen controvèrsia perquè alteren els incentius amb què els investigadors vivien la recerca. L'expressió «en peu de guerra» pertany al relat de l'autor; no generalitzar-la a tota la comunitat sense evidència.
- Interpretació de l'autor: si una empresa resol grans problemes matemàtics per demostrar la seva potència, pot desestabilitzar l'al·licient de qui volia resoldre un problema interessant i, alhora, demostrar una capacitat excepcional o destacar en aquell camp.
- [Concepció personal del doctorat] Arribar a ser la persona més experta del món en un tema molt concret, sigui un camp nou o un cas que encara ningú no ha estudiat. Conservar-ho com a perspectiva de l'autor, no com a definició normativa del doctorat.
- La qüestió afecta, doncs, també la identitat, el reconeixement i la singularitat de l'aportació de l'investigador, a més de l'accés material als recursos.
- [Projecció de l'autor] Aquest canvi d'incentius i les controvèrsies associades podrien estendre's a altres camps del coneixement.
- Síntesi de l'autor: el fenomen ja s'havia observat en àmbits concrets; a mesura que la intel·ligència es converteix en un recurs més accessible i comprable, i que invertir diners pot traduir-se en més capacitat de recerca, la dinàmica s'intensifica i s'estén.

### Fragment 16 — publicació, mobilitat i permeabilitat entre acadèmia i empresa

- L'autor considera que les empreses ja estan assumint en part funcions acadèmiques; posa com a exemple els grans laboratoris d'intel·ligència artificial.
- [Observació de l'autor, sense contrast documental encara] Tot i treballar de manera més tancada —l'autor evita afirmar que sigui necessàriament en secret—, aquests laboratoris també troben valor a publicar recerca.
- [Observació de l'autor, pendent de documentar si es vol exemplificar] Hi ha molta mobilitat d'investigadors entre companyies, cosa que afavoreix una «pol·linització creuada» important.
- Aquesta circulació de persones i la publicació matisen la imatge d'una recerca empresarial completament aïllada. No impliquen que tota la recerca o els resultats siguin oberts.
- [Experiència i percepció de l'autor] La barrera entre acadèmia i empresa era molt gran: es vivien com dos mons diferenciats, amb poca permeabilitat.
- L'autor considera que la situació actual obliga a superar aquesta separació.
- Proposta concreta: les persones haurien de poder passar de l'acadèmia a l'empresa i de l'empresa a l'acadèmia amb molta més facilitat.
- No s'han concretat encara els obstacles ni els mecanismes institucionals per facilitar aquests passos.

### Fragment 17 — canvi de focus: comprendre particulars i construir sistemes que resolen

- L'autor desplaça el centre de l'article: la recerca és un exemple d'un canvi més general, també visible en el programari i en altres activitats amb aplicació pràctica.
- Pregunta central: què vol dir investigar o avançar en el coneixement quan podem obtenir resultats sense recórrer personalment tot el procés analític?
- En la concepció inicial de l'autor, investigar estava molt lligat a entendre perfectament els particulars, en continuïtat amb la seva preferència per les solucions analítiques.
- El machine learning trenca aquesta expectativa: es passa d'entendre els particulars a entendre sistemes que poden abordar-los o resoldre'ls. L'expressió de l'autor és «sistemes que poden entendre els particulars»; no prendre-la com una afirmació tècnica demostrada sobre comprensió de les màquines.
- [Tesi interpretativa de l'autor] Guanya pes una forma d'avançar orientada a trobar resultats amb aplicació pràctica, sense exigir que el procés sigui analític de principi a fi.
- El resultat pot incloure coneixement exacte o solucions analítiques com a producte del procés; l'autor no afirma que aquestes solucions desapareguin ni que els resultats hagin de ser aproximats.
- Distingir el mètode de cerca o producció del resultat de la naturalesa del resultat obtingut: un procés après o automatitzat pot conduir a una solució exacta.
- La formulació «abans investigar era entendre perfectament» descriu el punt de partida personal de l'autor i el contrast que vol explorar; evitar convertir-la en una afirmació universal sobre tota la història de la ciència.
- El «clar guanyador» del relat és una manera de treballar, no una empresa o una institució concreta. Presentar aquesta primacia com la lectura de l'autor, sense afirmar-ne una superioritat universal demostrada.
- [Generalització proposada per l'autor] Allò amb aplicació pràctica pot avançar mitjançant una aproximació global i automatitzada, en lloc de dependre exclusivament de l'esforç particular de persones o grups sobre cada solució.
- El programari és un segon exemple central: segons l'autor, el múscul que distingia els grans projectes s'esvaeix amb aquestes capacitats. Encara no s'ha concretat un cas; evitar interpretar-ho com la desaparició de tots els avantatges dels equips grans.
- La reflexió final apunta a una substitució que pot abastar el conjunt d'una empresa humana o d'un projecte —l'«endeavor», en paraules de l'autor—, més enllà d'automatitzar una tasca concreta. El terme es pot expressar com «l'esforç col·lectiu orientat a un objectiu» o «el projecte sencer», segons el context.
- El desplaçament entre acadèmia i empresa queda com una conseqüència o un exemple del canvi de mètode; deixa de ser el fil principal.
- Mantenir l'abast acotat: aquesta reflexió reorganitza el material existent; no obre una nova ronda extensa d'entrevista sobre totes les activitats afectades.

## Fets i observacions

- [Aportat per l'autor] Hi ha un resultat recent relacionat amb OpenAI i el problema de Navier–Stokes.
- [Contrastat amb fonts primàries] El 8 de setembre de 2026, OpenAI va publicar una proposta de solució al problema d'existència i regularitat de Navier–Stokes.
- [Contrastat amb fonts primàries] La prova proposada segueix la via negativa: construeix una solució de les equacions tridimensionals incompressibles, amb viscositat positiva i força externa suau, que parteix del repòs i desenvolupa velocitat no fitada en temps finit, mantenint l'energia cinètica fitada.
- [Contrastat amb fonts primàries] OpenAI afirma que això estableix les alternatives C i D de la formulació oficial del problema del mil·lenni (casos de *breakdown* o singularitat), tant a l'espai complet com al tor tridimensional.
- [Contrastat amb fonts primàries] La publicació consta d'un manuscrit analític de 166 pàgines i d'una formalització en Lean 4 publicada a GitHub.
- [Segons OpenAI] El resultat va ser produït per un sistema intern més capaç que GPT-6 Astra; el grup decisiu va involucrar aproximadament 10.000 agents concurrents, va treballar unes 88 hores i va consumir uns 130.000 milions de tokens de sortida. La formalització i verificació en Lean va requerir 17 hores addicionals amb GPT-6 Astra.
- [Estat institucional, 16 de setembre de 2026] El Clay Mathematics Institute encara etiqueta el problema com a «Active». Per tant, convé escriure «OpenAI afirma haver resolt el problema» o «ha presentat una proposta de solució», no donar encara per feta l'acceptació oficial.
- [Contrastat amb el CMI] Perquè el Clay Mathematics Institute consideri una solució, aquesta ha d'aparèixer en una publicació admissible, han d'haver passat almenys dos anys i ha d'haver obtingut acceptació general de la comunitat matemàtica mundial.
- [Segons OpenAI] L'empresa no té intenció de reclamar el Premi del Mil·lenni.
- [Experiència de l'autor] Carrera acadèmica en interacció persona-ordinador, especialment en interacció i interfícies tangibles.
- [Experiència de l'autor] Una part important del treball de recerca i desenvolupament estava relacionada amb la detecció de gestos.
- [Posició inicial de l'autor] Rebuig fort del *machine learning* i preferència per solucions totalment analítiques.
- [Context aportat per l'autor] Boom de l'aprenentatge automàtic al Music Technology Group de la Universitat Pompeu Fabra, especialment en aplicacions d'àudio i música.
- [Projecte de l'autor] Reconeixement analític de gestos de direcció d'orquestra executats amb la batuta o amb la mà. L'autor confirma que formava part de la seva tesi doctoral i també d'un projecte europeu, recordat provisionalment com a «Fènix».
- [Enfocament de l'autor] Modelar els gestos mitjançant la seva forma, intenció i una seqüència explícita de condicions o esdeveniments.
- [Finalitat aclarida per l'autor] Enregistrar, identificar i etiquetar els gestos per documentar-los i permetre correlacions amb altres dades; el treball no fixava encara què s'estudiaria posteriorment amb aquestes dades.
- [Observació de l'autor a partir de converses amb directors] Distinció entre gestos més estàndards, associats sobretot als assajos, i gestos expressius que traslladen al moviment l'emoció musical.
- [Record provisional de l'autor] El projecte europeu volia enriquir l'experiència dels concerts de música clàssica amb explicacions accessibles al públic mitjançant una tauleta o un dispositiu semblant.
- [Valoració de l'autor en aquella etapa] El *machine learning* podia aproximar qualsevol solució, però l'aproximació era inferior a la certesa d'una solució analítica.
- [Record pendent de precisar] Microsoft Kinect emprava imatges de profunditat i un classificador per detectar o identificar mans o parts del cos.
- [Contrastat amb la publicació tècnica de Microsoft Research] El sistema de Kinect presentat a CVPR 2011 estimava la postura humana a partir d'una sola imatge de profunditat: convertia el problema en una classificació píxel a píxel de parts del cos i, a partir del resultat, proposava les posicions 3D de les articulacions.
- [Contrastat amb la publicació tècnica de Microsoft Research] El classificador era un bosc de decisió aleatori entrenat amb un conjunt de dades sintètic molt gran i variat. «Classificador de parts del cos —incloses les mans—» és una descripció més precisa que «classificador de mans».
- [Contrastat amb fonts de l'MTG] El Music Technology Group, creat el 1994 i dirigit per Xavier Serra en el període documentat, s'especialitzava en tecnologies de processament d'àudio i aplicacions musicals i multimèdia; entre les seves línies hi havia l'anàlisi i classificació automàtica de contingut musical.
- [Contrastat amb una publicació tècnica específica] El Kinect original obtenia profunditat mitjançant llum estructurada: un projector emetia un patró de punts infrarojos i una càmera IR desplaçada el capturava; la disparitat permetia calcular la profunditat.
- [Contrastat amb una publicació tècnica específica] L'oclusió del patró provocava regions sense dades de profunditat, descrites com a *Kinect shadows*. Com que el projector IR era a l'esquerra de la càmera IR, en el mapa de profunditat original aquestes ombres apareixien sempre a l'esquerra dels objectes que les provocaven.
- [Record de l'autor; no verificat documentalment] Un classificador entrenat amb persones dretanes va fallar amb persones esquerranes perquè havia après a utilitzar l'orientació d'aquestes ombres com a indici de la mà o de la seva postura.
- [Inferència tècnica plausible; no confirmada com a explicació del cas] Si les imatges de mans esquerres es transformaven per emmirallament per fer-les equivaler a mans dretes, també s'emmirallava l'artefacte del sensor. En canvi, en una captura real l'ombra ve determinada per la posició fixa del projector respecte de la càmera, no per la lateralitat de la persona.
- [Experiència de l'autor] La tesi doctoral va evitar gairebé completament i de manera deliberada l'ús de *machine learning*.
- [Experiència de l'autor] Es van fer algunes proves amb programari genèric capaç de rebre senyals i aprendre postures etiquetades manualment, però no es va adoptar com a metodologia central.
- [Interpretació retrospectiva de l'autor] La tesi se situa al final d'una primera onada d'interfícies tangibles que havia arribat abans que existissin les eines i els conceptes necessaris per fer-la plenament útil.
- [Experiència de l'autor] En acabar la tesi hi havia la sensació d'haver arribat tard a aquella onada, mentre el centre d'interès es desplaçava cap al *multitouch*.
- [Perspectiva de l'autor] El renaixement posterior de la realitat virtual va reforçar una visió cíclica del desenvolupament tecnològic: una tecnologia prematura pot semblar morta fins que canvien les condicions.
- [Experiència de l'autor] El final de la tesi comporta una acceptació simbòlica de l'esgotament de l'enfocament analític: la solució apresa podia imposar-se no per ser ideal, sinó perquè funcionava prou bé amb molt menys esforç específic.
- [Experiència de l'autor] Després d'un període sense pensar gaire en el tema, l'*inpainting*, la transferència de textures o d'estil, DeepDream i posteriorment els *transformers* van mostrar una dimensió generativa que va canviar la percepció sobre la utilitat de la IA.
- [Projecte professional de l'autor; detalls pendents] Un projecte intern anomenat provisionalment Product Pixel va explorar interfícies conversacionals, generació de contingut i control de la generació, però no es va arribar a llançar.
- [Analogía de l'autor] El *machine learning* era concebut com els epicicles del model astronòmic antic: un aproximador que podia ajustar-se tant com calgués, mentre que la solució analítica equivalia a trobar la llei compacta subjacent.
- [Contrast històric] El sistema recordat s'anomena d'epicicles i deferents. Copèrnic encara va conservar epicicles; Kepler va establir les òrbites el·líptiques i Newton en va donar després una explicació dinàmica general.
- [Posició actual de l'autor] Encara hi ha molts problemes amb solucions analítiques absolutament precises i valuoses, però molts altres són massa complexos o ambigus perquè l'exactitud sigui el criteri central.
- [Posició actual de l'autor] En moltes aplicacions d'IA és suficient una resposta «direccionalment correcta», de manera semblant a com les persones operen sovint amb aproximacions i context.
- [Criteri d'adequació] El *machine learning* és especialment apropiat per a problemes poc definits que admeten ambigüitat i per als quals existeixen models prou bons.
- [Record provisional de l'autor] Visita d'un investigador principal d'una universitat australiana, que va explicar el treball final de tesi d'un doctorand sobre reconeixement o reconstrucció 3D de mans amb una càmera convencional.
- [Hipòtesi forta, pendent de confirmació personal] El dispositiu comercial recordat era probablement **The Leap**, anunciat el 21 de maig de 2012 i conegut després com a Leap Motion Controller. «NUI» seria probablement el terme *Natural User Interface*, no el nom del dispositiu.
- [Contrastat] Leap Motion era una startup de San Francisco fundada el 2010; quan va anunciar The Leap el 2012 havia captat 14,55 milions de dòlars segons la seva nota de premsa. El preu anunciat del dispositiu era de 69,99 dòlars.
- [Contrastat] El Leap Motion Controller feia seguiment tridimensional de mans i dits mitjançant càmeres infraroges. La documentació comercial posterior anunciava fins a 200 fotogrames per segon.
- [Candidat principal; coincidència tècnica molt alta però institucional incompleta] Robert Y. Wang i Jovan Popović van publicar el 2009 un sistema que reconstruïa la postura 3D completa d'una mà a partir d'una sola imatge d'una webcam i d'un guant de Lycra amb un patró multicolor. El sistema estimava 26 graus de llibertat i funcionava aproximadament a 10 fps. Wang va acabar el doctorat en EECS al MIT el 2011, dirigit per Popović.
- [Possible explicació de la discrepància geogràfica] Jovan Popović va ser professor al MIT fins al 2008 i després investigador d'Adobe i professor afiliat de la University of Washington, a Seattle. És possible que «universitat australiana» sigui un record desplaçat —potser per confusió entre *Washington* i *Western Australia*— o que el relat de la visita i el projecte tècnic siguin dos records combinats. No s'ha trobat encara cap prova documental que Popović visités l'MTG.
- [Connexió empresarial del candidat principal] El projecte doctoral de Wang va desembocar en 3Gear Systems, fundada el març de 2012 i rebatejada posteriorment com Nimble VR. La primera versió comercial utilitzava dues Kinect; després va evolucionar cap a una única càmera de profunditat petita amb làser, seguiment esquelètic sense guant i una lectura aproximadament cada 20 ms. Facebook/Oculus va adquirir Nimble VR el 2014.
- [Possible barreja amb el dispositiu comercial] La seqüència «tesi del guant multicolor → aparell de profunditat molt més ràpid i sense guant» també descriu la trajectòria del mateix Wang des de la recerca del MIT fins a 3Gear/Nimble VR. Tanmateix, l'anunci de The Leap del maig de 2012 continua encaixant millor amb el record d'un dispositiu petit sobre el qual es posava la mà i amb un *frame rate* molt elevat.
- [Candidat australià descartat gairebé del tot] La tesi de Desmond Chun Fung Chik, «3D Hand Tracking in a Stochastic Approximation Framework» (Australian National University, 2009; supervisor principal Jochen Trumpf), tractava reconstrucció 3D de mans i rendiment interactiu, però emprava dues càmeres, era *markerless*, no feia servir un guant multicolor i es va acabar tres anys abans de l'anunci de Leap Motion.
- [Candidat australià històric, cronologia incompatible] La tesi d'Eun-Jung Holden, «Visual Recognition of Hand Motion» (University of Western Australia, 1997), sí que reconstruïa 21 graus de llibertat des d'una sola vista amb un guant codificat per colors, però és massa antiga per encaixar amb l'anunci de Leap Motion i l'etapa doctoral de l'autor.
- [Cronologia aportada per l'autor] La tesi doctoral es va presentar el 2014; el treball de reconeixement de gestos de directors d'orquestra correspon probablement a 2012–2013, i la visita de l'investigador se situa en aquella mateixa etapa, més probablement el 2012.
- [Contrastat amb OpenAI i premsa directa] El projecte de Navier–Stokes va emprar uns 10.000 agents concurrents i aproximadament 130.000 milions de tokens de sortida; OpenAI va dir a la premsa que el cost va ser de milions de dòlars.
- [Contrastat amb l'assaig de Terence Tao] Tao descriu una transició de l'«escassetat de proves» a l'«abundància de proves» i el risc d'«indigestió de proves»: generació, verificació, exposició, revisió humana i incorporació al coneixement canònic avancen a velocitats diferents.
- [Contrastat amb l'assaig de Terence Tao] Per a Tao, una prova formalment correcta no completa per si sola el progrés matemàtic: també ha de ser comprensible, comunicada, digerida per la comunitat i integrada en la teoria del camp. Afirma que una prova que cap humà pugui explicar adequadament s'hauria de considerar incompleta, fins i tot si ha estat verificada formalment.

## Cronologia i ordre dels esdeveniments

- Present: resultat recent sobre Navier–Stokes com a punt de partida narratiu.
- 28 d'agost de 2026: segons OpenAI, comença l'entrenament del nou model intern.
- 1 de setembre de 2026: OpenAI inicia l'avaluació dels problemes del mil·lenni després de sentir rumors que se n'havien resolt dos.
- 5 de setembre de 2026: els agents arriben al resultat de Navier–Stokes, unes 88 hores després de l'inici de l'experiment.
- 6 de setembre de 2026: finalitza la verificació en Lean, segons la cronologia d'OpenAI.
- 8 de setembre de 2026: OpenAI publica l'anunci, el manuscrit i la formalització.
- 16 de setembre de 2026: el CMI continua mostrant el problema com a actiu; encara no hi ha reconeixement oficial del premi.
- Retrospectiva: experiències anteriors de l'autor que van fer visible el desplaçament de la recerca i la limitació d'accés des de fora de les empreses; l'autor aclareix que no ho vivia especialment amb por o preocupació.
- Etapa inicial de la carrera acadèmica: treball en interacció persona-ordinador, interfícies tangibles i detecció de gestos.
- Posició metodològica d'aquella etapa: oposició al *machine learning* i defensa de les solucions analítiques.
- Mateixa etapa: forta expansió del *machine learning* al Music Technology Group, en contrast amb la posició de l'autor.
- Projecte de reconeixement dels gestos de directors d'orquestra mitjançant regles analítiques explícites.
- Context tecnològic contemporani: aparició de Microsoft Kinect i detecció corporal basada en imatges de profunditat i classificació.
- Fase tardana del desenvolupament o inici de proves externes del Kinect, segons el record de l'autor: detecció d'un possible biaix dretà/esquerrà relacionat amb les ombres infraroges.
- Durant la tesi doctoral de l'autor: decisió gairebé explícita d'evitar el *machine learning*, amb algunes proves exploratòries que no es van integrar en el nucli de la recerca.
- 2012, probablement: visita d'un investigador principal australià i relat sobre el projecte de tesi d'un dels seus doctorands; la data continua sent aproximada.
- 2012–2013, probablement: treball de l'autor sobre reconeixement de gestos de directors d'orquestra.
- 2009: publicació del sistema de Wang i Popović amb webcam i guant multicolor, possible coincidència tècnica amb el record però sense encaix institucional confirmat.
- 2011: Robert Y. Wang acaba el doctorat en EECS al MIT; aquesta data encaixa amb un relat fet poc abans o poc després de la defensa.
- 21 de maig de 2012: anunci públic de The Leap per Leap Motion; possible dispositiu que va desencadenar la reflexió de l'investigador visitant.
- Març-octubre de 2012: Wang funda 3Gear Systems i presenta una plataforma de seguiment de mans sense guant basada inicialment en dues Kinect; és una segona tecnologia comercial contemporània que es podria haver barrejat en el record.
- Moment pròxim a la defensa del doctorand: aparició del dispositiu comercial, que supera àmpliament el rendiment del prototip acadèmic segons el relat.
- 2014: presentació de la tesi doctoral de l'autor.
- Anys posteriors: l'autor revisa la seva posició i conclou que havia jutjat el *machine learning* a partir de sistemes i escales massa petits.
- Final de la tesi: acceptació simbòlica que l'autor podia ser «l'últim» a afrontar analíticament aquella classe de problemes; el *machine learning* guanyava perquè la seva «segona millor solució» ja era prou útil.
- Pas de l'acadèmia a l'empresa: període llarg en què la qüestió queda pràcticament fora del focus de l'autor.
- Nova onada d'IA visual: *inpainting*, transferència d'estil o textures i DeepDream fan visible una capacitat generativa diferent de la classificació tradicional.
- Etapa posterior: aparició dels *transformers*, les interfícies conversacionals i el projecte intern Product Pixel, que anticipa el pas de construir o declarar explícitament a dirigir la generació.
- 2026: els sistemes d'IA fan contribucions de recerca matemàtica, culminant provisionalment en l'anunci d'OpenAI sobre Navier–Stokes i reobrint la pregunta institucional.
- Projecció: conseqüències possibles per al futur institucional de la recerca.

## Idees clau

- [Focus vigent, fragment 17] El centre és el canvi de manera d'avançar: d'entendre i construir particularment cada solució a construir o emprar sistemes capaços de trobar resultats. Recerca i programari en són exemples.
- [Distinció central] Un procés automatitzat o après no implica un resultat aproximat; pot produir coneixement exacte o una solució analítica sense que tot el camí fins a obtenir-la hagi estat analític.
- [Conseqüència] L'automatització pot abastar un projecte o un esforç col·lectiu complet, més enllà de tasques concretes. Formular-ne l'abast amb exemples i sense universalitzar la tesi.

- [Fragment 16] L'empresa com a espai de recerca amb alguns trets acadèmics ja existeix, segons l'autor: publicar i canviar de laboratori afavoreix la circulació del coneixement fins i tot en entorns més tancats.
- [Proposta de l'autor] Facilitar el pas de persones en totes dues direccions entre acadèmia i empresa; superar la separació viscuda com dos mons poc permeables.

- [Fragment 15] Continuïtat intensificada: la IA fa més directa la conversió de pressupost i còmput en capacitat investigadora; segons l'autor, atraure talent humà específic pot deixar de ser el principal coll d'ampolla en alguns contextos actuals.
- [Contrapunt de l'autor] La mateixa IA amplia les possibilitats individuals; trobar preguntes originals pot guanyar importància davant la competició per problemes ja identificats.
- [Nova dimensió] A més dels recursos, poden canviar els incentius de la recerca: reconeixement, identitat professional i aspiració a fer una aportació singular. Cal documentar les reaccions concretes abans d'atribuir-les a una comunitat.
- [Pregunta institucional oberta] Com ha de canviar l'acadèmia i com pot canviar l'empresa per ser «també acadèmia»?

- [Criteri actualitzat amb el fragment 14] Presentar el desplaçament cap a empreses com una observació de l'autor, sense pressupostar por ni una valoració global negativa. La qüestió personal és la limitació per investigar en determinats camps quan no s'és dins d'una empresa amb prou recursos.
- [Perspectiva de l'autor] La lentitud acadèmica i la necessitat de sostenir l'activitat mitjançant finançament condicionen les línies de recerca. La capacitat empresarial per concentrar recursos pot ser una evolució natural quan hi ha aplicació pràctica.
- [Distinció de l'autor] Publicació i discussió acadèmiques versus major aïllament empresarial i dificultat de recolzar-se en el treball privat des de fora. La universitat pot tenir una funció complementària en àmbits sense retorn empresarial esperat.
- [Límit de l'article] La possible separació futura entre recerca i educació és una reflexió lateral, no un tema a desenvolupar aquí.

- Un avenç matemàtic recent serveix de detonant per plantejar una pregunta institucional més àmplia.
- Possible desplaçament del centre de gravetat de la recerca des de les universitats i institucions tradicionals cap a empreses privades.
- La qüestió no es limita a les matemàtiques: pot afectar la recerca en general.
- Cal diferenciar la capacitat científica de la IA del poder econòmic i institucional de les empreses que la desenvolupen.
- Punt de partida personal: confiança en els models explícits i comprensibles construïts analíticament, en contraposició a l'aprenentatge automàtic.
- Possible arc de transformació encara per completar: com i per què aquesta posició inicial va canviar, es va matisar o va entrar en crisi.
- La detecció de gestos pot servir com a cas concret per explicar la tensió entre dissenyar regles explícites i aprendre patrons a partir de dades.
- «La segona millor solució de tot»: síntesi memorable de la crítica inicial de l'autor al *machine learning*.
- Tensió epistemològica:
  - solució analítica: explicació explícita, causal o reglada i aparent certesa;
  - solució apresa: aproximació estadística capaç de cobrir molts casos, però amb errors i límits menys previsibles.
- Tensió professional o identitària: entendre i formalitzar el fenomen personalment versus delegar el reconeixement del patró a un model.
- La sensació de «fer trampa» pot ser un element important de l'arc personal: què es considera comprendre o resoldre realment un problema?
- Possible connexió futura amb Navier–Stokes: diferència entre una màquina que produeix una prova formal verificable i un classificador que només aproxima una resposta.
- Un model pot explotar correlacions accidentals o artefactes instrumentals en lloc de les propietats que els investigadors creuen que està aprenent.
- En una solució analítica, l'autor decideix explícitament quines propietats constitueixen el gest; en un model après, les propietats decisives poden quedar ocultes fins que apareix un cas fora de distribució.
- El problema no és únicament que el resultat sigui aproximat: també pot ser correcte per la raó equivocada.
- [Interpretació provisional] L'exemple és un cas del que posteriorment s'ha anomenat aprenentatge de dreceres (*shortcut learning*) o correlacions espúries.
- L'absència de *machine learning* en la tesi forma part de la posició epistemològica de l'autor: la metodologia escollida també expressava què considerava una solució legítima o «pura».
- Les eines d'aprenentatge interactiu reduïen l'esforç tècnic necessari per entrenar classificadors, però no resolien l'objecció conceptual de l'autor.
- Possible tensió per desenvolupar: «puresa» de la solució versus eficàcia, adaptabilitat o accessibilitat de les eines basades en exemples.
- L'error de perspectiva de l'autor no consistia necessàriament a descriure malament les limitacions dels models petits d'aquell moment, sinó a extrapolar-les sense imaginar els efectes d'escala.
- L'escala pot convertir una «segona millor solució» generalista en una solució pràcticament superior a les alternatives especialitzades.
- Una tecnologia no necessita ser la millor solució teòrica per substituir-ne una altra: n'hi ha prou que sigui accessible, general i funcioni prou bé.
- Epicicles versus llei subjacent com a metàfora de dues maneres de resoldre un problema:
  - acumular complexitat per ajustar qualsevol observació;
  - descobrir una estructura compacta que expliqui per què les observacions són com són.
- Possible semblança amb una sèrie de Fourier: amb prou components es pot aproximar una trajectòria periòdica arbitrària, però l'ajust no és necessàriament l'explicació física del fenomen.
- Les interfícies tangibles i la primera realitat virtual ofereixen un marc per parlar dels cicles tecnològics: invenció prematura, promesa, aparent fracàs i possible retorn quan maduren les eines i els conceptes.
- L'autor pot presentar-se com «l'últim» representant d'una manera analítica de resoldre problemes d'interacció, no com una afirmació literal sinó com la sensació que tancava una etapa.
- La IA generativa trenca l'objecció inicial que reduïa el *machine learning* a aproximar o classificar: ara produeix material nou i permet treballar dirigint un espai de possibilitats.
- Canvi de paradigma en el treball amb ordinadors: de declarar exactament cada resultat a definir la intenció, les restriccions o la direcció d'un procés generatiu.
- La qüestió no és escollir universalment entre exactitud i aproximació, sinó determinar quina mena de resposta exigeix cada problema.
- «Direccionalment correcte» pot ser un concepte central per descriure el valor pràctic de la IA en dominis oberts, creatius o contextuals.
- Semblança entre IA i cognició humana: una gran part de l'activitat intel·ligent quotidiana no consisteix a trobar una resposta formalment única, sinó a navegar satisfactòriament l'ambigüitat.
- El salt qualitatiu no prové només de l'algoritme: també de les dades, el còmput, el capital, l'enginyeria i la capacitat de coordinar molts agents.
- La innovació privada pot produir avenços científics reals i, alhora, desplaçar poder, talent, agenda i capacitat experimental fora de les universitats.
- Diferència entre produir resultats i produir una disciplina:
  - resultat: prova o solució correcta;
  - disciplina: explicacions, intuïcions, especialistes, revisió, transmissió, teoria compartida i formació de la generació següent.
- El coll d'ampolla pot passar de descobrir o demostrar a comprendre, revisar, ensenyar i integrar.
- La concentració de còmput crea una barrera d'entrada epistemològica: no només determina qui pot comercialitzar una tecnologia, sinó qui pot formular i executar experiments a la frontera del coneixement.
- Possible paradoxa: la universitat forma investigadors i produeix el coneixement públic amb què s'entrenen els sistemes, però pot quedar exclosa de la fase següent per manca de capital computacional.
- Les empreses probablement prioritzaran problemes amb valor estratègic, comercial o propagandístic; poden quedar desatesos camps científicament valuosos sense retorn evident.
- La pregunta «quin és el futur de les professions?» es concreta en la recerca: què pot fer un investigador individual quan l'instrument imprescindible ja no és un laboratori assequible, sinó una infraestructura d'inferència de milions de dòlars?

## Noms propis, institucions i conceptes

- OpenAI.
- Equacions de Navier–Stokes.
- Problemes del Mil·lenni del Clay Mathematics Institute.
- Clay Mathematics Institute (CMI).
- Lean 4: assistent de proves utilitzat per formalitzar el resultat.
- *Finite time blowup*: formació d'una singularitat en temps finit; la velocitat deixa de ser fitada.
- Alternatives C i D de la formulació oficial del problema: *breakdown* a l'espai complet i al tor tridimensional.
- Universitats i institucions de recerca tradicionals.
- Empreses privades com a possibles nous centres de producció científica.
- Interacció persona-ordinador (*Human–Computer Interaction*, HCI).
- Interacció tangible i interfícies tangibles (*Tangible User Interfaces*, TUI).
- Detecció o reconeixement de gestos.
- Solució analítica: model o regles explícites derivades del coneixement del problema.
- *Machine learning*: alternativa metodològica rebutjada per l'autor en aquella etapa.
- Music Technology Group (MTG), Universitat Pompeu Fabra (UPF).
- Reconeixement dels gestos dels directors d'orquestra.
- Batuta i moviments de la mà com a senyals d'intenció musical.
- Microsoft Kinect.
- Imatge o càmera de profunditat.
- Classificació de parts del cos; relació exacta amb la detecció de mans pendent de precisar.
- Llum estructurada infraroja.
- Projector de punts infrarojos i càmera infraroja desplaçada.
- Ombra de profunditat o *Kinect shadow*: regió sense mesura causada perquè un objecte tapa el patró projectat.
- Biaix dretà/esquerrà en les dades d'entrenament.
- Correlació espúria o drecera apresa: ús d'un indici accidental que funciona en l'entrenament però falla fora d'aquelles condicions.
- Aprenentatge interactiu supervisat: l'usuari proporciona exemples i etiquetes de postures directament durant la configuració del sistema.
- Programari agnòstic respecte dels senyals d'entrada; nom de l'eina pendent d'identificar.
- Investigador principal d'una universitat australiana; nom i institució pendents.
- Doctorand i projecte de reconstrucció o reconeixement 3D de mans amb càmera convencional; detalls pendents i possiblement barrejats amb un altre record.
- The Leap / Leap Motion Controller.
- Leap Motion, Inc.; startup fundada per Michael Buckwald i David Holz.
- *Natural User Interface* (NUI): possible origen del nom recordat.
- Robert Y. Wang i Jovan Popović; sistema «Real-Time Hand-Tracking with a Color Glove».
- Jovan Popović: director doctoral de Wang; professor al MIT fins al 2008, després investigador d'Adobe i professor afiliat de la University of Washington.
- 3Gear Systems / Nimble VR: empresa sorgida del treball doctoral de Wang; evolució del guant multicolor a seguiment sense guant amb càmeres de profunditat.
- Desmond Chun Fung Chik, Jochen Trumpf i Australian National University: candidat institucional australià amb discrepàncies tècniques i cronològiques fortes.
- Eun-Jung Holden i University of Western Australia: coincidència tècnica antiga —una vista i guant de colors— però cronologia incompatible.
- Efectes d'escala: dades, mida del model, còmput d'entrenament i inferència, nombre d'agents i capital.
- «Escassetat de proves», «abundància de proves» i «indigestió de proves», en la terminologia de Terence Tao.
- Canonització del coneixement: procés d'integrar un resultat en les teories, els manuals, les eines i la formació compartida d'un camp.

## Referències i fonts

### Referències confirmades

- OpenAI, «[On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/)», 8 de setembre de 2026. Anunci, explicació del resultat i relat del procés de generació.
- OpenAI, «[Finite Time Blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)», manuscrit de 166 pàgines.
- OpenAI, «[NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler)», repositori amb les formalitzacions en Lean 4 i instruccions de comprovació independent.
- Clay Mathematics Institute, «[Navier-Stokes Equation](https://www.claymath.org/millennium/navier-stokes-equation/)». Pàgina oficial del problema; constava com a «Active» el 16 de setembre de 2026.
- Clay Mathematics Institute, «[Rules for the Millennium Prize Problems](https://www.claymath.org/millennium-problems/rules/)». Condicions per considerar i reconèixer una solució.
- Jamie Shotton et al., «[Real-Time Human Pose Recognition in Parts from a Single Depth Image](https://www.microsoft.com/en-us/research/publication/real-time-human-pose-recognition-in-parts-from-a-single-depth-image/)», CVPR 2011, Microsoft Research. Font primària sobre l'algoritme de seguiment corporal de Kinect: imatge de profunditat, classificació de parts del cos i estimació de les articulacions 3D.
- Xavier Serra, «[Current Research in Music Technology at the Audiovisual Institute of the Pompeu Fabra University](https://mtg.upf.edu/node/364)», ICMC 2004. Context institucional i línies de recerca del Music Technology Group.
- Emilia Gómez et al./MTG, «[Content Processing of Music Audio Signals](https://mtg.upf.edu/node/842)», 2008. Context sobre descripció automàtica, identificació, navegació i transformació de senyals d'àudio musical.
- Teng Deng et al., «[Kinect Shadow Detection and Classification](https://www.cv-foundation.org/openaccess/content_iccv_workshops_2013/W21/papers/Deng_Kinect_Shadow_Detection_2013_ICCV_paper.pdf)», ICCV Workshops 2013. Confirma la geometria de llum estructurada, l'oclusió del patró, els forats de profunditat i el costat fix de les ombres causat per la posició relativa del projector i la càmera IR.
- Leap Motion, «[Leap Motion Unveils World's Most Accurate 3-D Motion Control Technology for Computing](https://www.tmcnet.com/usubmit/2012/05/21/6313534.htm)», nota de premsa del 21 de maig de 2012. Anunci original de The Leap, preu, finançament acumulat i afirmacions de rendiment.
- Leap Motion, «[Leap Motion Controller](https://www.leapmotiontechnology.com/product)», fitxa comercial històrica. Seguiment de mans amb càmeres infraroges i fins a 200 fotogrames per segon.
- Robert Y. Wang i Jovan Popović, «[Real-Time Hand-Tracking with a Color Glove](https://people.csail.mit.edu/rywang/handtracking/)», ACM Transactions on Graphics / SIGGRAPH 2009. Reconstrucció 3D amb una webcam i un guant multicolor; candidat tècnic al projecte recordat, però no institucional.
- Robert Y. Wang, «[pàgina personal i publicacions](https://people.csail.mit.edu/rywang/)». Confirma el doctorat al MIT amb Jovan Popović, el sistema del guant i la continuïtat posterior amb Nimble VR.
- MIT News, «[Gesture-based computing on the cheap](https://news.mit.edu/2010/gesture-computing-0520)», 20 de maig de 2010. Descriu el projecte de Wang com una reconstrucció 3D de la mà i dels dits amb retard gairebé imperceptible.
- MIT CSAIL, «[This MIT PhD has his fingers on the pulse of virtual-reality](https://www.csail.mit.edu/news/mit-phd-has-his-fingers-pulse-virtual-reality)», 4 d'abril de 2016. Confirma que Wang és PhD '11, que Nimble VR va néixer directament del treball del guant i que el sistema posterior feia seguiment sense guant amb una càmera de profunditat i làser cada 20 ms.
- 3Gear Systems, «[From color gloves to tiny cameras: 3Gear raises $1.9M](https://threegearsystems.blogspot.com/2014/04/from-color-gloves-to-tiny-cameras-3gear.html)», 2 d'abril de 2014. Relat de primera mà de l'evolució del guant del MIT a dues Kinect i després a una càmera de profunditat petita; l'empresa es va fundar el març de 2012.
- Desmond Chun Fung Chik, «[3D Hand Tracking in a Stochastic Approximation Framework](https://openresearch-repository.anu.edu.au/items/6ef80294-fd66-4d01-8d84-c4aeafe89bd4)», tesi doctoral, Australian National University, 2009. Candidat australià descartat gairebé del tot per càmeres, tècnica i cronologia.
- Eun-Jung Holden, «[Visual Recognition of Hand Motion](https://research-repository.uwa.edu.au/files/3248290/Holden_Eun-Jung_1997.pdf)», tesi doctoral, University of Western Australia, 1997. Coincidència antiga en una sola vista i guant codificat per colors, però incompatible amb la cronologia del relat.
- Terence Tao, «[Mathematics in the Age of AI](https://arxiv.org/abs/2608.16753)», agost de 2026. Font primària per a l'abundància i indigestió de proves, la comprensió humana i la integració comunitària del coneixement.
- WIRED, «[OpenAI Just Claimed a Huge Math Discovery. Some Academics Are Crying Foul](https://www.wired.com/story/openai-navier-stokes-math-discovery-academics/)», 8 de setembre de 2026. Inclou l'afirmació del cap de recerca d'OpenAI, Mark Chen, que el cost del projecte va ser de milions de dòlars.

### Referències pendents de localitzar o verificar

- Si es concreten exemples del fragment 16, documentar publicacions i trajectòries d'investigadors entre laboratoris d'IA; distingir mobilitat entre empreses de mobilitat entre acadèmia i empresa.

- Identificar l'anunci o la publicació d'OpenAI que l'autor recorda com a centenars de solucions a problemes matemàtics oberts; verificar data, quantitat, naturalesa dels problemes i estat de validació. Afirmació del fragment 15 encara no contrastada.
- Localitzar testimonis directes de matemàtics sobre els canvis d'incentius, el reconeixement i la controvèrsia descrits al fragment 15; distingir experiències individuals de valoracions generals sobre la comunitat.

- Reaccions i valoracions independents de matemàtics especialistes sobre la validesa de la prova.
- Situació editorial del manuscrit: si s'ha enviat o publicat en una revista que compleixi les regles del CMI.
- Autoria humana i crèdits concrets darrere de l'autoria institucional «OpenAI».
- Controvèrsia sobre treball concurrent, prioritat i atribució: Levent Alpöge, Tristan Buckmaster i els resultats sobre les equacions d'Euler.
- Referència concreta que documenti el «boom» del *machine learning* a l'MTG durant els anys exactes de l'experiència de l'autor; abans cal precisar el període.
- Localitzar la tesi doctoral de l'autor i les referències del treball sobre gestos de directors d'orquestra. La pertinença a la tesi queda confirmada per l'autor; falta documentar-la i confirmar el nom i la grafia del projecte europeu recordat com a «Fènix». L'autor preveu buscar la tesi més endavant.
- Font exacta de l'anècdota del Kinect sobre entrenament amb dretans, fallada amb esquerrans i ús involuntari de l'orientació de l'ombra com a característica. No localitzada encara.
- Comprovar si l'anècdota correspon al seguiment corporal del Kinect original, a un classificador posterior de postura de mans de Microsoft o a un altre projecte construït amb el sensor Kinect.
- Identificar el programari genèric emprat per entrenar postures a partir de senyals etiquetats manualment.
- Identificar definitivament l'investigador visitant, la universitat, el doctorand i la tesi o publicació sobre mans. Candidat tècnic principal: Robert Y. Wang / Jovan Popović; falta resoldre la discrepància «Austràlia» versus MIT / University of Washington.
- Confirmar amb l'autor si el dispositiu era The Leap / Leap Motion Controller.
- Determinar si el projecte del doctorand era el de Wang i Popović, un projecte australià semblant o una combinació de records.
- Trobar, si existeix, una font escrita de l'investigador visitant que compari explícitament la tesi del doctorand amb el dispositiu comercial.
- Quantificar millor el cost del projecte de Navier–Stokes si OpenAI publica un desglossament oficial de còmput o despesa.

## Dubtes i possibles llacunes

- Terminologia: es pot descriure com una «refutació» de la regularitat global o com una «resolució negativa» del problema; cal evitar donar a entendre que s'han refutat les equacions de Navier–Stokes.
- Validació: hi ha manuscrit i prova formal, però falta l'acceptació general de la comunitat i el procés temporal exigit pel CMI.
- Quin paper hi ha tingut la IA i quin paper hi han tingut els investigadors humans?
- [Resposta parcial, fragment 14] El desplaçament observat és cap a empreses amb finançament i capacitat de concentrar-se en camps amb aplicació pràctica. L'efecte destacat és la limitació per investigar-hi des de fora, sense una por general al canvi institucional.
- El cas demostra un trasllat de la recerca cap a l'empresa privada o, més concretament, una concentració excepcional de còmput, models, capital i capacitat de coordinació?
- Quins arguments concrets sostenien aleshores el rebuig del *machine learning*? Precisió, necessitat de dades, opacitat, robustesa, cost, elegància, control o capacitat de generalització?
- Hi havia algun projecte o sistema concret de detecció de gestos que exemplifiqués aquesta preferència analítica?
- En quin moment i arran de quin fet va començar a canviar aquesta posició?
- [Resposta parcial] La tesi es va presentar el 2014; el projecte dels gestos se situa probablement el 2012–2013 i la visita, més probablement, el 2012. Encara falta establir quan va començar la tesi i documentar les dates exactes dels projectes.
- [Resposta parcial] El treball sobre gestos de direcció d'orquestra formava part de la tesi i d'un projecte europeu recordat com a «Fènix». Falta confirmar el nom exacte del projecte i identificar les publicacions a partir de la tesi.
- [Resposta parcial] Es volien documentar els gestos mitjançant enregistrament i etiquetatge, per permetre correlacions amb altres dades. Falta concretar quins gestos s'etiquetaven i amb quines regles analítiques. L'autor no recorda si es va arribar a una anàlisi semàntica. Les preguntes de detall queden en pausa fins a recuperar el capítol de la tesi, per petició de l'autor.
- Quines dades es correlacionaven amb els gestos i com es relacionava, si ho feia, aquest treball amb les explicacions al públic? El record del projecte europeu apunta a enriquir concerts amb tauletes, pendent de documentació.
- El problema inesperat del Kinect queda identificat: el classificador podia haver après l'orientació d'una ombra instrumental en comptes de la forma essencial de la mà; falta confirmar-ne la font exacta.
- El contrast rellevant és entre aproximació i certesa, entre opacitat i explicabilitat, o entre reconèixer patrons i comprendre el fenomen? Pot ser una combinació, però caldrà precisar-ho.
- La font recordada era un article científic, un informe tècnic, una entrada de Microsoft Research, una conferència o una explicació oral?
- Es van capturar només mans dretes i després es van emmirallar les dades, o es van capturar cossos sencers de participants dretans?
- L'error afectava la detecció de la mà, la classificació de la seva postura o el reconeixement d'un gest complet?
- Què significava exactament «puresa» per a l'autor en aquell moment: explicabilitat, autoria de les regles, determinisme, elegància, comprensió causal o una combinació d'aquests elements?
- Quin programari permetia redirigir senyals, etiquetar postures i entrenar-les? Possible eina d'aprenentatge interactiu, encara sense identificar.
- Confirmar el nom exacte de Product Pixel, l'empresa i les dates aproximades; determinar també si se'n conserva documentació que es pugui citar o descriure.
- Què vol dir exactament «control de la generació en lloc de la declaració» en el context de Product Pixel? Caldrien un o dos exemples concrets d'interacció.
- Quin vincle causal estableix l'autor entre el final de les interfícies tangibles, l'ascens del *multitouch* i el triomf de les aproximacions apreses? Poden ser processos paral·lels i no necessàriament la mateixa substitució.
- [Resposta parcial] L'autor manté que molts problemes sí que tenen solucions analítiques absolutament precises, però reconeix que molts altres són complexos o poc definits i es resolen millor amb aproximacions útils. Queda per explorar la frontera entre totes dues categories.
- De quina universitat australiana provenia el visitant? La visita se situa ara aproximadament el 2012, tot i que falta confirmar-ne la data exacta.
- Podria el visitant haver estat Jovan Popović i la institució recordada haver estat la University of Washington, no una universitat australiana? Alternativament, el visitant podia ser australià però haver posat com a exemple el treball de Wang sense que fos el seu doctorand.
- El projecte reconstruïa tota la geometria 3D de la mà, estimava l'esquelet o només classificava postures i gestos?
- Cal esperar la continuació abans de cercar el projecte, perquè l'autor avisa que podria estar barrejant records.
- El dispositiu era realment Leap Motion? La data de l'anunci, el seguiment de mans sobre un sensor i l'alt *frame rate* hi encaixen molt bé.
- El rendiment del prototip doctoral era realment d'uns 5 fps o és una aproximació narrativa?
- El valor publicat per Wang i Popović és aproximadament 10 fps; la proximitat amb els 5 fps recordats reforça la identificació, però no la demostra.
- La crítica principal és que les empreses poden executar millor la mateixa agenda acadèmica, o que també poden decidir quina serà l'agenda científica?
- [Pregunta exploratòria anterior; no pressuposa una reivindicació de l'autor] Quines funcions específiques haurien de continuar sent públiques o universitàries: accés al còmput, selecció de problemes, verificació, preservació, formació, crítica independent o totes aquestes?
- [Pregunta exploratòria anterior; no és una proposta de l'autor] Si la frontera exigeix milions en inferència, quins models institucionals podrien preservar l'accés públic: infraestructures nacionals, consorcis universitaris, fundacions, obligacions d'accés o models oberts?

## Relacions i contradiccions a revisar

## Possibles línies d'organització

<!-- Només esquemes o agrupacions provisionals; no redactar l'article. -->

### Proposta editorial anterior — repàs del 17 d'octubre de 2026

- Superada pel canvi de focus del fragment 17 i per la proposta revisada següent; es conserva com a historial de les decisions.

- Estat: hi ha prou material per començar a estructurar i redactar; aturar l'expansió de l'entrevista a nous temes. Aquesta és una proposta de l'assistent, encara no una estructura aprovada per l'autor.
- Petició actual de l'autor: revisar què tenim, limitar les ramificacions i avançar cap a un article publicable sense esperar setmanes.
- Fil central proposat: el desplaçament de capacitat investigadora cap a empreses amb recursos ja era visible durant la tesi; la IA l'intensifica en fer més directa la conversió de pressupost i còmput en capacitat de recerca. Alhora, amplia les possibilitats individuals i pot donar més valor a trobar preguntes originals.
- Veu: reflexió personal basada en experiència i observació; conservar els matisos dels fragments 14–16, sense atribuir a l'autor por ni una denúncia general de la recerca privada.
- Abast suggerit: aproximadament 1.200–1.600 paraules, amb una sola anècdota central i un exemple actual ben documentat.

#### Estructura proposada

1. Detonant actual i record: un avenç recent en recerca amb IA fa tornar una escena de l'etapa doctoral. Triar i verificar l'exemple abans de publicar; evitar una llista de novetats.
2. Allò que ja passava: la visita i el relat d'un treball doctoral superat per un desenvolupament empresarial. Presentar-ho com a record personal amb incerteses, sense imposar una identificació conjectural. Context breu de la tesi, sense entrar en els detalls del projecte europeu.
3. Allò que l'autor no havia anticipat: «la segona millor solució de tot» i el canvi de perspectiva sobre l'escala. Fer servir aquest arc com a pont breu cap al present, sense convertir-lo en un tractat sobre exactitud i aproximació.
4. Què accentua la IA: pressupost, còmput i accés; «si estaves fora, estaves fora»; possibles canvis de reconeixement i incentius. Equilibrar-ho amb les oportunitats noves i el valor de les preguntes originals. Formular com a interpretació les generalitzacions que no es puguin demostrar.
5. Tancament obert però concret: acadèmia i empresa amb funcions complementàries i passos més fàcils entre totes dues; recuperar la pregunta sobre qui pot fer recerca i amb quins mitjans, sense haver de dissenyar una reforma institucional completa.

#### Material a reservar

- Mecànica i etiquetes del projecte de gestos; nom exacte del projecte europeu i recuperació de la tesi.
- Anècdota del Kinect si no es localitza una font clara; no és necessària per sostenir el fil central.
- Desenvolupament històric dels epicicles, cicles de realitat virtual i interfícies tangibles.
- Projecte Product Pixel i detalls sobre interfícies generatives.
- Separació entre educació i recerca, obstacles concrets de les carreres acadèmiques i propostes institucionals exhaustives.
- Comprensió humana versus producció de proves (Tao): com a màxim un matís breu, si encaixa; reservar-ne el desenvolupament per a un altre text.

#### Mínim pendent abans de publicar

- Verificar amb fonts primàries l'exemple actual escollit, la data i l'estat de validació. Les etiquetes de «confirmat» de les notes antigues no substitueixen aquesta revisió.
- Si es conserva l'afirmació de centenars de problemes resolts o de controvèrsia entre matemàtics, documentar-ne l'abast amb fonts precises; altrament, prescindir de les xifres i de les atribucions col·lectives.
- Per a l'anècdota antiga, mantenir només els detalls recordats amb confiança i explicitar que és un record; no cal bloquejar la redacció fins a identificar tots els noms.
- No cal ampliar l'entrevista per començar l'esborrany. Les decisions de selecció i el contrast de les afirmacions que s'incloguin són suficients per al següent pas.

### Proposta editorial revisada — després del fragment 17

- Esquema de treball proposat per l'assistent, pendent de validació; no és prosa de l'article.
- Centre: com canvia l'activitat d'investigar, crear i resoldre quan el procés particular es pot confiar a sistemes generals apresos o automatitzats.
- Fil personal: «la segona millor solució de tot» → reconeixement del valor pràctic i de l'escala → distinció entre comprendre cada solució i saber fer funcionar sistemes que la poden trobar.
- La recerca és l'exemple que desencadena la reflexió; el programari permet mostrar que l'abast és més ampli.

1. Punt de partida personal: durant la tesi, preferència per entendre i definir les regles de cada solució; «la segona millor solució de tot». Context mínim de gestos, sense desenvolupament tècnic.
2. Revisió d'aquella intuïció: l'escala i la utilitat dels sistemes apresos; entendre sistemes capaços d'abordar particulars, en lloc de construir cada resposta a mà.
3. El cas de la recerca: els resultats matemàtics com a exemple, un cop verificats; diferenciar obtenir una solució, comprovar-la i comprendre-la. No cal que el procés de producció sigui analític perquè el resultat pugui ser exacte.
4. El mateix canvi en el programari: possibilitat d'abordar projectes i objectius sencers amb sistemes generals. Relacionar-ho amb l'experiència de l'autor i distingir-ho de l'automatització de tasques aïllades.
5. Conseqüències i tancament: canvien el valor de l'expertesa particular, els recursos necessaris i la tria de problemes; hi ha concentració de capacitat i noves possibilitats individuals. La permeabilitat entre acadèmia i empresa pot aparèixer breument, però no organitza el text.

- La visita de l'investigador i el dispositiu comercial passen a ser una anècdota opcional: conservar-la només si ajuda al fil sense dominar-lo.
- Recuperar la distinció entre produir resultats i comprendre'ls, abans reservada; ara és pertinent per al centre del text. No cal desenvolupar tota la qüestió institucional o pedagògica.
- Mantenir l'objectiu de text acotat i el contrast de les afirmacions actuals abans de publicar. No cal ampliar totes les ramificacions per començar l'esborrany.

### Criteri editorial final i guió breu

- L'autor demana un article curt, amb alguna intuïció útil, escrit des de les observacions i l'experiència personals.
- Evitar grans veritats, to de certesa universal, prediccions del futur i desenvolupaments extensos sobre l'ambició humana; aquesta última pot ocupar només un parell de frases.
- Encàrrec actual: un guió amb punts i notes concretes perquè l'autor desenvolupi manualment la prosa.
- Guió vigent: [Guió](ha-guanyat-la-segona-millor-solucio-guio.md). Substitueix les propostes d'estructura anteriors com a base de treball; aquestes es conserven com a historial.
- L'extensió anterior de 1.200–1.600 paraules deixa de ser la referència; el guió proposa orientativament 700–900, sense mínim obligatori.
