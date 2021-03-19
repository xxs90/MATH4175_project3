cipherText = "XCIUIHTVOQVRLHJEYJXAVICEJFWXRVRUAAEPVPNEQLFZGFQEBXOIUXGIVJXVGLBRBXYIDB" \
             "FZVKCSGHNITYJBXTSWXZHWZAYSEPINIIZWBRMITIFMQJRKLKASRIMIJPICEMIGGEIINWUT" \
             "PZWVIFFEDRJXJXEHTISVNGOWRRVLIMZZGWLHZWZKFXHDRRASRXCEKKAOINYJIJLWJPVGGG" \
             "XMSCSNXVGTIKLXJXYIAKHVXREKTVZWLPLEERIEJGKGZQVRLBWNSDILBQZWLRSUPZXFVWV" \
             "SQIIXZXRKIFMSAICIUMVJRZGUHQHYEMUTXDSEWXKSHXYILXGCRFPGZCKVFZAWIMIMIFB" \
             "RMIJTGGWZXFEUHYMXFVVXVJVUYDREPXYSJBDZHNEJKEIXZWKNIYFPEXXHZVRPBNHBIWSJX" \
             "BVQGPWFEICTSEFYIMTELBSIWJIJOMXIJRGPIIGICHMGZVKEAGGJQDYFBGVXZSFLFTHVJSN" \
             "POAZXZMLZOVCFXGZWJEJRXJHVGJRTOXYIUHQHYEMUTXDSEWKHPZPPMFMLZLRRVLSAXYIWG" \
             "HPWVVLAMNEGTDBINFFXZPLZRKLWWEOEZWAGQJXZSFHZZVVPWVXMSEMUGIOAFVCLSMEKVWL" \
             "XJRRRWEIXXISFBGYIMMUXMAXYIUHQHYEMUTXDSEWHKSQMUIJBWNIIZWWADXYEOTVMEEXKX" \
             "IFMEKLASNITSEFYIMTELBSIWKLWIVJZZHWKGVRESLIVJZZHWMLZHRXSUIXELWWBXCEJHWL" \
             "MBRVHLAIOITLFHPJKPWMVLOLRXAMGVRESLUIVGTIKLIYFPEFRXCMIHHTVOCNIVHRJXYENX" \
             "EICJMDOIMFLPDXXNEEHLAIYMJGMLWDSEWOBXCMEXZXISITYLBZZFIEFVLVVVWLBPGSEKGB" \
             "RBAYMDXXCIIIZTWISKCWMFZIEEVXGDWZSFPLZXYIJMSNIVODXKDWCELBSIAVQMLXRSIOOB" \
             "XCGFRYKINWZRVNWOVPEUTHZQZGKIVDZRGQZVJYGWSGHJXYIJLXJGIEXMEIEGTJHEXLKLSM" \
             "EYHIIKLINECPGYXCIDYDMMKPVGGFTZXZRYVSIGVVFLXCEKLSOIWIVRLAIASTYKHJNSDYUA" \
             "HZFRXWUYOAVGSGEGPRKJXIOLRXOXADPCRWXHJRXSAGKCSEIKMEIHZRXHVHIUTMUPDGUITT" \
             "XZESSMMLJASIKMXJTISLXGOPZFWKXTEEHKXGPVZXQBRWSKLGNVGENWSGHJYIXWVLISCSYR"

length = len(cipherText)

#print(length)

m = [4, 5, 6, 7, 8]

for num in m:
    if num == 4:
        print("m = 4")
        y1 = ""
        y2 = ""
        y3 = ""
        y4 = ""
        for i in range(length):
            if i % 4 == 0:
                y1 += cipherText[i]
            elif i % 4 == 1:
                y2 += cipherText[i]
            elif i % 4 == 2:
                y3 += cipherText[i]
            else:
                y4 += cipherText[i]
        print("y1 = ", y1)
        print("y2 = ", y2)
        print("y3 = ", y3)
        print("y4 = ", y4)

    elif num == 5:
        print("\nm = 5")
        y1 = ""
        y2 = ""
        y3 = ""
        y4 = ""
        y5 = ""
        for i in range(length):
            if i % 5 == 0:
                y1 += cipherText[i]
            elif i % 5 == 1:
                y2 += cipherText[i]
            elif i % 5 == 2:
                y3 += cipherText[i]
            elif i % 5 == 3:
                y4 += cipherText[i]
            else:
                y5 += cipherText[i]
        print("y1 = ", y1)
        print("y2 = ", y2)
        print("y3 = ", y3)
        print("y4 = ", y4)
        print("y5 = ", y5)

    elif num == 6:
        print("\nm = 6")
        y1 = ""
        y2 = ""
        y3 = ""
        y4 = ""
        y5 = ""
        y6 = ""
        for i in range(length):
            if i % 6 == 0:
                y1 += cipherText[i]
            elif i % 6 == 1:
                y2 += cipherText[i]
            elif i % 6 == 2:
                y3 += cipherText[i]
            elif i % 6 == 3:
                y4 += cipherText[i]
            elif i % 6 == 4:
                y5 += cipherText[i]
            else:
                y6 += cipherText[i]
        print("y1 = ", y1)
        print("y2 = ", y2)
        print("y3 = ", y3)
        print("y4 = ", y4)
        print("y5 = ", y5)
        print("y6 = ", y6)

    elif num == 7:
        print("\nm = 7")
        y1 = ""
        y2 = ""
        y3 = ""
        y4 = ""
        y5 = ""
        y6 = ""
        y7 = ""
        for i in range(length):
            if i % 7 == 0:
                y1 += cipherText[i]
            elif i % 7 == 1:
                y2 += cipherText[i]
            elif i % 7 == 2:
                y3 += cipherText[i]
            elif i % 7 == 3:
                y4 += cipherText[i]
            elif i % 7 == 4:
                y5 += cipherText[i]
            elif i % 7 == 5:
                y6 += cipherText[i]
            else:
                y7 += cipherText[i]
        print("y1 = ", y1)
        print("y2 = ", y2)
        print("y3 = ", y3)
        print("y4 = ", y4)
        print("y5 = ", y5)
        print("y6 = ", y6)
        print("y7 = ", y6)

    elif num == 8:
        print("\nm = 8")
        y1 = ""
        y2 = ""
        y3 = ""
        y4 = ""
        y5 = ""
        y6 = ""
        y7 = ""
        y8 = ""
        for i in range(length):
            if i % 8 == 0:
                y1 += cipherText[i]
            elif i % 8 == 1:
                y2 += cipherText[i]
            elif i % 8 == 2:
                y3 += cipherText[i]
            elif i % 8 == 3:
                y4 += cipherText[i]
            elif i % 8 == 4:
                y5 += cipherText[i]
            elif i % 8 == 5:
                y6 += cipherText[i]
            elif i % 8 == 6:
                y7 += cipherText[i]
            else:
                y8 += cipherText[i]
        print("y1 = ", y1)
        print("y2 = ", y2)
        print("y3 = ", y3)
        print("y4 = ", y4)
        print("y5 = ", y5)
        print("y6 = ", y6)
        print("y7 = ", y7)
        print("y8 = ", y8)
