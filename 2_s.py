mojis = input()
mojis_hairetu = [0 for _ in range(26)]
num = ""
nums = [1]
shouryaku_hantei = True

for moji in mojis:
    k = 1
    if moji == "0" or moji == "1" or moji == "2" or moji == "3" or moji == "4" or moji == "5" or moji == "6" or moji == "7" or moji == "8" or moji == "9":
        num += moji
    else:
        if num != "":
            if shouryaku_hantei:
                k = (int(num))
            else:
                nums.append(int(num))
            num = ""
        if "(" == moji:
            shouryaku_hantei = False
        elif ")" == moji:
            del nums[1]
            if len(num) == 1:
                shouryaku_hantei = True
        else:
            for i in nums:
                k = i*k
            print(moji)
            print(nums)
            print(k)
            if moji =="a":
                mojis_hairetu[0]+=k
            elif moji =="b":
                mojis_hairetu[1]+=k
            elif moji =="c":
                mojis_hairetu[2]+=k
            elif moji =="d":
                mojis_hairetu[3]+=k
            elif moji =="e":
                mojis_hairetu[4]+=k
            elif moji =="f":
                mojis_hairetu[5]+=k
            elif moji =="g":
                mojis_hairetu[6]+=k
            elif moji =="h":
                mojis_hairetu[7]+=k
            elif moji =="i":
                mojis_hairetu[8]+=k
            elif moji =="j":
                mojis_hairetu[9]+=k
            elif moji =="k":
                mojis_hairetu[10]+=k
            elif moji =="l":
                mojis_hairetu[11]+=k
            elif moji =="m":
                mojis_hairetu[12]+=k
            elif moji =="n":
                mojis_hairetu[13]+=k
            elif moji =="o":
                mojis_hairetu[14]+=k
            elif moji =="p":
                mojis_hairetu[15]+=k
            elif moji =="q":
                mojis_hairetu[16]+=k
            elif moji =="r":
                mojis_hairetu[17]+=k
            elif moji =="s":
                mojis_hairetu[18]+=k
            elif moji =="t":
                mojis_hairetu[19]+=k
            elif moji =="u":
                mojis_hairetu[20]+=k
            elif moji =="v":
                mojis_hairetu[21]+=k
            elif moji =="w":
                mojis_hairetu[22]+=k
            elif moji =="x":
                mojis_hairetu[23]+=k
            elif moji =="y":
                mojis_hairetu[24]+=k
            elif moji =="z":
                mojis_hairetu[25]+=k
            else:
                print(moji)
print("a " + str(mojis_hairetu[0]))
print("b " + str(mojis_hairetu[1]))
print("c " + str(mojis_hairetu[2]))
print("d " + str(mojis_hairetu[3]))
print("e " + str(mojis_hairetu[4]))
print("f " + str(mojis_hairetu[5]))
print("g " + str(mojis_hairetu[6]))
print("h " + str(mojis_hairetu[7]))
print("i " + str(mojis_hairetu[8]))
print("j " + str(mojis_hairetu[9]))
print("k " + str(mojis_hairetu[10]))
print("l " + str(mojis_hairetu[11]))
print("m " + str(mojis_hairetu[12]))
print("n " + str(mojis_hairetu[13]))
print("o " + str(mojis_hairetu[14]))
print("p " + str(mojis_hairetu[15]))
print("q " + str(mojis_hairetu[16]))
print("r " + str(mojis_hairetu[17]))
print("s " + str(mojis_hairetu[18]))
print("t " + str(mojis_hairetu[19]))
print("u " + str(mojis_hairetu[20]))
print("v " + str(mojis_hairetu[21]))
print("w " + str(mojis_hairetu[22]))
print("x " + str(mojis_hairetu[23]))
print("y " + str(mojis_hairetu[24]))
print("z " + str(mojis_hairetu[25]))