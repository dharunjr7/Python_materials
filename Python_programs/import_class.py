import Classexercies

if __name__ == '__main__':
    
    excel1 = 'adult.xlsx'
    excel2 = 'IPL.xlsx'
    excel3 = 'Drinks.xlsx'
    filepath1 = r'csvfiles\adult.csv'
    filepath2 = r'csvfiles\IPL.csv'
    filepath3 = r'csvfiles\drinks.csv'
    
    
    f1 = Classexercies.Excelwrite(filepath1, excel1)
    f1.exceloutput()
    
    f2 = Classexercies.Excelwrite(filepath2, excel2)
    f2.exceloutput()
    
    f2 = Classexercies.Excelwrite(filepath2, excel2)
    f2.exceloutput()
    