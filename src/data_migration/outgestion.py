import psycopg2

def writeToDB(dictionary, connection):
    """
    Take columnar data stored in
    a dictionary and write
    them to the database
    """
    cursor = connection.cursor()
    ## sort the keys
    sorted_keys = tuple(sorted(dictionary.keys()))
    ## create the iterator
    iterator = zip(*[dictionary[key] for key in sorted_keys])
    ## assemble the query
    query = "INSERT INTO items "+str(sorted_keys)+" VALUES (%s, %s, %s, )"
    ## loop for the range of the index
    for line in iterator:
        query = "INSERT INTO items "+str(sorted_keys)+" VALUES "+str(line)
        cursor.execute(query)
    ## commit the connection as a batch
    connection.commit()