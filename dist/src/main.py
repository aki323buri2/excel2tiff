from pathlib import Path 
import os, sys
import click 

root = Path(__file__).parent 
sys.path.append(str(root.resolve()))

from excel2pdf import excel2pdf 
from pdf2tiff import pdf2tiff 

backup = {
  'xlsx'        : root / 'excel' / '011_納品書_タテ型.xlsx', 
  'pdf_folder'  : root / 'pdf', 
  'tiff_folder' : root / 'tiff', 
}

@click.command()
@click.argument('xlsx')
@click.option('--pdf-folder', help='pdf folder')
@click.option('--tiff-folder', help='tiff folder')
def main(**option):

  for name, value in backup.items():
    option[name] = Path(option[name]) if option[name] else value
  
  xlsx = option['xlsx']
  pdf_folder = option['pdf_folder']
  tiff_folder = option['tiff_folder']

  for folder in [
    pdf_folder, 
    tiff_folder, 
  ]:
    folder.mkdir(parents=True, exist_ok=True)

  pdf = excel2pdf(xlsx, pdf_folder)
  tiff = pdf2tiff(pdf, tiff_folder)
  print(str(tiff))

if __name__ == '__main__':
  main()