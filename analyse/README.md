# Analyse
Code für die Analyse der Parlamentsdokumente. Ziel hier war, Einsichten in den Datensatz zu erhalten.
Die Arbeit gliedert sich in 4 Teilaspekte:

- OST-preprocessing: Das Herunterladen der Parlamentsdokumente und die Extraktion der Texte
- llama_zusammenfassung: Mit Hilfe einer lokalen LLama2-Installation wurden Zusammenfassungen und Verschlagwortungen erstellt.
- notebooks: Enthält Notebooks zur Analyse der Textdokumente
- Daten Enthält Excel-Dateien, welche die auf der [Opendata-Plattform der Stadt St.Gallen](https://daten.stadt.sg.ch/explore/dataset/traktandierte-geschaefte-sitzungen-stadtparlament-stgallen/table/?disjunctive.legislatur&disjunctive.geschaeftstyp&disjunctive.gliederung&disjunctive.gliederungsnummer&disjunctive.ebene1&disjunctive.ebene2&disjunctive.ebene3&disjunctive.ebene4&disjunctive.ebene5&disjunctive.ebene6&disjunctive.traktandenstatus&sort=nr) bereitgestellten Daten erweitern, insbesondere um die Extrahierten Texte und zusätzliche semantische Informationen.


### Vorgehen

1. Llama wurden Themen vorgegeben und die KI angewiesen, jedem Geschäft das passende zuzuordnen. So wurde der Datensatz mit Hilfe bekannter Tools (pandas) erweitert.
2. Die Volltexte wurden nach Quartiernamen durchsucht, um so festzustellen, welche Geschäfte welchem Quartier zugeordnet werden können. (Oder nicht.) Auf diese Art wurde der Datensatz erweitert.
3. Mit ChatGPT-4 wurden ebenfalls Themen abgefragt, aber auch Prompts mitgegeben wie z.B. "Wie links oder rechts ist Vorstoss X?"
4. ChatGPT wurde mit den Datensätzen trainiert mit dem Ziel, die KI in einem Dashboard einzubetten.
5. Mit Power BI wurden Visualisierungen erstellt.
6. Ein Dashboard wurde erstellt, in das die genannten Ergebnisse einflossen.
