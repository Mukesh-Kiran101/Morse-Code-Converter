# morse_to_letter_number = {morse : letter/number }
#letter_number_to_morse = {letter/number : morse }

letter_number_to_morse = {" ":" /","a":" .-","b":" -..","c":" -.-.","d":" -..","e":" .","f":" ..-.","g":" --.","h":" ....","i":" ..","j":" .---","k":" -.-","l":" .-..","m":" --","n":" -.","o":" ---","p":" .--","q":" --.-","r":" .-.","s":" ...","t":" -","u":" ..-","v":" ...-","w":" .--","x":" -..-","y":" -.--","z":" --.",0: "-----", 1: ".----", 2: "..---", 3: "...--", 4: "....-", 5: ".....", 6: "-....", 7: "--...", 8: "---..", 9: "----."}
morse_to_letter_number = {" ": "", "/": " ", ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z" , ".----": 1, "..---": 2, "...--": 3, "....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9, "-----": 0}

#Converting letter/number into morse code

def conv(xin):
    res = ""
    for i in xin:
        res += str(letter_number_to_morse[i])
    return res

#Converting morse into Letter/number

def conv_m(riss):
    rizz = ""
    for i in riss.split(" "):
        rizz += str(morse_to_letter_number[i])
    return rizz

#Output

x = True
while x :
    cho = input("\n1 : sentence to morse code convertion \n2 : Morse code to sentence\n\n    >> Enter your choice 1 or 2 :")
    if cho == "1":
        print("your Morse code is:", conv((input("Enter the sentence:")).lower()))
    if cho == "2":
        print("Your sentence is:", (conv_m(input("Enter the Morse code:"))))
    #choice to continue or not to the user
    x = input("Do u want to continue\n1:Yes and 2:No\n >> Enter:")
    if x == "1":x = True
    elif x == "2":x = False
