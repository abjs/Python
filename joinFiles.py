import pandas as pd
import os
import glob
import csv
from xlsxwriter.workbook import Workbook
current_dir = os.getcwd()
files_path = os.path.join(current_dir, 'Files')
all_files = os.listdir(files_path)
csv_output = os.path.join(current_dir, 'compined.csv')
compined = []
for i in all_files:
    file = os.path.join(files_path, i)
    if os.path.isfile(file):
        data = pd.ExcelFile(file)
        for sheet in data.sheet_names:
            df = data.parse(sheet)
            df.to_csv(csv_output, mode='a', header=False, index=False)


for csvfile in glob.glob(csv_output):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
