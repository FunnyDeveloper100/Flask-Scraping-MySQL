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

1. Use the domains-csv.py code to import the data into a MySQL database. (Please intergrate this into the test app)
2. Create a basic front end CRUD application in Flask that can access and display the data. (You can use any flask extention you want, but must include a requirements.txt.)
3. Use any opensource Bootstrap theme you like for the front end.
4. Allow a user to create and save searches on this data. 
5. You will need to create another MySQL table to store the user searches and results. (Your script must create the table etc)
6. For each search the user creates there are Three fields: SearchID, Search and ResultsData.  
7. For the search field the user must be able to enter: %WORDSEARCH% which is the same as Like%...% in Mysql. (ie Wildcard search)
8. These searches get saved in the new MySQL table.
9. The user can also delete searches.


# set up project using docker

1. install docker and docker-compose
- enabling docker repository
    ```sudo apt-get update```
	
    ```sudo apt-get install apt-transport-https ca-certificates curl software-properties-common```

    ```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```
	
    ```sudo apt-key fingerprint 0EBFCD88```
	
    ```sudo add-apt-repository "deb [arch=amd64]   https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"```
- install docker-ce
    ``` sudo apt update```
    ```sudo apt install docker-ce ```
- install docker-compose
    ```sudo curl -L  "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```

    ```sudo chmod +x /usr/local/bin/docker-compose```

    ```docker-compose --version```
2.  install git on ubuntu
	  ```sudo apt-get update```
	
	  ```sudo apt-get install git```

3. cloning project from repository
	  ```git clone git@github.com:FunnyDeveloper100/Flask-Scraping-MySQL.git ```
	
	  ```cd working directory```
4. run docker image
	  if mysql server is running on ubuntu already, please stop mysql server by run ```sudo service mysql stop```
	
	  ```docker-compose up```
5. run entrypoint script
	  ```docker exec flask_app sh docker-entrypoint.sh```

6. link the url [localhost:8001](http://localhost:8001)


