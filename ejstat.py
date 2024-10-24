
from __future__ import division, print_function
from loadprops import Properties
import os, uuid
import itertools as it
import pywintypes # for exception
from win32com.client import Dispatch, DispatchEx,GetActiveObject
import pythoncom
from PIL import ImageGrab, Image
import uuid
from datetime import date
import pywintypes
import subprocess
from pathlib import Path


def excel_catch_screen(filename, sheetname, screen_area, img_name=False):
# """ Take a screenshot of the table area of ​​excel - use case: excel_catch_screen(ur"D:\Desktop\123.xlsx", "Sheet1", "A1:J10")"""
    
    pythoncom.CoInitialize() # excel multithreading related
    proper = Properties.load_proper()
    subprocess.Popen(proper['excel2013'])
    time.sleep(3)
    Excel = GetActiveObject('Excel.Application')
    Excel.Visible = True # Visualization
    Excel.DisplayAlerts = False # Whether to display warnings
    Wb = Excel.Workbooks.Open(filename) # Open excel
    Ws = Wb.Sheets(sheetname) # select sheet
    
    oldcount = int(Wb.Worksheets[0].Range("AT16"))
    count = Wb.Sheets.Count
    for i in range(count):
        ws = Wb.Worksheets[i]
        ws.Unprotect() # IF protected

        pivotCount = ws.PivotTables().Count
        for j in range(1, pivotCount+1):
            ws.PivotTables(j).PivotCache().Refresh()
            
        print ("Готовенько") 
    if  oldcount <= int(Wb.Worksheets[0].Range("AT16")):
        #не забудь потом убрать равно
        print ("Обновилось") 
        origfile  = "Y:\\WorkDocs\\Discharge\\Статистика ЦА Ежедневная %s По регионам.xlsx" %date.today()
        imagefile = "Y:\\WorkDocs\\Discharge\\Статистика ЦА Ежедневная %s По регионам Картинки.xlsx" %date.today()
        Wb.SaveAs(origfile)
        Ws.Range(screen_area).CopyPicture() # Copy image area
        workbook = Excel.Workbooks.Add()
        workbook.Sheets("Лист1").Paste(workbook.Sheets("Лист1").Range('A1')) # paste ws.Paste(ws.Range('B1')) # Move the image to a specific location
        
        sheet = workbook.Worksheets(1)
        Excel.ActiveWindow.DisplayGridlines = False
        workbook.SaveAs(imagefile)
        
        workbook.Close(SaveChanges=0)
        Wb.Close(SaveChanges=0) # Close the workbook, do not save
        Excel.Quit() # Exit excel
        pythoncom.CoUninitialize()
        
    else:
        print("Обновление не произошло")
    






def send_mail(subject,body_text,sendto,copyto=None,blindcopyto=None,
              attach=None):
    pythoncom.CoInitialize()
    session = Dispatch('Lotus.NotesSession')
    session.Initialize('12345')
    proper = Properties.load_proper()
    db = session.getDatabase('Lotus9966/M9966/МНС', 'mail\{}.nsf'.format(proper['LotusServerFile']))
    home = Path.home()
    if not db.IsOpen:
        try:
            db.Open()
        except pywintypes.com_error:
            print( 'could not open database: {}'.format(db_name) )

    doc = db.CreateDocument()
    doc.ReplaceItemValue("Form","Memo")
    doc.ReplaceItemValue("Subject",subject)

    # assign random uid because sometimes Lotus Notes tries to reuse the same one
    uid = str(uuid.uuid4().hex)
    doc.ReplaceItemValue('UNIVERSALID',uid)

    # "SendTo" MUST be populated otherwise you get this error: 
    # 'No recipient list for Send operation'
    doc.ReplaceItemValue("SendTo", sendto)

    if copyto is not None:
        doc.ReplaceItemValue("CopyTo", copyto)
    if blindcopyto is not None:
        doc.ReplaceItemValue("BlindCopyTo", blindcopyto)

    # body
    body = doc.CreateRichTextItem("Body")
    body.AppendText(body_text)

    # attachment 
    if attach is not None:
        attachment = doc.CreateRichTextItem("Attachment")
        for att in attach:
            attachment.EmbedObject(1454, "", att, "Attachment")

    # save in `Sent` view; default is False
    doc.SaveMessageOnSend = True
    doc.Send(False)
    pythoncom.CoUninitialize()

def excelandsend():

    
    origfile  = "Y:\\WorkDocs\\Discharge\\Статистика ЦА Ежедневная %s По регионам.xlsx" %date.today()
    imagefile = "Y:\\WorkDocs\\Discharge\\Статистика ЦА Ежедневная %s По регионам Картинки.xlsx" %date.today()
    excel_catch_screen(r"Y:\\WorkDocs\\Discharge\\statistics.xlsx", 1, "A1:N86")
    subject = "Статистика СООН по состоянию на %s" %date.today()
    body = "Добрый день. Направляю статистику по СООН по состоянию на %s" %date.today()
    sendto = ['Виталий В Сапунов']
    files = [origfile,imagefile]
    attachment = it.takewhile(lambda x: os.path.exists(x), files)

    # send_mail(subject, body, sendto, attach=attachment)
