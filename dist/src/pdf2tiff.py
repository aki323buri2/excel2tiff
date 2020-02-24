from pdf2image import convert_from_path 
from pathlib import Path 
import os

poppler = Path(__file__).parent / '../poppler-0.68.0/bin'
os.environ['PATH'] += os.pathsep + str(poppler.resolve())

def pdf2tiff(pdf, folder = None):
  pdf = Path(pdf)
  folder = pdf.parent if not folder else folder 

  pages = convert_from_path(str(pdf.resolve()))
  max = len(pages)
  keta = len(str(max))

  tiff = []
  for i, page in enumerate(pages):
    name = '{} ({}-{})'.format(
      pdf.stem , 
      str(i+1).zfill(keta), 
      str(max).zfill(keta), 
    )
    filename = (folder / name).with_suffix('.tiff').resolve()
    page.save(str(filename), 'TIFF')
    tiff.append(str(filename))

  return tiff