message6 = 'FKDPD Fkd Pdslqgxcl sdprmd qd ylmdqd zdnh nxslwld xprmd zdr zd XYFFP,nlphpvkxnld dolbhnxzd Pzhqbhnlwl zd Wxph bd Pdedglolnr bd Ndwled, Mdml MrvhskZdulred, nlnlpwdnd ddfkh nxmlgdqjdqbd, nzdql vxdod od Ndwled psbd kdolzhcl nxzddmhqgd bd xfkdjxcl pnxx, pzdndql. Nzd xsdqgh zd XYFFP, lphpwdnd Mdml Zdulred,ddfkh pdud prmd nxwxpld gkdpdqd dolbrnxzd dphshzd bd nxzd Pzhqbhnlwl zd Wxph bdPdedglolnr bd Ndwled, nzdql pxgd zdnh xphlvkdpdolclnd nlvkhuld. Ndxol klcrclolwrohzd nzd qbdndwl wridxwl qd ylrqjrcl zd fkdpd klfkr, lnlzd ql vlnx fkdfkh wdqjxMdml Zdulred dwrh pdrql bdnh nxkxvldqd qd Udvlpx lolbrshqghnhczd qd Exqjh Pddoxpod Ndwled, dpedsr dolnrvrd nxwrndqd qd nxdfkzd nzd eddgkl bd pdrql bd zdqdqfkl.Dlgkd, dphhqghohd nxvlvlwlcd nxzd, dwdnxzd Udlv zd Zdwdqcdqld, elod nxmdol glql,ndelod dx ybdpd, klybr pdhqghohr bd vhulndol bdnh kdbdwdedjxd. Dnlcxqjxpcd mdqdpmlql kdsd nzhqbh pnxwdqr zd ndpshql xolrkxgkxulzd qd pdhoix bd zdwx dpedr dolnlulnxzd ql pnxezd dpedr kdmdzdkl nxxrqd, dphzdkdnlnlvkld nxzd dwdlhqghvkd qfkl nzdxvwddudex qd vl nzd xglnwhwd ndpd dpedybr eddgkl bd zdwx zdphnxzd zdnlgdl.'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(alphabet)):
    decrypted = ''
    message = message6.upper()
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
