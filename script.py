import prosodic as p

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
# string='from fairest creatures we desire increase \n that thereby beautys rose might never die \n but as the riper should by time decease'
# string='We will, we will rock you \n We will, we will rock you'
# string='but as the riper should by time decease'
# t = p.Text(string)
t = p.Text('C:\\Users\\HP ProBook\\prosodic_data\\corpora\\corppoetry_en\\test1.txt')

t.parse()
# list(t.iparse(meter=None,arbiter='Line',line_lim=None,toprint=False))

text=[]
for parse in t.bestParses():
	print(parse)
	text.append(str(parse))

syllablegram=fsyllablegram(text)

print(syllablegram)