# FUCK

import re


def get_words(pos_sent):
    # get words from sentence word/POS
    return ' '.join(w for w in re.findall(r'(\w+)/', pos_sent))

def get_phrase(pos_sent, r):
    # Penn Tagset
    # Determiner can be DT
    # Adjective can be JJ,JJR,JJS
    # Noun can be NN,NNS,NNP,NNPS
    listy = []

    for pair in re.findall(r, pos_sent):

        words = get_words(' '.join(w for w in pair))
        listy.append(words.split(' '))

    # print("LISTY: ", listy)

    return listy








if __name__ == '__main__':
	
	r = r'(\w/DT)?\s?(\w+/JJ)*\s?(\w+/NN)+'

	pos_sent = "the/DT lion/NN adv/VBD the/DT bul/NN to/TO remov/VB every/DT horn/NN of/IN the/DT bul/NN becaus/IN every/DT horn/NN of/IN the/DT bul/NN was/VBD ug/RB"

	matches = re.findall(r, pos_sent)
	print(matches)


	matchy = []
	for tup in matches:
		mini_list = [w.split('/')[0] for w in tup if w != '']
		matchy.append(mini_list)

	matches = [ [w.split('/')[0]] for tup in matches for w in tup ]

	print(matchy)

	matches = re.finditer(r, pos_sent)
	for match in matches:
		mini_list = match.group(0).split(' ')
		mini_list = [w.split('/')[0] for w in mini_list]
		print(mini_list)
		print(match.start())
		print(match.group(0))















