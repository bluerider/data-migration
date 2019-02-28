import zipfile

def unzipFile(file):
    """
    Extract file to tempdir and return tempdir
    """
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(file, "r") as zip_ref:
        zip_ref.extractall(tempdir)
    return(temp_dir)