##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# CHUNKY_BOI
#   mah boi gets da correct answer
##############

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

from nltk.stem.wordnet import WordNetLemmatizer

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

def decide(question, answer_sentence):

    # 1. looks at words in question and decides whether to look for words or POS
    # WHO - looks for a POS NP "DT" "JJ" "NN"
    # WHAT - tricky, reads Q last 2 words, then searches for words after them
    # WHERE - looks for POS tag "IN" "DT" "NN" ?
    # WHEN - tricky as well, looks for POS "IN"
    # WHY - looks for the word "because" and words after it
    return

# get the correct answer using a super top secret algo
def mah_boi(question, answer_sentence):

    print()
    print(c.OKGREEN + "Q Sent: " + c.ENDC, question)
    print(c.OKGREEN + "A Sent: " + c.ENDC, answer_sentence)
    print()

    decide(question, answer_sentence)

    return answer_sentence














# EOF #