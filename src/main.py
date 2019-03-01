import sys, glob
from data_migration import ingestion, outgestion, utils

def main(zip_file, database):
    """
    Extract files to a temporary directory and
    write results to postgres
    """
    ## create a temporary directory
    temp_dir = ingestion.unzipFile(zip_file)
    ## locate newly unzipped files
    json_files = glob.glob('/'.join([temp_dir,"*.json"]))
    ## loop for all files in found json files
    for file in json_files:
        ## get columnar table
        temp_dict = utils.jsonToColumnar(file)
        ## get the sql querie
        sql_queries = utils.compileSQLQueries(temp_dict)
        ## write the table to database
        outgestion.writeToDB(sql_queries, connection)

if __name__ == "__main__":
    zip_file = sys.argv[1]
    database = sys.argv[2]
    main(zip_file, database)