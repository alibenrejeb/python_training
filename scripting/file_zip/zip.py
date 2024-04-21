import zipfile
import shutil

# file_zip = zipfile.ZipFile("data/fichiers_zip.zip", "w", zipfile.ZIP_DEFLATED)
# file_zip.write("../file_excel/data/octobre.xlsx")
# file_zip.write("../file_excel/data/novembre.xlsx")
# file_zip.write("../file_excel/data/decembre.xlsx")
# file_zip.close()

# shutil.make_archive("data/archive", "zip", "../file_excel/data")

shutil.unpack_archive("data/archive.zip", "data/archive")
