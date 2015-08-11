
import win32com.client as win32
import os
import sys

def save_excel_charts (file, sheet, number_of_charts):
    excel = win32.gencache.EnsureDispatch('Excel.Application') 
    wb = excel.Workbooks.Open(file) 
    excel.Visible = True
    wb.Sheets(sheet).Select() 
    wbSheetOne = wb.Sheets(1) 
    wb.DisplayAlerts = False 

    count = int(number_of_charts)
    for index in range(1, count + 1):
        currentChart = wbSheetOne.ChartObjects(index)
        print currentChart.Name
        currentChart.Copy
        currentChart.Chart.Export(os.path.dirname(os.path.realpath(file)) + "/chart" + str(index) + ".png")

    wb.DisplayAlerts = True 
    excel.ActiveWorkbook.Close()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit("Use: python excel_save_charts.py excel.xlsx Sheet1 1")
    
    save_excel_charts(sys.argv[1], sys.argv[2], sys.argv[3])
