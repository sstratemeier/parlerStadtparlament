# Open Data St.Gallen

Datendownload und -preprocessing sowie automatische Klassifikation von Parlamentsgeschäften 

## Einleitung

Wirtschaftsingenieurwesen Studierende im 6. Semester der Ostschweizer Fachhochschule in St.Gallen, haben von der Stadt St.Gallen und insbesodere Nicola Wullschleger (Projektmanager Open Data, Stadt St.Gallen) eine praxisorientierte Aufgabenstellung erhalten, um diese im Modul Machine Learning unter der Leitung des Dozenten Dr. Beat Tödli zu bearbeiten.




### Ausgangslage

Die Stadt St.Gallen betreibt seit September 2019 ein Open Data Portal auf dem unpersönliche, unkritische Daten der Stadtverwaltung veröffentlicht werden. Mit der Veröffentlichung von sogenannten Open Government Data (OGD) als maschinenlesbare Datensätze will die öffentliche Verwaltung einen Beitrag zur Förderung von Transparenz, Partizipation, und Innovation leisten. Neben Statistikdaten, Geodaten, Verkehrszähldaten oder Sensordaten gehören dazu auch Daten aus dem Politik- und Verwaltungs-Bereich, wie beispielsweise öffentliche Vergaben oder die städtischen Budgets.

Nun plant die Stadt St.Gallen die Veröffentlichung eines umfangreichen Datensatzes des städtischen Ratsinformationssystems. Darin beinhaltet sind die traktandierten Geschäfte des Stadtparlaments St.Gallen seit dem Jahr 2001. Den behandelten Geschäften sind verschiedenen Eigenschaften wie das Sitzungsdatum, die Art des Geschäfts, oder auch die Aktenplannummer (sprich das Thema) zugeordnet. Damit lassen sich die rund 4000 Geschäfte nicht nur thematisch filtern, sondern es lassen sich auch politikwissenschaftliche Analysen bspw. über die Themenschwerpunkte im Verlauf der Jahre durchführen.

### Problemstellung

Die Geschäfte des Stadtparlaments können grossmehrheitlich in zwei Arten unterteilt werden:

Die Sachgeschäfte, welche von Seiten der Verwaltung angestossen, bearbeitet und traktandiert werden (1750 Geschäfte).
Die Parlamentarischen Vorstösse, bestehend aus Interpellationen, Motionen und Einfachen Anfragen, welche von Seiten der Stadtparlamentarierinnen und Stadtparlamentariern eingebracht werden (1840 Geschäfte).

Während die Sachgeschäfte einer thematischen Aktenplannummer wie Schule, Kultur, Entsorgung, etc. zugeordnet werden, erhalten die parlamentarischen Vorstösse eine Aktenplannummer nach der entsprechenden Geschäftsart. Dies führt zu folgender thematischer Häufung der Geschäfte.

 
Erläuterung: Die erste Säule "Stadtparlament" wird durch die grosse Anzahl an parlamentarischen Vorstössen bestimmt, während die Sachgeschäfte in die restlichen Kategorien eingeteilt werden.

Diese Verzerrung der Themen führt zu einem geringeren Mehrwert des Datensatzes, weil

die Filterung nach Aktenplannummer (Thema) unvollständige Resultate ergibt,
politische Themenanalysen nur die Sachgeschäfte und somit die Verwaltungsseite abdecken, und
damit ein politikwissenschaftlicher Vergleich der Geschäftsthemen zwischen Verwaltungsseite und Parlamentsseite verunmöglicht wird.

### Ziel

Während eine manuelle Neuzuordnung der parlamentarischen Vorstösse möglich wäre, ist sie ressourcentechnisch unrealistisch. Aus diesem Grund soll dieser Mangel des Datensatzes, mittels Data Mining kategorisiert werden. Ziel ist es, die parlamentarischen Vorstösse den bestehenden thematischen Kategorien zuzuordnen und die Genauigkeit der maschinellen Zuordnung auszuweisen. Fehlerhafte Zuordnungen sollen möglichst vermieden werden, um die Qualität der Filterfunktion des Datensatzes zu gewährleisten. Mittels der ausgewiesenen Genauigkeit könnten ungenaue Zuordnungen durch Verwaltungsmitarbeitende überprüft oder manuell zugeordnet werden. Damit kann die Machine Learning Anwendung den Nutzen des Datensatzes massiv steigern, während der manuelle Aufwand innerhalb der Verwaltung minimal gehalten wird.

