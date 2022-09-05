import tabula
import pandas as pd


path = "https://omext.cancom.de/dam/?mdocs-file=10592&_ga=2.63385327.1360698842.1652388237-1052630406.1652191089&_gl=1*qrd42*_ga*MTA1MjYzMDQwNi4xNjUyMTkxMDg5*_ga_LQPDT87YP2*MTY1MjM4ODIzNi4zLjAuMTY1MjM4ODIzNi42MA"

df = tabula.read_pdf(path, pages = 'all')
for i in range(len(df)):
 df[i].to_excel('file_'+str(i)+'.xlsx')