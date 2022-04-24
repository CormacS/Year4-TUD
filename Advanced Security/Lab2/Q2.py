message2 = 'FEV MRIZRKZFE KF KYV JKREURIU TRVJRI TZGYVI ZJ NYVE KYVRCGYRSVK ZJ "BVPVU" SP LJZEX R NFIU. ZE KYV KIRUZKZFERCMRIZVKP, FEV TFLCU NIZKV KYV RCGYRSVK FE KNF JKIZGJ REU ALJKDRKTY LG KYV JKIZGJ RWKVI JCZUZEX KYV SFKKFD JKIZG KF KYVCVWK FI IZXYK. KF VETFUV, PFL NFLCU WZEU R CVKKVI ZE KYV KFGIFN REU JLSJKZKLKV ZK WFI KYV CVKKVI ZE KYV SFKKFD IFN. WFI RBVPVU MVIJZFE, FEV NFLCU EFK LJV R JKREURIU RCGYRSVK, SLKNFLCU WZIJK NIZKV R NFIU (FDZKKZEX ULGCZTRKVU CVKKVIJ) REUKYVE NIZKV KYV IVDRZEZEX CVKKVIJ FW KYV RCGYRSVK. WFI KYVVORDGCV SVCFN, Z LJVU R BVP FW "ILDBZE.TFD" REU PFL NZCC JVVKYRK KYV GVIZFU ZJ IVDFMVU SVTRLJV ZK ZJ EFK R CVKKVI. PFLNZCC RCJF EFKZTV KYV JVTFEU "D" ZJ EFK ZETCLUVU SVTRLJV KYVIVNRJ RE D RCIVRUP REU PFL TREK YRMV ULGCZTRKVJ.'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(alphabet)):
    decrypted = ''
    message = message2.upper()
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
