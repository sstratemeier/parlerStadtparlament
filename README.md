# Open Data Hackathon Challenge

## Einleitung:

Im Rahmen des Open Data Hackathons steht die Stadt St.Gallen vor der Herausforderung, durch die Analyse der parlamentarischen Geschäfte einen tiefen Einblick in die Entwicklung und Konjunktur von Themen im Stadtparlament zu gewinnen. Diese Erkenntnisse sollen nicht nur die Datenanalysten, sondern vor allem die Bürgerinnen und Bürger der Stadt erreichen. Die Zusammenarbeit mit dem "St.Galler Tagblatt" und der Datenjournalistin Marlen Hämmerli unterstreicht das Bestreben, die gewonnenen Erkenntnisse in Form von aussagekräftigen Zeitungsartikeln der breiten Öffentlichkeit zugänglich zu machen.

## Ausgangslage:

Die politische Landschaft entwickelt sich ständig weiter, und das St.Galler Stadtparlament spielt eine zentrale Rolle bei der Diskussion und Entscheidung über verschiedene Themen. Um den Bürgern einen transparenten Einblick in die Aktivitäten und Interessen des Parlaments zu bieten, ist es entscheidend, die historische Entwicklung und den Fokus auf bestimmte Themen im Laufe der Zeit zu verstehen. Die Aufgabe besteht darin, durch Analyse von vorhandenen Daten und Einsatz von Machine Learning-Methoden verlässliche Informationen zu generieren. Dies ermöglicht nicht nur eine zeitliche Einordnung von Themen, sondern auch die Identifizierung von Schwerpunkten und Veränderungen in der politischen Agenda. Marlen Hämmerli, die selbst an der Challenge teilnimmt, strebt an, die gewonnenen Erkenntnisse durch Artikel im "St.Galler Tagblatt" zu verbreiten. Damit wird die Bedeutung von Open Data und Datenjournalismus bei der Schaffung von Transparenz und Verständnis in der Gemeinschaft hervorgehoben.

## Problemstellung:

Das Stadtparlament St.Gallen behandelt eine Vielzahl von Themen, und die Aufgabe besteht darin, einen Überblick über die zeitliche Entwicklung dieser Themen seit dem Jahr 2000 zu erstellen. Zusätzlich sollen Einblicke in die Themenkonjunktur nach Partei/Fraktion gewonnen werden. Die Herausforderung liegt darin, verlässliche Aussagen über folgende Punkte zu treffen:

- Wie oft hat sich das Stadtparlament mit einem bestimmten Thema beschäftigt?
- Welche Themen waren in einem bestimmten Jahr oder Zeitraum besonders wichtig?
- Wie hat sich die Themenkonjunktur über die Jahre/Jahrzehnte entwickelt?
- Welche Parteien/Fraktionen haben sich welchen Themen gewidmet, und wie hat sich das im Laufe der Zeit verändert?
- Gibt es spezifische Interessen, wie zum Beispiel schulische Themen bei der SP oder Finanzthemen bei der FDP?
- Gibt es Themen, die im Stadtparlament kaum je diskutiert werden?
- Hat sich die Behandlung von klimapolitischen Themen seit Fukushima im Vergleich zu früher verändert?

## Ziele & Erwartungen:

Während des Hackathons sollen Visualisierungen und Erkenntnisse über die Themenentwicklung im St.Galler Stadtparlament erstellt und interpretiert werden. Die Analyseansätze und Codebasis sollen weiterentwickelt werden oder es soll ein neuer Ansatz gefunden werden. Bei aufschlussreichen und verlässlichen Erkenntnissen plant Marlen Hämmerli vom "St.Galler Tagblatt", Zeitungsartikel zu den Ergebnissen zu verfassen. Mit der Codebasis plant sie auch, zukünftig Geschäfte zu analysieren, beispielsweise nach Ablauf einer Legislatur.

Als zweiter Schritt ist die Entwicklung eines interaktiven Dashboards oder einer Analyseplattform denkbar. Diese Plattform soll in die städtische Website eingebettet werden und es Laien ermöglichen, Analysen vorzunehmen.

## Ziele & Erwartungen:
- Marlen
- Raquel
- Beat
- Orhan
- Till
- Tobi
- Simon

## Ressourcen:

- Ein Datensatz auf der Open-Data-Plattform der Stadt St.Gallen: "Traktandierte Geschäfte in Sitzungen des Stadtparlaments St.Gallen (RIS – Ratsinformationssystem)". Der Datensatz enthält auch Links zu den Sitzungsprotokollen des Stadtparlaments.

- Eine Kaggle-Competition (kaggle.com/competitions/male-stgallen-recommender) mit einer detaillierten Problembeschreibung.

- Code von Studierenden (bei Beat Tödtli beziehbar). Der Code ermittelt eine Vorhersage des Themas aufgrund der Titel der Geschäfte und den Kategorien aus dem Aktenplan. Das Machine Learning Modell muss jedoch weiterentwickelt werden, um die Verlässlichkeit bedeutend zu erhöhen.

## Funktionen der Plattform

Die entwickelte Plattform bietet eine Vielzahl von Funktionen, um die Anforderungen der Hackathon-Challenge zu erfüllen und den Zugang zu den Daten des Stadtparlaments St.Gallen zu erleichtern.

## Visualisierungen und Dashboards

Die Plattform integriert Grafiken, Diagramme und Dashboards, die durch Power BI erstellt wurden. Diese Visualisierungen bieten einen intuitiven Überblick über die zeitliche Entwicklung und die Schwerpunkte der behandlungsbedürftigen Themen im St.Galler Stadtparlament seit dem Jahr 2000. Die Integration von Power BI ermöglicht zudem die einfache Einbettung und Aktualisierung von Dashboards über das Power BI REST API.

## Onelake Data Hub

Die Plattform nutzt den Onelake Data Hub, um Daten effizient zu speichern und abzurufen. Dies ermöglicht eine nahtlose Integration von neuen Informationen durch den Power Query Editor UI. Damit haben die Teilnehmer und Entwickler die Flexibilität, die Datenbank mühelos zu aktualisieren und auf aktuelle Entwicklungen im Stadtparlament zu reagieren.

## KI Chatbot

Die Plattform enthält einen KI-gesteuerten Chatbot, der mithilfe des ChatGPT API integriert wurde. Dieser Chatbot ermöglicht den Nutzern, auf natürliche Weise mit der Plattform zu interagieren. Benutzer können dem Chatbot Fragen zu spezifischen Themen, Parteien oder Entwicklungen stellen und erhalten sofortige, automatisierte Antworten. Der KI-Chatbot verbessert die Benutzerfreundlichkeit und ermöglicht einen schnellen Zugriff auf relevante Informationen.

## Programmiersprachen

Die Plattform bietet mehrsprachige Unterstützung, um sicherzustellen, dass eine breite Palette von Nutzern Zugang zu den Informationen hat. Durch die Implementierung von Javascript, HTML, CSS, Svelt für das Frontend und Python, R für das Backend wird eine vielseitige Plattform geschaffen, die auf unterschiedlichen technologischen Hintergründen basiert.

Die Kombination dieser Funktionen macht die Plattform zu einem leistungsfähigen Werkzeug, um verlässliche Erkenntnisse über die Themen im St.Galler Stadtparlament zu gewinnen und diese Informationen auf eine zugängliche Weise der Bevölkerung zu präsentieren.