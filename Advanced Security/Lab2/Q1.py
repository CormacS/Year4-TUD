message1 = 'RQH YDULDWLRQ WR WKH VWDQGDUG FDHVDU FLSKHU LV ZKHQ WKH DOSKDEHW LV "NHBHG" EB XVLQJ D ZRUG. LQ WKHWUDGLWLRQDO YDULHWB, RQH FRXOG ZULWH WKH DOSKDEHW RQWZR VWULSV DQG MXVW PDWFK XS WKH VWULSV DIWHU VOLGLQJWKH ERWWRP VWULS WR WKH OHIW RU ULJKW. WR HQFRGH, BRXZRXOG ILQG D OHWWHU LQ WKH WRS URZ DQG VXEVWLWXWH LWIRU WKH OHWWHU LQ WKH ERWWRP URZ. IRU D NHBHG YHUVLRQ,RQH ZRXOG QRW XVH D VWDQGDUG DOSKDEHW, EXW ZRXOG ILUVWZULWH D ZRUG (RPLWWLQJ GXSOLFDWHG OHWWHUV) DQG WKHQZULWH WKH UHPDLQLQJ OHWWHUV RI WKH DOSKDEHW. IRU WKHHADPSOH EHORZ, L XVHG D NHB RI "UXPNLQ.FRP" DQG BRX ZLOO VHHWKDW WKH SHULRG LV UHPRYHG EHFDXVH LW LV QRW D OHWWHU.BRX ZLOO DOVR QRWLFH WKH VHFRQG "P" LV QRW LQFOXGHGEHFDXVH WKHUH ZDV DQ P DOUHDGB DQG BRX FDQW KDYHGXSOLFDWHV.'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(alphabet)):
    decrypted = ''
    message = message1.upper()
    for letter in message:
        if letter in alphabet:
            #Subtracting the key to get the correct letter
            num = alphabet.find(letter)
            num = num - key
            if num < 0:
                num = num + len(alphabet)
            decrypted = decrypted + alphabet[num]
        else:
            decrypted = decrypted + letter
    print('\nKey %s: %s' % (key, decrypted))
