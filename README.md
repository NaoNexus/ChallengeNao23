# ChallengeNao23

![alt text](https://github.com/NaoNexus/ChallengeNao23/blob/main/images/logo_con_scritta.png)

## NAO Challenge 

Ogni anno il tema della NaoChallenge viene cambiato, tuttavia esso ha come scopo usare la robotica come mezzo per risolvere problematiche attuali. Questa edizione si fonda sulla sostenibilità e in particolare sui punti descritti dall'Agenda 2030 per lo Sviluppo Sostenibile. 

Il team NaoNexus si è particolarmente concentrato sui temi dell'energia pulita e accessibile e l'agire per il clima. 

### Date

- 6/04/2023 consegna progetto per semifinale - valutazione asincrona
- 28/04/2023 restituzione valutazioni

### Requisiti

- Video descrittivo del progetto (durata max 5 min)
- Logo e brand identity
- Sito web
- Report scientifico-tecnico
- Software utilizzato per la realizzazione del progetto

### Progetto

Il team NaoNexus si è impegnato per creare un progetto innovativo collaborando con l'azienda Amperia, la quale usa tecnologie in grado di rendere le infrastrutture ecosostenibili. 

La sinergia tra il team e l'azienda ha permesso di creare un sistema in grado di misurare attraverso un sensore i livelli di CO2, umidità, temperatura e luce i quali vengono poi inviati all'umanoide NAO. Essendo collegato alla domotica dell'ambiente analizzato, il robot è in grado di agire su sistemi come tapparelle, luci e termostato, garantendo condizioni di vita ideali continuamente.

Inoltre NAO è in grado di fungere da consulente ambientale tramita l'utlizzo della piattaforma Solaredge, mostrando all'utente i cambiamenti da apportare all'infrastuttura per abbassare l'impatto ambientale, piantando per esempio alberi o installando pannelli solari. 


## Cartelle progetto - coding

### Cartella app_domotica

La cartella [app_domotica] contiene il codice che ha permesso la creazione dell'app di domotica, attraverso la quale l'utente visualizza i livelli di umidità, luminosità, CO2 e temperatura di un determinato ambiente, tenendolo sempre sotto conctrollo.  

### Cartella nao_domotica

La cartella [nao_domotica] presenta al suo interno i possibili dialoghi, comportamenti e interazioni che NAO è tenuto a effettuare durante l'interazione con l'utente per la regolazione dei parametri precedentemente esposti all'interno di una stanza o infrastruttura.

### Cartella nao_solaredge

La cartella [nao_solaredge] contiene i dialoghi e azioni che NAO effettua in base alle richieste dell'utente che si vuole interfacciare con la piattaforma Solaredge, usata per una consulenza ambientale.

### Cartella server_domotica

La cartella [server_domotica] ha al suo interno l'algoritmo che permette di connettersi al server della domotica della scuola per effettuare richieste riguardanti le azioni da compiere in base ai valori raccolti tramite il sensore usato ed elaborati con l'umanoide.

### Cartella server_solaredge

La cartella [server_solaredge] contiene il codice attraverso il quale ci si può connettere alla piattaforma Solaredge e inviare eventuali richieste, essa restituirà poi come risultato le possibili modifiche e installazioni apportabili all'ambiente selezionato.

## Cartella Social

### Cartella green_nao

La cartella [green_nao] presenta al suo interno i testi e i comportamenti che NAO assume per l'esposizione degli episodi della rubrica GreenNao. Essa ha lo scopo di evidenziare quelle che sono le maggiori infrastruttre e organizzazioni eco-sostenibili dell'ambiente veronese in maniera divertente ed innovativa.

### Cartella website

La cartella [websote] contiene il codice necessarrio alla realizzazione del sito del NaoNexus team, il quale presenta il progetto e la squadra in modo completo, semplice ed intuitivo.