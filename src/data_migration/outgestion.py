import psycopg2

def writeToDB(sql_statements, connection):
    """
    Take a list of sql statements and
    write them to a databse
    """
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
    ## commit the connection as a batch
    connection.commit()