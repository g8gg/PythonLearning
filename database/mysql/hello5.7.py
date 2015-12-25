# MySQL.com connector 2.1.3
# Connection of MySQL 5.7.9
import mysql.connector
from pprint import pprint

"""
Using the Connector/Python C Extension

  As of Connector/Python 2.1.1, the use_pure connection argument determines whether to connect
using a pure Python interface to MySQL, or a C Extension that uses the MySQL C client library
(see Chapter 8, The Connector/Python C Extension). The default is True (use the pure Python implementation).
Setting use_pure to False causes the connection to use the C Extension if your Connector/Python
installation includes it.
  The following examples are similar to others shown previously but with the includion of use_pure=False.
"""
cnMySQL = mysql.connector.connect(user='root', password='mememe',
                                  host='127.0.0.1',
                                  database='DDZB',
                                  use_pure=False
                                  )
print(cnMySQL._server_version)
cnMySQL.close()

from mysql.connector import (connection, errorcode)

config = {
    'user': 'root',
    'password': 'mememe',
    'host': '127.0.0.1',
    'database': 'DDZB',
    'raise_on_warnings': True,
}

try:
    cnx = connection.MySQLConnection(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print(cnx.charset)
    statement = "select * from mysql.user"
    for result in cnx.cmd_query_iter(statement):
        if 'columns' in result:
            columns = result['columns']
            # pprint(result)
            rows = cnx.get_rows()
            # pprint(columns)
            pprint(rows)

    cnx.close()
