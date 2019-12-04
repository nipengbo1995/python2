def liststr(list):
    str = ''
    for i in list[:len(list)-1]:
        str = str + i + ','
    str = str + 'and '+ list[len(list)-1]
    return str
     