### Datenstruktur

Die Themen, sprich die Aktenplannummern enthalten verschiedene Ebenen, welchen die Sachgeschäfte und parlamentarischen Vorstösse zugeordnet wurden. Die hierarchische Struktur des Aktenplans sieht wie folgt aus:

Ebene 1: 9 Kategorien
Ebene 2: 35 Kategorien
Ebene 3: 175 Kategorien
Ebene 4: 1094 Kategorien
etc.

Aus diesem Grund ist eine Zuordnung auf Basis von Ebene 2 realistisch. Der Aktenplan auf Ebene 2 beinhaltet 35 Kategorien, wovon 29 im vorliegenden Datensatz verwendet wurden. 12 Kategorien enthalten weniger als 20 Geschäfte, weshalb sie in der Kategorie "sonstige Themen" zusammengefasst wurden. Neben der Kategorie "Stadtparlament", in der die parlamentarischen Vorstösse enthalten sind, verbleiben somit die 17 folgenden Kategorien, welchen die Geschäfte zugeordnet werden sollen:

- Bürgerschaft					
- Entsorgung
- Finanzhaushalt					
- Kultur
- Organisation der Verwaltung		
- Schulen
- Soziales, Sozialhilfe			
- Sport
- Stadtrat						
- Stadtwerke
- Städtisches Personal			
- Umweltschutz
- Verkehr, Telekommunikation		
- Verkehrsbetriebe
- Öffentliche Ordnung und Sicherheit	
- Öffentliches Bauen
- Sonstige Themen

## Installation
### Code aus Gitlab holen
- in der Konsole 

		git clone ssh://git@gitlab.ost.ch:45022/beat.toedtli/opendatasg.git

ausführen.

### Anaconda virtuelles Environment generieren
- ev. bestehende Environments anzeigen:

		conda info --envs  
- ev. bestehendes Environment löschen:

		conda remove -n male --all

- [Virtual Environment generieren](https://de.acervolima.com/richten-sie-mit-anaconda-eine-virtuelle-umgebung-fur-python-ein/#google_vignette)

		conda env create -n male --file male.yml
		conda activate male
		pip install pdfplumber
		python -m spacy download de_core_news_md
		#ev. alternativ:
		python -m spacy download de_core_news_md --user

**Notiz: Mamba ist viel schneller als conda, daher die Empfehlung stattdessen dies zu benutzen:**

		mamba env create -n male --file male_mamba.yml
		conda activate male
		python -m spacy download de_core_news_md
		#ev. alternativ:
		python -m spacy download de_core_news_md --user

- Conda aktivieren

		conda activate male

## Daten herunterladen

		python daten-stadt-sg.py

## Ausführen der Erkennung
Mit 
	python main.py
wird die `inputcsv`-Datei (siehe `config.ini`) gelesen und um zusätzliche Spalten ergänzt, welche die Vorhersagen enthalten.

### Known Issues
- Pip und Conda passen nicht gut zusammen- leider gibt es aktuell kein brauchbares pdfplumber Paket in conda
- Die abgespeicherten Pickle-Dateien der Scikit-Learn-Klassifikatoren sind in älteren Scikit-Learn Versionen erstellt worden als die Scikit-Learn Version, die mit der `male.yml`-Datei installiert wird. Daher entstehen `UserWarning`-Warnmeldungen in der Konsole.

## Authors and Acknowledgment
Mitwirkende Studenten:
- Biel Luca
- Bucheli Mathias
- Hensch Andreas
- Vonplon Maurice
- Wagner Pascal
Dozierender und aktuell Repository-Verantwortlicher: 
- [Dr. Beat Tödtli](beat.toedtli@ost.ch)
Danke auch Nicola Wullschleger und der Open Data Plattform der Stadt St.Gallen für den Use Case!

## License
Aktuell ist der Code noch Closed-Source.

## Project status
Wird weiterentwickelt. Mitarbeit jederzeit willkommen!
