import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print('Что сказать?')
    s = input( )            #You can type in 中文 or English
    speaker.Speak(s)