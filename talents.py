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

for a in range(0,talentrowlength):
    for b in range(0,talentrowlength):
        for c in range(0,talentrowlength):
            for d in range(0,talentrowlength):
                for e in range(0,talentrowlength):
                    for f in range(0,talentrowlength):
                        for g in range(0,talentrowlength):
                            add_list_to_text(talents) # Print talents
                            talents[0] += 1
                        talents[0] = 1
                        talents[1] += 1
                    talents[1] = 1
                    talents[2] += 1
                talents[2] = 1
                talents[3] += 1
            talents[3] = 1
            talents[4] += 1
        talents[4] = 1
        talents[5] += 1
    talents[5] = 1
    talents[6] += 1
talents[6] = 1

text = text[:-2]

f = open('talents.txt','w')
f.write(text)
f.close()

print(str((len(text.split('\n'))+1)//3) + ' ('+str(talentrowlength)+'^'+str(len(talents))+') copies stored in talents.txt.')