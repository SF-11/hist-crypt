# hist-crypt
hist-crypt (Historical Cryptography) is a command-line utility to encrypt, decrypt, and sometimes crack, classical cryptographic ciphers.  
Currently, the following ciphers are implemented:  
* Affine
* Caesar
* Substitution
* Vignere
* ADFGVX


## Usage
```
Usage: hist-crypt.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help          Show this message and exit.
  
Commands:
  affine
  caesar
  substitution
  vignere
```

### Affine
```
Usage: hist-crypt.py affine [OPTIONS]

Options:
  -f, --file FILENAME             name of file containing text or stdin if
                                  blank
  -a [1|3|5|7|9|11|15|17|19|21|23|25]
                                  [required]
  -b INTEGER                      [required]
  -d, --decrypt
  --help                          Show this message and exit.
```

### Caesar
```
Usage: hist-crypt.py caesar [OPTIONS]

Options:
  -f, --file FILENAME      name of file containing text or stdin if blank
  -k, --key INTEGER RANGE  [-26<=x<=26; required]
  --help                   Show this message and exit.
```

### Substitution
```
Usage: hist-crypt.py substitution [OPTIONS]

Options:
  -f, --file FILENAME     name of file containing text
  -m, --mapfile FILENAME  [required]
  --help                  Show this message and exit.

```

### Vignere
```
Usage: hist-crypt.py vignere [OPTIONS]

Options:
  -f, --file FILENAME  name of file containing text or stdin if blank
  -k, --key TEXT       [required]
  -d, --decrypt
  --help               Show this message and exit.

```

### ADFGVX
```
Usage: hist-crypt.py adfgvx [OPTIONS]

Options:
  -f, --file FILENAME       name of file containing text
  -k, --key TEXT            [required]
  -a, --alphafile FILENAME  File containing 5x5 or 6x6 ADFGV(X) subsititution
                            square, comma delimeters  [required]
  -d, --decrypt
  --help                    Show this message and exit.
```

### Playfair
```

```

### Bacon
```

```



## Setup Virtual Environment
pip install virtualenv  
python3 -m venv venv  
source venv/bin/activate (or: venv\Scripts\activate)  
pip install -r requirements.txt  


## Run Tests
python -m pytest --cov-report term-missing --cov
