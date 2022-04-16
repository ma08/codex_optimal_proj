

def main():
    #dictionary of the new alphabet
    new_alphabet = {'a':'@','b':'8','c':'(','d':'|)','e':'3','f':'#','g':'6','h':'[-]','i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]','n':'[]\[]','o':'0','p':'|D','q':'(,)','r':'|Z','s':'$','t':'\'][\'','u':'|_|','v':'\/','w':'\/\/','x':'}{','y':'`/','z':'2','A':'@','B':'8','C':'(','D':'|)','E':'3','F':'#','G':'6','H':'[-]','I':'|','J':'_|','K':'|<','L':'1','M':'[]\/[]','N':'[]\[]','O':'0','P':'|D','Q':'(,)','R':'|Z','S':'$','T':'\'][\'','U':'|_|','V':'\/','W':'\/\/','X':'}{','Y':'`/','Z':'2'}
    #get input
    text = input()
    #create output string
    output = ''
    #iterate through the characters of the input string
    for char in text:
        #if the character is in the new alphabet, add the new character to the output string
        if char in new_alphabet:
            output += new_alphabet[char]
        #if the character is not in the new alphabet, add the character to the output string
        else:
            output += char
    #print the output string
    print(output)

main()
