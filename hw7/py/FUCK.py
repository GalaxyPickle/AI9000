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
	
	r = r'(\w+/NN)+'

	pos_sent = "a/DT crow/NNP was/VBD sit/VBG on/IN a/DT branch/NN of/IN a/DT tre/NN with/IN a/DT piec/NN of/IN chees/NN in/IN her/PRP$ beak/NN when/WRB a/DT fox/NNP observ/VBD her/PRP$ and/CC set/VB his/PRP$ wit/NNS to/TO work/VB to/TO discov/VB som/DT way/NN of/IN get/VBG the/DT chees/NN"

	matches = re.findall(r, pos_sent)
	matches = [w.split('/')[0] for w in matches]

	print(matches)