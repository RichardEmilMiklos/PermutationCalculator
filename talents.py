char_name = 'Kirez'
talentrowlength = 3
talents = [1,1,1,1,1,1,1]
text = ''

def add_list_to_text(lst):
    global text
    talentstring = ''

    for i in range(0,len(lst)):
        talentstring += str(lst[i])
        
    text += 'copy=' + char_name + '-' + talentstring + '\n' + 'talents=' + talentstring + '\n\n'

def calc(counter):
    if(talents[counter] != 0):
        if(counter == 0):
            for _ in range(0,talentrowlength):
                add_list_to_text(talents) # Print talents
                talents[0] += 1
            talents[0] = 1
        else:
            for _ in range(0,talentrowlength):
                calc(counter-1)
                talents[counter] += 1
            talents[counter] = 1
    else:
        if(counter != 0):
            calc(counter-1)
        else:
            add_list_to_text(talents) # Print talents
        

calc(len(talents)-1)

text = text[:-2]

f = open('talents.txt','w')
f.write(text)
f.close()

print(str((len(text.split('\n'))+1)//3) + ' ('+str(talentrowlength)+'^'+str(len(talents))+') copies stored in talents.txt.')