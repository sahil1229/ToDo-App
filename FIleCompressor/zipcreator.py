import zipfile

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(dest_dir,"w") as archive:
        for filepath in filepaths:
            archive.write(filepath)