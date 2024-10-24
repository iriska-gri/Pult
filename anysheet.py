import datetime

def IcheckForPicture():
    # today = datetime.date(2021, 1, 1)
    today = datetime.date.today()
    if (datetime.date(today.year, 12, 20) <= today) or (today <= datetime.date(today.year, 1, 14)): 
        return ''
    elif datetime.date(today.year, 2, 20) <= today <= datetime.date(today.year, 2, 25):
        return '23'
    elif datetime.date(today.year, 3, 5) <= today <= datetime.date(today.year, 3, 11):
        return '8m'
    elif datetime.date(today.year, 4, 28) <= today <= datetime.date(today.year, 5, 3):
        return '1m'
    elif datetime.date(today.year, 5, 6) <= today <= datetime.date(today.year, 5, 12):
        return '9m'
    elif datetime.date(today.year, 6, 10) <= today <= datetime.date(today.year, 6, 13):
        return '12j'
    elif datetime.date(today.year, 11, 1) <= today <= datetime.date(today.year, 11, 6):
        return '4nov'
    elif datetime.date(today.year, 11, 18) <= today <= datetime.date(today.year, 11, 23):
        return '21n'
    elif  today.weekday()== 4:
        return 'pyat'