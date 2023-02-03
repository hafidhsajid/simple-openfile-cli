# Simple open log file using python

## Documentation
usage: `openfile.py [-h] [-o OUTPUTFILE] [-t TYPE] input`

- positional arguments:

    | Command  | Function  |
    :-: | :-----------:
    input | Input file location


- options:
    | Command  | Function  |
    :-: | :-----------:
    -h, --help | show this help message and exit
    -o | Output file location default (output.txt)
    -t | Type file location

## Example Command


```
python3 openfile.py /var/log/apache2/access.log -o ~/Desktop/output.json -t json
```

```
python3 openfile.py /var/log/apache2/access.log -o ~/Desktop/output.json
```

```
python3 openfile.py /var/log/apache2/access.log -t text
```
```
python3 openfile.py /var/log/apache2/access.log -t json
```
