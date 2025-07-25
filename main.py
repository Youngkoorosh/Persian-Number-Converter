addad = {
    '1': "yek", '2': "do", '3': "se",
    '4': "chahaar", '5': "panj", '6': "shesh",
    '7': "haft", '8': "hasht", '9': "noh",
    '10': "dah", '11': "yaazdah", '12': "davaazdah",
    '13': "sizdah", '14': "chahaardah", '15': "paanzdah",
    '16': "shaanzdah", '17': "hifdah", '18': "hijdah",
    '19': "noozdah", '20': "bist", '30': "si",
    '40': "chehel", '50': "panjaah", '60': "shast",
    '70': "haftaad", '80': "hashtaad", '90': "navad",
    '100': "sad", '200': "devist", '300': "sisad",
    '400': "chahaarsad", '500': "paansad", '600': "sheshsad",
    '700': "haftsad", '800': "hashtsad", '900': "nohsad"
}


for i in range(int(input())):
    num=input()
    if len(num) == 3:
        if num in addad:
            print (addad[num])
        elif num[1:] in addad and num[0] + "00" in addad:
            print (addad[num[0] + "00"] + "o " + addad[num[1:]])
        elif num[0] + "00" in addad and num[1] + "0" in addad and num[2] in addad:
            print (addad[num[0] + "00"] + "o " + addad[num[1] + "0"] + "o " + addad[num[2]])
        elif num[0] + "00" in addad and num[2] in addad:
            print (addad[num[0] + "00"] + "o "  + addad[num[2]])
    elif len(num) == 2:
        if num in addad:
            print (addad[num])
        elif num[0] + "0" in addad and num[1] in addad:
            print (addad[num[0] + "0"] + "o " + addad[num[1]])
    elif len(num) == 1 and num in addad:
        print (addad[num])
