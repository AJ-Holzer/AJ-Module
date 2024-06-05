import zipfile, os

def create_zip(
        paths:list[str],
        name:str = "Your_Zip",
        compression:str = "deflate",
        compressLevel:int = 0
    ) -> None:
    """
    Creates a zip with the following things provided:\n
    path           = The path which will be added to the zipfile (directory or file)\n
    name           = The name of the Zipfile\n
    compression    = What compression type will be used ["zip", "deflate", "bzip2", "lzma"]\n
    compressLevel  = The level of compression\n
    """

    # Determine the compression method
    if compression == 'zip':
        new_compression = zipfile.ZIP_STORED
    elif compression == 'deflate':
        new_compression = zipfile.ZIP_DEFLATED
    elif compression == 'bzip2':
        new_compression = zipfile.ZIP_BZIP2
    elif compression == 'lzma':
        new_compression = zipfile.ZIP_LZMA
    else:
        raise ValueError(f"Unsupported compression type: {compression}")
    
    with zipfile.ZipFile(
        name + ".zip",
        "w",
        compression=new_compression,
        compresslevel=compressLevel,
        ) as f:

        if paths:
            try:
                for path in paths:
                    # If the path is a directory, add all its contents
                    if os.path.isdir(path):
                        for root, _, files in os.walk(path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, start=path)
                                f.write(file_path, arcname=arcname)
                    else:
                        # If the path is a file, add just this file
                        f.write(path, arcname=os.path.basename(path))
            except:
                raise Exception("PathNotFound", "The path you provided could not be found!")