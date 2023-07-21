import csv
from openpyxl import Workbook

class Excelwrite:
    def __init__(self,file,excel):
        self.file=file
        self.excel=excel
        
    def exceloutput(self):
        wb = Workbook()
        sheet = wb.active
        
        self.fobj = open(self.file)
        reader = csv.reader(self.fobj)
        for records in reader:
            sheet.append(records)
        wb.save(self.excel)
        
     
if __name__ == '__main__':
    excelname = 'student_data.xlsx'
    filepath = r'csvfiles\students.csv'
    obj1 = Excelwrite(filepath,excelname)
    obj1.exceloutput()