import psycopg2

def writeToDB(sql_statements, database_url):
    ## create the postgres connection
    connection = psycopg2.connect(database_url)
    """
    Take a list of sql statements and
    write them to a databse
    """
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
    ## commit the connection as a batch
    connection.commit()