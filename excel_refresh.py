
import sys
import win32com.client

if len(sys.argv) < 2:
    sys.exit("Use: python excel_refresh.py file.xlsx")

xlsx = sys.argv[1]
print xlsx


xl = win32com.client.DispatchEx("Excel.Application")
wb = xl.workbooks.open(xlsx)
xl.Visible = True
wb.RefreshAll()

