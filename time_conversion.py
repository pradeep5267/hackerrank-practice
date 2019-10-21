#%%
def timeConversion(s):
    tmp = str(s[-2:])
    hh = int(s[:2])

    if (hh < 0 or hh > 23):
        return 'False'

    if (tmp==str('PM')):
        if (hh==12):
            return s[:-2]
        else:
            return str(hh+12)+s[2:-2]

    if(tmp == str('AM')):
        if(hh == 12):
            return '00'+s[2:-2]
        else:
            return s[:-2]

    
timeConversion('12:05:45PM')
#%%
