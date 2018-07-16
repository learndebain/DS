# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211

def countAndSay(number):
    if (number == 1):
        return '1'
    if (number == 2):
        return '11'
    count = 1
    string = countAndSay(number - 1)
    newstring = ''
    i = 0
    while True:
        while (i < len(string) - 1):
            i += 1
            if (string[i] == string[i-1]):    
                count = count + 1
            else:
                i -= 1
                break
        newstring += str(count) + str(string[i])
        count = 1
        if (i >= len(string) - 1):
            break
        else:
            i += 1
    return newstring


    


number = int(input("Enter the number: "))
print(countAndSay(number))
