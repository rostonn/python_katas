string = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
string = 'map'
ans = ''
for char in string:
    if ord(char) > 96 & ord(char) < 123:
        number = ord(char) - 97
        if number == 24:
            newLetter = chr(97)
        elif number == 25:
            newLetter = chr(97+1)
        else:
            newLetter = chr(97+2+number)
        ans = ans + newLetter
        print '['+char+']='+newLetter+' = '+str(number)
    else:
        ans = ans+char


print(ans)
