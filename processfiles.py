''' This module processes Dark Kitchen reports to extract raw data to a separate CSV file '''

import os
import pandas as pd
from filedialog import getfile
from filedialog import getfolder


#print(os.getcwd())

# get folder reports are in
srcfolder = getfolder("C:\\Users\\NMacewan\\", "Please select folder with files to be processed")

#print(srcfolder)

# get folder files with extracted data to be saved to
dstfolder = getfolder("C:\\Users\\NMacewan\\", "Please select folder to save raw data to")

#print(dstfolder)

# get reports to be processed
filenames = getfile(srcfolder, True)

for idx, path in enumerate(filenames):

    # read raw data from first sheet in file
    data = pd.read_excel(path, sheet_name=0, skiprows=6, usecols="A:F")

    #print(data)

    # remove the rows with na
    data = data.dropna()

    # convert the Class. No column to integer
    data['Class. No'] = data['Class. No'].astype(int)

    #print(data)

    #print(data.dtypes)

    # get original filename
    filename = os.path.basename(path)

    # extract site name number from filename
    site = filename[filename.index('Site')+5:-5]

    # format filename if required
    if site.isnumeric():
        site = f'{int(site):03d}'

    # filename for CSV with raw data extract
    rawfilename = '4543-LON Site' + site + '.csv'

    # save raw data to CSV in specified destination folder
    data.to_csv(dstfolder + '/' + rawfilename, index=False)

    #
    print(f'{filename} processed\n Raw data file saved in {dstfolder} as {rawfilename}')
