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

def get_index_coincidence(input_str):
    arr = [0] * 26
    for n in range(len(input_str)):
        if input_str[n] == 'A':
            arr[0] += 1
        elif input_str[n] == 'B':
            arr[1] += 1
        elif input_str[n] == 'C':
            arr[2] += 1
        elif input_str[n] == 'D':
            arr[3] += 1
        elif input_str[n] == 'E':
            arr[4] += 1
        elif input_str[n] == 'F':
            arr[5] += 1
        elif input_str[n] == 'G':
            arr[6] += 1
        elif input_str[n] == 'H':
            arr[7] += 1
        elif input_str[n] == 'I':
            arr[8] += 1
        elif input_str[n] == 'J':
            arr[9] += 1
        elif input_str[n] == 'K':
            arr[10] += 1
        elif input_str[n] == 'L':
            arr[11] += 1
        elif input_str[n] == 'M':
            arr[12] += 1
        elif input_str[n] == 'N':
            arr[13] += 1
        elif input_str[n] == 'O':
            arr[14] += 1
        elif input_str[n] == 'P':
            arr[15] += 1
        elif input_str[n] == 'Q':
            arr[16] += 1
        elif input_str[n] == 'R':
            arr[17] += 1
        elif input_str[n] == 'S':
            arr[18] += 1
        elif input_str[n] == 'T':
            arr[19] += 1
        elif input_str[n] == 'U':
            arr[20] += 1
        elif input_str[n] == 'V':
            arr[21] += 1
        elif input_str[n] == 'W':
            arr[22] += 1
        elif input_str[n] == 'X':
            arr[23] += 1
        elif input_str[n] == 'Y':
            arr[24] += 1
        elif input_str[n] == 'Z':
            arr[25] += 1
    #print(arr)

    b = 0
    for j in range(len(arr)):
        if arr[j] != 1:
            a = arr[j] * (arr[j] - 1)
            b += a
    return b


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

        # print("y1 = ", y1)
        ic1 = get_index_coincidence(y1) / (len(y1) * (len(y1) + 1))
        print("ic1 = ", ic1)
        # print("\ny2 = ", y2)
        ic2 = get_index_coincidence(y2) / (len(y2) * (len(y2) + 1))
        print("ic2 = ", ic2)
        # print("\ny3 = ", y3)
        ic3 = get_index_coincidence(y3) / (len(y3) * (len(y3) + 1))
        print("ic3 = ", ic3)
        # print("\ny4 = ", y4)
        ic4 = get_index_coincidence(y4) / (len(y4) * (len(y4) + 1))
        print("ic4 = ", ic4)

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

        #print("y1 = ", y1)
        ic1 = get_index_coincidence(y1) / (len(y1) * (len(y1) + 1))
        print("ic1 = ", ic1)
        #print("\ny2 = ", y2)
        ic2 = get_index_coincidence(y2) / (len(y2) * (len(y2) + 1))
        print("ic2 = ", ic2)
        #print("\ny3 = ", y3)
        ic3 = get_index_coincidence(y3) / (len(y3) * (len(y3) + 1))
        print("ic3 = ", ic3)
        #print("\ny4 = ", y4)
        ic4 = get_index_coincidence(y4) / (len(y4) * (len(y4) + 1))
        print("ic4 = ", ic4)
        #print("\ny5 = ", y5)
        ic5 = get_index_coincidence(y5) / (len(y5) * (len(y5) + 1))
        print("ic5 = ", ic5)


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

        #print("y1 = ", y1)
        ic1 = get_index_coincidence(y1) / (len(y1) * (len(y1) + 1))
        print("ic1 = ", ic1)
        #print("\ny2 = ", y2)
        ic2 = get_index_coincidence(y2) / (len(y2) * (len(y2) + 1))
        print("ic2 = ", ic2)
        #print("\ny3 = ", y3)
        ic3 = get_index_coincidence(y3) / (len(y3) * (len(y3) + 1))
        print("ic3 = ", ic3)
        #print("\ny4 = ", y4)
        ic4 = get_index_coincidence(y4) / (len(y4) * (len(y4) + 1))
        print("ic4 = ", ic4)
        #print("\ny5 = ", y5)
        ic5 = get_index_coincidence(y5) / (len(y5) * (len(y5) + 1))
        print("ic5 = ", ic5)
        #print("\ny6 = ", y6)
        ic6 = get_index_coincidence(y6) / (len(y6) * (len(y6) + 1))
        print("ic6 = ", ic6)

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

        #print("y1 = ", y1)
        ic1 = get_index_coincidence(y1) / (len(y1) * (len(y1) + 1))
        print("ic1 = ", ic1)
        #print("\ny2 = ", y2)
        ic2 = get_index_coincidence(y2) / (len(y2) * (len(y2) + 1))
        print("ic2 = ", ic2)
        #print("\ny3 = ", y3)
        ic3 = get_index_coincidence(y3) / (len(y3) * (len(y3) + 1))
        print("ic3 = ", ic3)
        #print("\ny4 = ", y4)
        ic4 = get_index_coincidence(y4) / (len(y4) * (len(y4) + 1))
        print("ic4 = ", ic4)
        #print("\ny5 = ", y5)
        ic5 = get_index_coincidence(y5) / (len(y5) * (len(y5) + 1))
        print("ic5 = ", ic5)
        #print("\ny6 = ", y6)
        ic6 = get_index_coincidence(y6) / (len(y6) * (len(y6) + 1))
        print("ic6 = ", ic6)
        #print("\ny7 = ", y7)
        ic7 = get_index_coincidence(y7) / (len(y7) * (len(y7) + 1))
        print("ic7 = ", ic7)

        for i in range(len(y1)):
            if i != len(y1) - 1:
                print(y1[i], " ", y2[i], " ", y3[i] , " ", y4[i], " ",
                      y5[i], " ", y6[i], " ", y7[i], "\n")
            else:
                print(y1[i], " ", y2[i], " ", y3[i], " ", y4[i], "\n")

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

        #print("y1 = ", y1)
        ic1 = get_index_coincidence(y1) / (len(y1) * (len(y1) + 1))
        print("ic1 = ", ic1)
        #print("\ny2 = ", y2)
        ic2 = get_index_coincidence(y2) / (len(y2) * (len(y2) + 1))
        print("ic2 = ", ic2)
        #print("\ny3 = ", y3)
        ic3 = get_index_coincidence(y3) / (len(y3) * (len(y3) + 1))
        print("ic3 = ", ic3)
        #print("\ny4 = ", y4)
        ic4 = get_index_coincidence(y4) / (len(y4) * (len(y4) + 1))
        print("ic4 = ", ic4)
        #print("\ny5 = ", y5)
        ic5 = get_index_coincidence(y5) / (len(y5) * (len(y5) + 1))
        print("ic5 = ", ic5)
        #print("\ny6 = ", y6)
        ic6 = get_index_coincidence(y6) / (len(y6) * (len(y6) + 1))
        print("ic6 = ", ic6)
        #print("\ny7 = ", y7)
        ic7 = get_index_coincidence(y7) / (len(y7) * (len(y7) + 1))
        print("ic7 = ", ic7)
        #print("\ny8 = ", y8)
        ic8 = get_index_coincidence(y8) / (len(y8) * (len(y8) + 1))
        print("ic8 = ", ic8)

