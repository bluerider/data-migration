import sys, tempfile, glob
import psycopg2
from data_migration import ingestion, outgestion, utils

def main(zip_file, database):
    """
    Extract files to a temporary directory and
    write results to postgres
    """
    ## create a temporary directory
    temp_dir = ingestion.unzipFile(zip_file)
    ## locate newly unzippes files
    json_files = glob.glob(temp_dir+"*.json")
    ## create the postgres connection
    connection = psycopg2.connect(database)
    ## loop for all files in found json files
    for file in json_files:
        ## get columnar table
        temp_dict = utils.jsonToColumnar(file)
        ## write the table to database
        outgestion.writeToDB(temp_dict, connection)

if __name__ == '__main__':
    zip_file = sys.argv[1]
    database = sys.argv[2]
    main(zip_file, database)