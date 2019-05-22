#masterarbeit

Das Ziel der vorliegende Masterarbeit ist es, die wichtigsten empirisches Erforschung
des maschinellen Lernens für eine bestmögliche Gestaltung der Vorhersage im Fehlerfall
des Reparierbaren Gerätes am Beispiel der Firma ’RATIONAL AG’ zu prognostizieren.
In dieser Arbeit wird die Methodik des maschinellen Lernens bestehende aus Vorher-
sage für Fehlerfall eingeführt. Grundsätzlich werden aus Beobachtung in Daten mittels
Methoden des maschinellen Lernens ein Modell extrahiert. Das Modell gibt eine Pro-
gnose aus, die mit Validierungsdaten verglichen wird. Die Nützlichkeit des maschinellen
Lernens hängen davon ab, wie korrekt ein Modell extrahiert wird und vor allem wie
viel Qualität die existierende Beobachtungsdaten hat und aus welche Struktur besteht.
Dies beschreibt erste Schritt der Ansätze im Auswahl des Modells. Anschließend wird
verraten, was im Hintergrund des maschinellen Lernens Methoden geschieht, welche
kaum von ML Entwickler gesehen wird.
Auswahl des Modells steht in einem engem Zusammenhang der Kenntnisse und Ein-
schätzung von ML Experten und Data Analysten basierend auf Verwendung der Lei-
stungskennzahlen. Diese Schritt wird sehr Mühsam und umständlich sogar verwirrend
sein.

Mittels Bildern, Texten, theoretischen Aussagen und sowie empirische Beobachtung
der Ausgabe wird diese Arbeit durchgeführt. Wobei die Bildern wird verwendet, um
die Ergebnis der Algorithmen darzustellen, welche in Python programmiert und imple-
mentiert wurden.
Es wird die verfügbare Daten der Firma RATIONAL Basis der reparierten Geräten
betreut durch Technical Service Abteilung analysiert. Dazu werden die Daten im laufe
der Jahren 2009 bis 2018 verglichen. Danach wurden diese Erkenntnisse mittels maschi-
nelles Lernalgorithmen in Python verarbeitet und die Prognose entwickelt. Die Basis
der Arbeit ist fachliche Kompetenz und Programmierkenntnisse des Verfassers sowie
seine Erforschungen bzw. technische Erfahrungen im Rahmen der Studium und Ar-
beit. Vor allem Betreuung der Arbeit durch die Fachleuten in beiden Seiten setzt die
Aktivitäten der Erforscher in richtigen Weg ein.
Mit Blick auf graphische Darstellung der Prognose wird gewonnen, dass die Qualität
der sogenannte intelligente Geräte tendenziell steigend ist.
Zu diesem Thema viele fachliche und wissenschaftliche Standpunkte und Beweise exi-
stieren, dass in dieser Arbeit in einem ersten Schritt als theoretische Hintergrund an die
Reihe kommen. Um diese mathematische und statistische Verfahren für die Schätzung
der Effekte zu anwenden, wird Literaturquelle angegeben.

42

Vorwort
Diese Forschungsstudie ist eine wissenschaftliche Arbeit im Rahmen der Abschlussar-
beit im Masterstudiengang, zwischen der Technische Hochschule Deggendorf und der
Firma RATIONAL.
“Hochschule Deggendorf hat sich seit der Gründung im Jahr 1994 die Technische Hoch-
schule Deggendorf (THD) zum innovativen Vorreiter in der Hochschullandschaft ent-
wickelt. Am 1. Oktober startete die Hochschule mit einer neuen Höchstzahl von fast
7000 Studierenden in das Wintersemester 2018/19.”
Die Firma RATIONAL ist einer der weltweit größten Hersteller für gewerbliche Küchen-
geräte. Eine Reparatur der Geräte ist möglich, dies tritt jedoch nur zu einem kleinem
Prozentsatz während der oder außerhalb von Garantie ein. ’Time to Failure’ ist für die
Hersteller eine wichtige Kennzahlung, da diese Reparaturen mit Kosten für die Firmen
verbunden sind. ’Time to Failure’ beschreibt die Dauer zwischen der Installation und
dem ersten Fehlerfall. Ziel des praktischen Teils der Masterarbeit ist die sogenann-
te ’Time to Failure’ zu prognostizieren. Diese Vorhersage wird mittels maschinellen
Lernalgorithmen prognostiziert.

3

Einleitung
In dieser Arbeit sollen maschinelle Lernmethoden, welche zur prognostischen Ermitt-
lung zukünftiger Werte jedoch passend zu der existierte Reparatur-Datenstruktur be-
troffen sind, evaluiert werden. Daher werden bei der Durchführung vier Hauptbereiche
angesprochen: (1) Definition und Vorstellung der Künstliche Intelligenz (KI) und Ma-
schinelles Lernen (ML) Methoden, (2) Evaluation der betroffene Algorithmen des ma-
schinellen Lernens, (3) Auswertungen und Analysieren der Daten, welche jedoch zuvor
in Praktischer Teil umstrukturiert bzw. vorverarbeitet werden sollen und schließlich die
Implementierung in Python und (4) Beschreibung der Anwendung von ML Algorith-
men in der entwickelten Applikation für die Firma RATIONAL, welche im vorherigen
Schritt erläutert wurden.
Alle ML prognostische Algorithmen treffen sich nicht zu der allen Datenstrukturen,
daher werden nicht alle Algorithmen im zweite Schritt betrachtet. In Beschreibung der
ML Methoden fokussiert sich diese Arbeit auf Anwendung und Optimierung der ML
Algorithmen, was in praktische Anwendung der Arbeit verwandt sind.
