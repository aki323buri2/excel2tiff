from pathlib import Path 
from win32com import client as win32 

def excel2pdf(xlsx, folder = None):
  xlsx = Path(xlsx)
  folder = xlsx.parent if not folder else Path(folder)
  pdf = (folder / xlsx.name).with_suffix('.pdf')

  with Excel(str(xlsx.resolve())) as excel:
    excel.to_pdf(str(pdf.resolve()))

  return pdf.resolve()

class Excel :
  def __init__(self, path):
    self.app = win32.Dispatch('Excel.Application')
    self.book = self.app.Workbooks.Open(path)
    self.app.Visible = True 

  def __enter__(self):
    return self 
  
  def __exit__(self, type, value, stack):
    if not self.book:
      self.book.Close()
    self.app.Quit()
  
  def to_pdf(self, path):
    self.book.Worksheets.Select()
    self.book.ExportAsFixedFormat(0, path)
    return path