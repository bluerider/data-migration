import zipfile, tempfile

def unzipFile(file):
    """
    Extract file to tempdir and return tempdir
    """
    ## make a temporary directory
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(file, "r") as zip_ref:
        ## extract all zip files to the temporary
        ## directory
        zip_ref.extractall(temp_dir)
    return(temp_dir)