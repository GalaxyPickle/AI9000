##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# CHUNKY_BOI
#   mah boi gets da correct answer
##############

from nltk.stem.wordnet import WordNetLemmatizer
import argparse, re, nltk, math

# colorssszzzzzz
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#returns lemma of word added 
def lemmatizer(tokens):
    lem_tokens = []
    # this little bit is because wordnet lemmas don't play nicely with things verb infinitives....... [very rough fix
    second_form_same_vinfinitive = [('felt','feel'),('fell','fall'),('stood','stand'),('flattered','flatter'),('flattery','flatter')]

    vinfinitive_check = [a for (a,b) in second_form_same_vinfinitive]
    for token in tokens:
        for (a,b) in second_form_same_vinfinitive:
            if a == token:
                lem_tokens += [b]
        if token not in vinfinitive_check:
            lem_tokens += [WordNetLemmatizer().lemmatize(token,'v')]

    return lem_tokens

# def whoSearch(q, s):

# def whatSearch(q, s):

# def whereSearch(q, s):

# def whenSearch(q, s):

# def whySearch(q, s):

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
        print("words: ", words)
        listy.append(words.split(' '))

    return listy

# returns a list of matches for the pattern in the myList
# returns a list of tuples: (word string, average index in the sentence list)
def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            # append a tuple containing the string match and the average i index
            matches.append((
                [ w for w in mylist[i:i + len(pattern)] ], 
                math.floor(len(pattern) / 2 + i) 
                ))

    return matches

def decide(q, s):

    q_proc = " ".join(word + "/" + tag for word, tag in q)
    s_proc = " ".join(word + "/" + tag for word, tag in s)

    # print("\s_proc: " + c.OKGREEN + s_proc + c.ENDC)
    # print("\s_proc words: " + c.OKGREEN + str(get_words(s_proc)) + c.ENDC)
    # print("\ns_proc noun phrase: " + c.OKGREEN + str(get_noun_phrase(s_proc)) + c.ENDC)

    r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+'

    s_matches = []
    for match in get_phrase(s_proc, r):
        sub_match = subfinder([word for word, tag in s], match)
        s_matches.append(sub_match)

    print(s_matches)

    q_matches = []
    for match in get_phrase(q_proc, r):
        return

    # 1. looks at words in question and decides whether to look for words or POS
    # WHO - looks for a POS NP "DT" "JJ" "NN"
    if 'who' in [word for word, tag in q]:
        r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+'
    # WHAT - tricky, reads Q last 2 words, then searches for words after them
    if 'what' in q:
        return
    # WHERE - looks for POS tag "IN" "DT" "NN" ?
    if 'where' in q:
        return
    # WHEN - tricky as well, looks for POS "IN"
    if 'when' in q:
        return
    # WHY - looks for the word "because" or just the Q and words after it
    if 'why' in q:
        return
    return 

# get the correct answer using a super top secret algo
def mah_boi(question, answer_sentence):

    question = [(word.lower(), tag) for word, tag in question if re.match(r'\w+', word)]
    answer_sentence = [(word.lower(), tag) for word, tag in answer_sentence if re.match(r'\w+', word)]

    print()
    print(c.OKGREEN + "Q Sent: " + c.ENDC, question)
    print(c.OKGREEN + "A Sent: " + c.ENDC, answer_sentence)
    print()

    return decide(question, answer_sentence)














# EOF #