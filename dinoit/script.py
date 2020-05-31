########################
######## IMPORT ########
########################

import prosodic as p
import random
from tkinter import Tk,Frame,Text,Button
import webbrowser

#########################
##### syllablegram ######
#########################

def fsyllablegram(text):
	scheme=[]
	for line in text:
		cnt=line.count('|')
		line_scheme=[]
		pattern=[]
		flag=True
		for i in range(len(line)):
			if line[i]=='|':
				flag=True
			elif flag:
				if line[i].isupper():
					pattern.append(1)
				else:
					pattern.append(0)
				flag=False
			if len(pattern)==4:
				break

		if pattern.count(1)==2:
			if pattern[0]==1:
				pattern=[1,0]
				rhythm=21
			else:
				pattern=[0,1]
				rhythm=22
		else:
			if pattern[0]==1:
				pattern=[1,0,0]
				rhythm=31
			elif pattern[1]==1:
				pattern=[0,1,0]
				rhythm=32
			else:
				pattern=[0,0,1]
				rhythm=33
		line_scheme=[rhythm]
		line_scheme=line_scheme+(pattern*(cnt+1))[0:cnt+1]

		scheme.append(line_scheme)
	return scheme

p.lang='en'
p.config['print_to_screen']=0

########################
######## DINOIT ########
########################

yamb1 = ['t-rex', 'minmi', 'troodon']
yamb2 = ['baryonyx', 'bambiraptor', 'kotasaurus']
horey1 = ['yinlong']
horey2 = ['caudipteryx', 'rinchenia', 'triceratops', 'diplodocus']
dactyl = ['tanius']
dactyl2 = [['tirex', 'diplodocus'], ['minmi', 'triceratops'], ['troodon', 'caudipteryx']]
amph1 = ['kaatedocus', 'raptorex', 'zalmoxes', 'aardonyx', 'coelurus']
anapest1 = ['rapator']
anapest2 = [['bambiraptor', 'yiulong'], ['baryonyx', 'yinlong']]

def dinoline(line):
    size = line[0] // 10
    stress = line[0] % 10
    parts = (len(line) - 1) // size
    remainder = len(line) - 1 - parts * size
    ans = []
    k = parts
    while k > 0:
        if (size == 2):
            if (stress == 1):
                if k >= 3:
                    ans.append(yamb2[random.randint(0,2)])
                    k -=2
                else:
                    ans.append(yamb1[random.randint(0,2)])
                    k -= 1
            else:
                if k >=3:
                    ans.append(horey2[random.randint(0, 3)])
                    k -= 2
                else:
                    ans.append('yinlong')
                    k -= 1
        else:
            if (stress== 1):
                if k >= 3:
                    t = random.randint(0,2)
                    ans.append(dactyl2[t][0])
                    ans.append(dactyl2[t][1])
                    k -= 2
                else:
                    ans.append('tanius')
                    k -= 1
            elif (stress == 2):
                ans.append(amph1[random.randint(0,4)])
                k -= 1
            else:
                if k >= 3 and k % 3 == 0:
                    t = random.randint(0,1)
                    ans.append(anapest2[t][0])
                    ans.append(anapest2[t][1])
                    k -= 2
                else:
                    ans.append('rapator')
                    k -= 1
    if remainder != 0:
        if size == 2:
            if stress == 1:
                ans.append('khaan')
            else:
                ans.pop()
                ans.append('raptorex')
        else:
            if remainder == 2:
                if stress == 1:
                    ans.pop()
                    ans.append('thyreophora')
                elif stress == 2:
                    ans.append('yinlong')
                else:
                    ans.pop()
                    ans.append('tsagantegia')
            else:
                if stress == 1:
                    ans.append('khaan')
                elif stress == 2:
                    ans.pop()
                    ans.append('diplodocus')
                else:
                    ans.pop()
                    ans.append('baryonyx')
    return ans


def dinoit(syllablegram):
    ans = []
    for i in range(len(syllablegram)):
        ans.append([])
        for word in dinoline(syllablegram[i]):
            ans[i].append(word)
    return ans

