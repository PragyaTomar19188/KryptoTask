# KryptoTask

Project Template

Import Psycopg2

Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of concurrent "INSERT"s or "UPDATE"s.

If prerequisites are met, you can install psycopg like any other Python
package, using ``pip`` to download it from PyPI_::

    $ pip install psycopg2
    
Give your connection details in the conn section to connect to Postgre database in your system!

Import flask

    $ pip install flask
    
The second way is to manually clone this repository and change it later by own.You need to clone and run:

```sh
$ mkdir Project
$ cd Project
$ git clone git@github.com:KryptoTask/mainn.git .
$ make
$ make run
```

Working and Approach:
- After completing the above steps make sure to enable "Less secure apps" for the gmail account you provide for Gmail SMTP to work properly. 
- Run the script mainn.py and it asks for User Email Address and Email Password for Gmail.
- Provide the details and the third input box asks for Amount you need to set the alert for BTC stock alert!
- Give the required amount and press submit
- The script generates the current BTC stock amount in console and checks for the given condition if the amount is less than the given condition it sends an alert to the persons gmail id.
- The script refreshes after every 10 mins to check if the condition still satisfies until the user gives a different value!
- For everytime the user sets a new value, it gets updated in the DB StockData under the Stock table
- Run the api endpoint /create/alert/{id} giving in the alert id to create a new alert in the system
- Run the api endpoint /delete/alert/{id} giving in the alert id to delete that id from the system

In case of anymore clarification please reach out to my email id: pragyatomar1918@gmail.com





