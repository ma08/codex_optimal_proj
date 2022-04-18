

import os
import gzip
import shutil
import glob

for file in glob.glob("*.gz"):
    with gzip.open(file, 'rb') as f_in:
        with open(file[:-3], 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    os.remove(file)
