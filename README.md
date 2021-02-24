# Hasher

Questo programma ha lo scopo di creare, a partire da un file dizionario, un secondo file contenente tutte le entry presenti nel primo codificate con l'algoritmo di hash selezionato.<br><br>


## Installazione
Nessuna installazione richiesta.<br>
Nessuna libreria richiesta.<br><br>


## Uso
```
$ python3 hasher.py -d my_dict.txt -f <algoritmo di hashing>
```

Gli algoritmi supportati sono:
- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512
- SHA3_224
- SHA3_256
- SHA3_384
- SHA3_512
<br><br>

## Note
- Tipicamente non dovrebbero esserci problemi per qualsiasi versione di Python dalla 3.6 in poi
- Hasher utilizza la libreria ```hashlib``` di python, pertanto le funzioni di hashing SHA3 e BLAKE dipendono dalla libreria ```OpenSSL``` dalla versione 1.1.1 in poi.