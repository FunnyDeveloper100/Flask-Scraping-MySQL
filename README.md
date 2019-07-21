Upload .au domains names CSV file to database

### Requirements:

* python 3+
* mysql-connector

```
usage: domains-csv.py [-h] [-v] [--database DATABASE] [--file FILE]
                      [--url URL]

Upload CSV to MySQL

optional arguments:
  -h, --help           show this help message and exit
  -v                   enable verbosity
  --database DATABASE  database to use
  --file FILE          local file to use
  --url URL            url to download file from
```
### Full download of domains https://ausdomainledger.net/au-domains-latest.csv.gz
### For testing use the smaller sample file in this repository
