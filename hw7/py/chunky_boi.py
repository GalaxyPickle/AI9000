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

# returns matches for regex exp passed into a sentence tagged <...> <word>/<POS> <...>
def get_phrase(pos_sent, r):

    matches = re.findall(r, pos_sent)

    ret = []
    for tup in matches:

        mini_list = [ w.split('/')[0] for w in tup if w != '']

        ret.append(mini_list)

    print(c.OKGREEN + "SEARCH WORDS: " + c.ENDC, ret)



    return ret

# returns a list of matches for the pattern in the myList
# returns a list of tuples: (word string, average index in the sentence list)
def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and len(mylist) >= i + len(pattern) and mylist[i:i+len(pattern)] == pattern:
            # append a tuple containing the string match and the average i index
            matches.append((
                [ w for w in mylist[i:i + len(pattern)] ], 
                math.floor(len(pattern) / 2 + i) 
                ))

    return matches

def decide(q, s):

    # ----------------------------------------------------------------------------------------

    print("Q: ", q)

    stopwords = set(nltk.corpus.stopwords.words("english"))

    # 1. remove all stopwords from q and s, and stem all words remaining in q and s
    # ----------------------------------------------------------------

    q_proc = [ (nltk.LancasterStemmer().stem(word), tag) for word, tag in q 
        if word not in stopwords ]
    q_proc = " ".join(word + "/" + tag for word, tag in q_proc)

    # print("QPROC: ", q_proc)

    s_proc = [ (nltk.LancasterStemmer().stem(word), tag) for word, tag in s ]
    s_proc = " ".join(word + "/" + tag for word, tag in s_proc)

    s_proc_nostem = " ".join(word + "/" + tag for word, tag in s)

    # print("SPROC: ", s_proc)

            # ----------------------------------------------------------------
    # 2. set demo regex
    r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+'

    # r = r'(\S+/TO)?\s?(\S+/VB)*\s?(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+\s?(\S+/NN)?\s?(\S+/NN)?\s?(\S+/NN)?\s?(\S+/NN)?\s?(\S+/IN)?\s?(\S+/NN)*'


    # how:
    # r = r'(\S+/ninininininin)*\s?(\S+/RB)+\s?'

    # why:
    # r = r'(\S+/IN)+\s?(\S+/DT)?\s?(\S+/IN)*\s?(\S+/NN)+\s?(\S+/NN)+\s?(\S+/NN)+\s?(\S+/NN)+'
        #everything after because...


    # where:
    # r = r'(\S+/IN)*\s?(\S+/DT)?\s?(\S+/IN)*\s?(\S+/NN)+'

    # what:
    # r = r'(\S+/TO)?\s?(\S+/VB)*\s?(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+'
    # r = r'(\S+/TO)?\s?(\S+/VB)*\w?\s?(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+\s?(\S+/IN)?\s?(\S+/DT)?\s?(\S+/NN)*\s?(\S+/VB)?\w?\s?(\S+/JJ)*'

    # when:
    # r = r'(\S+/WRB)?\s?(\S+/PRP)*\s?(\S+/VBD)*'


    # who:
    # r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+'

    # 1. looks at words in question and decides whether to look for words or POS
    # WHO - looks for a POS NP "DT" "JJ" "NN"
    search_words = [word for word, tag in q]
    if 'who' in search_words:
        print('who')
        r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+\s?(\S+/NN)?\s?(\S+/NN)?'
        #default.

    # WHAT - tricky, reads Q last 2 words, then searches for words after them
    elif 'what' in search_words:
        if 'did' in search_words:
        #('that', 'IN'), ('the', 'DT'), ('lion', 'NN'), ('was', 'VBD'), ('friendly', 'RB')
        # r = r'(\S+/IN)?\s?(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN)+(\S+/VB\w?)?\s?(\S+/RB)?'
            print('what did')
            r = r'(\S+/TO)?\s?(\S+/DT)?\s?(\S+/VB\w?)?\s?(\S+/JJ)*\s?(\S+/NN)+\s?(\S+/NN)?\s?(\S+/NN)?\s?(\S+/IN)?\s?(\S+/NN)*\s?(\S+/DT)?\s?(\S+/TO)?\s?(\S+/VB\w?)?\s?(\S+/NN)*\s?(\S+/VB\w?)?\s?(\S+/JJ)*\s?(\S+/NN)?\s?(\S+/RB\w?)?'
        elif 'happened' in search_words:
            #('police', 'NNP'), ('cars', 'NNS'), ('were', 'VBD'), ('burned', 'VBN')
            print('what happened')
            r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN\w?)+\s?(\S+/NN\w?)?\s?(\S+/NN\w?)?\s?(\S+/VB\w?)?\s?(\S+/VB\w?)?\s?(\S+/VB\w?)?'
        elif 'was' in search_words:
            print('what was')
            #('police', 'NNP'), ('cars', 'NNS'), ('were', 'VBD'), ('burned', 'VBN')
            #('in', 'IN'), ('a', 'DT'), ('flat', 'JJ'), ('and', 'CC'), ('large', 'JJ'), ('dish', 'NN')]
            r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/CC)?\s?(\S+/JJ)*\s?(\S+/NN\w?)+\s?(\S+/NN\w?)?\s?(\S+/NN\w?)?\s?(\S+/VB\w?)?\s?(\S+/VB\w?)?\s?(\S+/VB\w?)?'

    # WHERE - looks for POS tag "IN" "DT" "NN" ?
    elif 'where' in search_words:
        print('where')
        # ('in', 'IN'), ('a', 'DT'), ('flat', 'JJ'), ('and', 'CC'), ('large', 'JJ'), ('dish', 'NN')
        r = r'(\S+/IN)*\s?(\S+/DT)?\s?(\S+/IN)?\s?(\S+/JJ)*\s?(\S+/CC)?\s?(\S+/JJ)*\s?(\S+/NN\w?)+'

    # WHEN - tricky as well, looks for POS "IN"
    elif 'when' in search_words:
        print('when')
        #[('a', 'DT'), ('few', 'JJ'), ('years', 'NNS'), ('ago', 'RB')
        r = r'(\S+/DT)?\s?(\S+/JJ)*\s?(\S+/NN\w?)+\s?(\S+/RB)?'

    # WHY - looks for the word "because" or just the Q and words after it
    elif 'why' in search_words:
        print('why')
        #('in', 'IN'), ('order', 'NN'), ('for', 'IN'), ('the', 'DT'), ('birds', 'NNS'), ('to', 'TO'), ('wait', 'VB')
        # r = r'(\S+/IN)*\s?(\S+/NN\w?)?\s?(\S+/IN)*\s?(\S+/DT)*\s?(\S+/NN\w?)*\s?(\S+/TO)?\s?(\S+/VB\w?)?'
        r = r'(?<=becaus).*'
        #looks for because

    elif 'how' in search_words:
        print('how')
        r = r'(\S+/ninininininin)*\s?(\S+/RB)+\s?'

    # 3. search answer sentence for phrases matching reg exp and assign index num value
    # ----------------------------------------------------------------

    # s_matches = []
    # for match in get_phrase(s_proc, r):
    #     # print("sent match: ", match)
    #     sub_match = subfinder([word for word, tag in s], match)
    #     if len(sub_match) != 0:
    #         s_matches.append(sub_match)

    # print(c.OKGREEN + "S_MATCHES: " + c.ENDC, s_matches)

    # # 4. search answer sentence for all words in processed question and assign index num value
    # # ----------------------------------------------------------------

    # q_r = re.findall(r'(\w+)/+', q_proc)
    # q_r = [[w] for w in q_r]
    # # print(c.OKGREEN + "QR" + c.ENDC, q_r)

    # q_matches = []
    # for match in q_r:
    #     # print("ques match: ", match)
    #     sub_match = subfinder([word for word, tag in s], match)
    #     if len(sub_match) != 0:
    #         q_matches.append(sub_match)

    # print(c.OKGREEN + "Q_MATCHES: " + c.ENDC, q_matches)

    # # 5. compare the indices for the found s_matches and q_matches, then return the best one!
    # # ----------------------------------------------------------------

    # # 99 is index of answer tup in s_matches
    # # 66 is num value of answer_tup in s_matches
    # high = (99, 66)
    # if q_matches != []:
    #     for listy in q_matches:
    #         for tup in listy:
    #             q_index = tup[1]

    #             # compare indices and return the highest one
    #             if s_matches != []:
    #                 for i in range(len(s_matches)):
    #                     for stup in s_matches[i]:
    #                         if stup != []:
    #                             print("STUP: ", stup)
    #                             s_index = stup[1]
    #                             comp = math.fabs(s_index - q_index)
    #                             if comp <= high[1]:
    #                                 high = (i, comp)


    #             # print(q_index)
    # else:
    #     high = (0, 0)

    # # print("S: ", s)

    answer = ""
    # if s_matches != []:
    #     answer = s_matches[high[0]]
    print(c.OKGREEN + "ANSWER: " + c.ENDC, answer)

    return answer

# get the correct answer using a super top secret algo
def mah_boi(question, answer_sentence):

    question = [(word.lower(), tag) for word, tag in question if re.match(r'\w+', word)]
    answer_sentence = [(word.lower(), tag) for word, tag in answer_sentence if re.match(r'\w+', word)]

    # print()
    # print(c.OKGREEN + "Q Sent: " + c.ENDC, question)
    # print(c.OKGREEN + "A Sent: " + c.ENDC, answer_sentence)
    # print()

    return decide(question, answer_sentence)














# EOF #