# SecureFlow-Vault

Dieses Projekt habe ich entwickelt, um die Konzepte von Datenschutz (Privacy) und Verschlüsselung in der Praxis anzuwenden. Es ist eine Pipeline, die sensible Daten in Berichten automatisch bereinigt und anschließend sicher verschlüsselt.

### Was das Tool macht:
* **Bereinigung (Scrubbing):** Das Skript nutzt Regular Expressions (Regex), um E-Mail-Adressen in Textdateien zu finden und diese durch `[REDACTED]` zu ersetzen.
* **Verschlüsselung:** Mit der `cryptography`-Library (AES-128) wird die bereinigte Datei verschlüsselt, sodass sie ohne den passenden Schlüssel nicht lesbar ist.
* **Entschlüsselung:** Ein separates Skript (`decrypt.py`) stellt die Daten für autorisierte Nutzer wieder her.

### Projektstruktur:
* `vault.py`: Das Hauptskript für die Bereinigung und Verschlüsselung.
* `decrypt.py`: Das Skript zum Entschlüsseln der Daten.
* `requirements.txt`: Liste der benötigten Libraries (cryptography).
* `secret.key`: Der vom Skript generierte Schlüssel (wird lokal erstellt).

### Installation und Nutzung:
1. Benötigte Tools installieren: 
   `pip install cryptography`
2. Daten verschlüsseln: 
   `python vault.py`
3. Daten wieder lesbar machen: 
   `python decrypt.py`

*Hinweis: Dieses Projekt entstand im Rahmen meines Studiums (Fokus Security & Compliance), um den Schutz von "Data-in-Transit" zu simulieren – ein wichtiges Thema im modernen Banking.*
