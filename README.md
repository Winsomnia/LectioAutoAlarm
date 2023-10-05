# LectioAutoAlarm
Tjekker automatisk hvornår din første time starter næste dag, og justere en alarm i forhold til det, ved hjælp af "python-lectio library"(https://github.com/BetterLectio/python-lectio/tree/main) og Android appen "MacroDroid"(https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=en_US)

### Setup
der er 4 variabler som kan konfigures i scriptet.
2 er nødvendige for at det skal virke:

1. "Macrodroid_adress". Denne variabel referere til det unikke Link hver macrodroid bruger har, når de laver en webhook trigger inde på appen. formatet er som følgene: "https://trigger.macrodroid.com/{indsæt_personligMacroDroidWebHookID}/" hvor at {indsæt_personligMacroDroidWebHookID} er en lang række tal man finder inde på sin macrodroid app. ("{}" skal selvfølgelig undlades når id indtastest)
2. "client" denne variabel bruges til at definere dine lectio login oplysninger, så scriptet kan hente dine lectio mødetider. formatet er som følgene: 
lectio.sdk(brugernavn="{Lectio brugernavn}", adgangskode="{lectio adgangskode}", skoleId="{lectio skoleID}") skoleid'et er et tal, som hver skole har for at lectio kan differentiere mellem skoler. CG har foreksempel tallet 5. Din skoles ID kan findes under URL'et hos din skoles Lectio: FX. CGs lectio URL hvor at 5-tallet fremgår: https://www.lectio.dk/lectio/5/default.aspx

Udover disse er der 2 variabler som ikke er nødvendige, men er gode at sætte op for at skrædersyge din LectioAutoAlarm oplevelse:
1. "RoutineCheckupDelaymin" denne variabel definere hvor mange minutter der skal gå, imellem hver gang scriptet skal tjekke efter om et modul er blevet aflyst.
2. "WakeUpDelay" denne variabel definere hvor mange minutter du bruger på at gøre dig klar og nå i skole. Dette bruges i scriptet til at skubbe alarmen den mængde minutter fra mødetiden som er nødvendigt for at du kan nå i skole.