# text = [[31, 1, 0, 0, 1, 0, 0, 1, 0 , 0, 1, 0], [31, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]]
# res = dinoit(text)
# print(res)


#########################
######## Tkinter ########
#########################


root = Tk()

panel_frame = Frame(root, height = 50, width=50, bg = 'gray')
text_frame= Frame(root,height=20,width=50)
panel_frame.pack(side='bottom',fill='both')
text_frame.pack(side='top')

input_text = Text(text_frame,width=25, height=20, font='Arial 14', wrap='word')
output_text = Text(text_frame,width=25, height=20, font='Arial 14', wrap='word')
output_text.insert(1.0,'')

input_text.pack(side = 'left')
output_text.pack(side = 'right')

go=Button(panel_frame, text = 'Dino it!')
learn=Button(panel_frame, text = 'Learn with me!')

def go_ans(event):
	output_text.delete(1.0, 'end')
	text=input_text.get(1.0, 'end-1c')
	t = p.Text(text,meter='default_english')
	t.parse()

	txt=[]
	for parse in t.bestParses():
		# print(parse)
		txt.append(str(parse))

	syllablegram=fsyllablegram(txt)
	# print(syllablegram)

	to_print=dinoit(syllablegram)
	# print(to_print)
	for line in to_print:
		for word in line:
			output_text.insert('end',word+' ')
		output_text.insert('end','\n')

def learn_ans(event):
	if output_text.tag_ranges('sel'):
		dino=output_text.get('sel.first', 'sel.last')
		# print(dino)
		if(dino=='raptorex'):
			link='https://en.wikipedia.org/wiki/Raptorex'
		elif(dino=='kaatedocus'):
			link='https://en.wikipedia.org/wiki/Kaatedocus'
		elif(dino=='thyreophora'):
			link='https://en.wikipedia.org/wiki/Thyreophora'
		elif(dino=='t-rex'):
			link='https://www.nhm.ac.uk/discover/dino-directory/tyrannosaurus.html'
		else:
			link='https://www.nhm.ac.uk/discover/dino-directory/{}.html'.format(dino)
		# print(link)
	else:
		arr=['https://www.nhm.ac.uk/discover/dino-directory/khaan.html',
 'https://www.nhm.ac.uk/discover/dino-directory/minmi.html',
 'https://www.nhm.ac.uk/discover/dino-directory/tyrannosaurus.html',
 'https://www.nhm.ac.uk/discover/dino-directory/troodon.html',
 'https://www.nhm.ac.uk/discover/dino-directory/baryonyx.html',
 'https://www.nhm.ac.uk/discover/dino-directory/bambiraptor.html',
 'https://www.nhm.ac.uk/discover/dino-directory/kotasaurus.html',
 'https://www.nhm.ac.uk/discover/dino-directory/yinlong.html',
 'https://www.nhm.ac.uk/discover/dino-directory/caudipteryx.html',
 'http://nhm.ac.uk/discover/dino-directory/rinchenia.htmla',
 'https://www.nhm.ac.uk/discover/dino-directory/triceratops.html',
 'https://www.nhm.ac.uk/discover/dino-directory/diplodocus.html',
 'https://www.nhm.ac.uk/discover/dino-directory/tanius.html',
 'https://en.wikipedia.org/wiki/Thyreophora',
 'https://en.wikipedia.org/wiki/Kaatedocus',
 'https://en.wikipedia.org/wiki/Raptorex',
 'https://www.nhm.ac.uk/discover/dino-directory/zalmoxes.html',
 'https://www.nhm.ac.uk/discover/dino-directory/aardonyx.html',
 'https://www.nhm.ac.uk/discover/dino-directory/coelurus.html',
 'https://en.wikipedia.org/wiki/Rapator',
 'https://www.nhm.ac.uk/discover/dino-directory/tsagantegia.html']
		link=arr[random.randint(0,len(arr)-1)]
	webbrowser.open(link, new=2)

go.bind("<Button-1>", go_ans)
learn.bind("<Button-1>", learn_ans)

go.place(x=100,y=15,width=60,height=20)
learn.place(x=375,y=15,width=100,height=20)

root.mainloop()