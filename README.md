# 
 
# TechemTools-SQL2CSV

Questo script Python converte un file CSV in istruzioni SQL INSERT compatibili con MariaDB, con particolare attenzione alla formattazione delle date.

## Funzionalità

- Legge un file CSV con campi separati da punto e virgola (;)
- Converte le date dal formato MM/GG/AAAA al formato AAAA-MM-GG
- Genera istruzioni SQL INSERT per MariaDB
- Gestisce l'escape dei caratteri speciali nelle stringhe
- Supporta l'encoding UTF-8

## Requisiti

- Python 3.x

## Utilizzo

1. Salvare lo script in un file, ad esempio `csv_to_mariadb.py`
2. Aprire il prompt dei comandi di Windows
3. Navigare alla directory dove è stato salvato lo script
4. Eseguire il comando:

   ```
   python csv_to_mariadb.py <percorso_del_file_csv> <nome_tabella>
   ```

   Dove:
   - `<percorso_del_file_csv>` è il percorso completo del file CSV da convertire
   - `<nome_tabella>` è il nome della tabella MariaDB in cui verranno inseriti i dati

5. Per salvare l'output in un file SQL, utilizzare:

   ```
   python csv_to_mariadb.py <percorso_del_file_csv> <nome_tabella> > output.sql
   ```

## Formato del CSV

- Il file CSV deve utilizzare il punto e virgola (;) come separatore
- La prima riga del CSV deve contenere i nomi delle colonne
- Le date devono essere nel formato MM/GG/AAAA (es. 09/30/2021)

## Output

Lo script genererà istruzioni SQL INSERT nel seguente formato:

```sql
INSERT INTO `nome_tabella` (`colonna1`, `colonna2`, ...) VALUES ('valore1', 'valore2', ...);
```

Le date nell'output saranno nel formato AAAA-MM-GG.

## Note

- Lo script gestisce automaticamente l'escape degli apici singoli nelle stringhe
- Utilizza l'encoding UTF-8 per la lettura del file CSV e per l'output
- In caso di errori di codifica, i caratteri non riconosciuti verranno sostituiti

## Risoluzione dei problemi

Se si incontrano problemi con la codifica dei caratteri, assicurarsi che il file CSV sia salvato con encoding UTF-8.

Per qualsiasi altro problema o richiesta di funzionalità aggiuntive, si prega di aprire una issue su GitHub o su Teams.