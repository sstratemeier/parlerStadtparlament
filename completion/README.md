# Analyse von Sitzungsprotokollen des Stadtparlaments St. Gallen

## Über das Projekt

Dieses Projekt zielt darauf ab, Sitzungsprotokolle des Stadtparlaments St. Gallen zu analysieren und in auswertbare JSON-Dateien umzuwandeln. Es wurde mit dem Fokus auf Benutzerfreundlichkeit und Anpassbarkeit entwickelt, sodass es auch für Python-Einsteiger leicht verständlich ist. Das Projekt ermöglicht in seinem Aufbau eine inkrementelle Weiterentwicklung in Richtung Automatisierung und Schnittstellenimplementierung zu ermöglichen.

## Datengrundlagen/Datenquellen

Das Projekt verwendet öffentlich zugängliche Daten des Stadtparlaments St. Gallen. Diese Daten umfassen Sitzungsprotokolle, die in strukturierter Form analysiert werden.

## Datenverarbeitung

Die Datenverarbeitung erfolgt in mehreren Schritten:
1. Einlesen der Sitzungsprotokolle.
2. Analyse der Texte mithilfe von KI-Modellen.
3. Umwandlung der Ergebnisse in JSON-Format für einfache Weiterverarbeitung und Analyse.

## Verwendete APIs

- **OpenAI API:** Für die Textanalyse und Verarbeitung nutzen wir die OpenAI API.
- **Andere APIs:** (Falls weitere APIs verwendet werden, hier einfügen.)

## Architektur

Das Projekt folgt einer modularen Architektur, wobei jede Komponente für einen spezifischen Teil des Verarbeitungsprozesses verantwortlich ist. Dies fördert die Wartbarkeit und Erweiterbarkeit des Codes.

## Limitationen

- **Datenqualität:** Die Qualität und Genauigkeit der Analyse ist direkt abhängig von der Qualität der Eingangsdaten.
- **Sprachliche Einschränkungen:** Derzeit ist das System auf Texte in deutscher Sprache optimiert.

## Weiterentwicklung

Zukünftige Erweiterungen könnten beinhalten:
- Automatisierung des Datenerfassungsprozesses.
- Implementierung weiterer Sprachen und Dialekte.
- Integration zusätzlicher Datenquellen zur umfassenderen Analyse.

## Einrichtung und Installation

Das Projekt ist mit Poetry aufgesetzt. Befolgen Sie diese Schritte, um es einzurichten und die erforderlichen Pakete zu installieren:

1. **Python installieren**: Stellen Sie sicher, dass Python auf Ihrem System installiert ist. Sie können es von [python.org](https://www.python.org/downloads/) herunterladen.

2. **Poetry installieren**: Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus, um Poetry zu installieren:
   ```shell
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Klonen des Repositories:**  
   `git clone https://github.com/tobit0101/open_data_hack_2023.git`

4. **Wechseln in das Projektverzeichnis:**  
   `cd open_data_hack_2023`

5. **Installieren der Abhängigkeiten mit Poetry:**  
   `poetry install`

## Nutzung

Das Projekt ist so konzipiert, dass es einfach zu bedienen und anzupassen ist. Konstanten und Variablen können am Anfang des Codes angepasst werden, um das Verhalten des Programms zu ändern. Folgen Sie diesen Schritten, um das Programm auszuführen:

1. **Anpassen der Konfigurationsvariablen:**  
   Öffnen Sie die Konfigurationsdatei und passen Sie die erforderlichen Variablen an Ihre Bedürfnisse an.

2. **Ausführen des Skripts:**  
   Starten Sie das Skript mit `poetry run python main.ipynb`.

## Code-Struktur und Logik

- **Konstanten und Konfiguration:**  
  Zu Beginn des Skripts können Sie Konstanten und Einstellungen anpassen.

- **Funktionen:**  
  Jede Funktion ist selbsterklärend benannt und in klare Abschnitte unterteilt, um die Verständlichkeit und Wartbarkeit zu erhöhen.

- **Datenverarbeitung:**  
  Der Code liest die Eingabedaten, verarbeitet sie mit Hilfe von KI-Modellen und speichert die Ergebnisse in JSON-Dateien, wobei jede Datei einem Datensatz entspricht.

- **Erweiterbarkeit:**  
  Der Code ist so strukturiert, dass er leicht erweitert und mit zusätzlichen Funktionen oder Schnittstellen ausgestattet werden kann.


