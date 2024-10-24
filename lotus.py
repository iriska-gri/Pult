from __future__ import division, print_function
import os, uuid
import itertools as it
from win32com.client import Dispatch
import pywintypes # for exception
import datetime
import string
import pythoncom
from pathlib import Path
import loadprops

def lotusSender():
    session = Dispatch('Lotus.NotesSession')
    session.Initialize('12345')
    proper = self.load_proper()
    db = session.getDatabase('Lotus9966/M9966/МНС', 'mail\{}.nsf'.format(proper['LotusServerFile']))
    home = Path.home()

    if not db.IsOpen:
        try:
            db.Open()
        except pywintypes.com_error:
            print( 'could not open database: {}'.format(db_name) )

    doc = db.CreateDocument()
    doc.ReplaceItemValue("Form","Memo")
    doc.ReplaceItemValue("Subject",'Thema')

    # assign random uid because sometimes Lotus Notes tries to reuse the same one
    uid = str(uuid.uuid4().hex)
    doc.ReplaceItemValue('UNIVERSALID',uid)

    # "SendTo" MUST be populated otherwise you get this error: 
    # 'No recipient list for Send operation'
    doc.ReplaceItemValue("SendTo", "Виталий В Сапунов")

    #if copyto is not None:
        #doc.ReplaceItemValue("CopyTo", copyto)
    #if blindcopyto is not None:
        #doc.ReplaceItemValue("BlindCopyTo", blindcopyto)

    # body
    body = doc.CreateRichTextItem("Body")
    body.AppendText("dsfsdgfsdfsdf")
    attach = [home.joinpath('Desktop','Project', 'Lotus python','l.py')]
    # attachment 
    if attach is not None:
        attachment = doc.CreateRichTextItem("Attachment")
        for att in attach:
            attachment.EmbedObject(1454, "", att, "Attachment")

    # save in `Sent` view; default is False
    doc.SaveMessageOnSend = True
    doc.Send(False)

lotusSender()