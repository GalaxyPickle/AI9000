##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH SENTENCE
#   recieves Q, type, fetches the sentence from .story or .sch file that holds the correct answer to the Q
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

import sys, nltk, operator, zipfile

# unzip and read story from zip file
def unzip_corpus(input_file, name):
    zip_archive = zipfile.ZipFile(input_file)
    contents = [zip_archive.open(fn, 'r').read().decode('utf-8') 
        for fn in zip_archive.namelist() if fn == name]
    return ''.join(contents)

# get bag of words
# breaks sentences into set of tokenized sentences, removing stopwords
def get_bow(tagged_tokens, stopwords=""):
    if stopwords == "":
        return set([t[0].lower() for t in tagged_tokens])
    else:
        return set([t[0].lower() for t in tagged_tokens if t[0].lower() not in stopwords])

# The standard NLTK pipeline for POS tagging a document
def get_sentences(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    
    return sentences

# qtokens: is a list of pos tagged question tokens with SW removed
# text: list of a list of pos tagged story sentences
# stopwords is a set of stopwords
# matches words to sentences for each text and returns the best answer
def baseline(qbow, text, stopwords):
    # Collect all the candidate answers
    answers = []
    qbow = set([nltk.LancasterStemmer().stem(word) for word in qbow])
    print(qbow)
    for f in text:
        for sent in f:
            # A list of all the word tokens in the sentence
            sbow = get_bow(sent, stopwords)

            # stem all questions and sentences for better results
            sbow = set([nltk.LancasterStemmer().stem(word) for word in sbow])

            # and then add the other
            print(sbow)
            
            # Count the # of overlapping words between the Q and the A
            # & is the set intersection operator
            overlap = len(qbow & sbow)
            print(c.OKGREEN + "overlap: " + c.ENDC + str(overlap))
            
            answers.append((overlap, sent))
        
    # Sort the results by the first element of the tuple (i.e., the count)
    # Sort answers from smallest to largest by default, so reverse it
    answers = sorted(answers, key=operator.itemgetter(0), reverse=True)
    #print(answers)

    # Return the best answer
    best_answer = (answers[0])[1]

    return best_answer

# reads file and finds best sentence
def find_best_sentence(question, fnames):
    print(c.OKGREEN)
    print(fnames)

    # raw story / sch
    dataset = "hw6_dataset"
    text = [unzip_corpus(dataset + ".zip", dataset + "/" + f) for f in fnames]

    # get words for every sentence in sentence
    stopwords = set(nltk.corpus.stopwords.words("english"))
    #stopwords = ""

    # get bow for Q
    print("Q: " + c.ENDC + question + c.OKGREEN)
    question = question[:len(question) - 1]
    qbow = get_bow(get_sentences(question)[0], stopwords)
    print("Q BOW: " + c.ENDC + str(qbow))
    
    # get list of list of POS tag tup sentences in story
    #   [ 
    #   fables-01.story: [sent1: ('the', 'DT'), ...], 
    #       fables-01.sch: [('sack', 'FF'), ...] 
    #   ]
    #   (usually just .story or .sch, not both)
    text = [get_sentences(story) for story in text]
    #print(text)

    answer = baseline(qbow, text, stopwords)
    print(c.OKGREEN + "Answer: " + c.ENDC + " ".join(t[0] for t in answer))

    return " ".join(t[0] for t in answer)

# 1. open story/sch file or both for q
# 2. use super s1ck algorithms to find the best sentence
#   (if story | sch, open both and find best matching sentence)
# 3. return best sentence
def fetch(fname, question, q_type):
    # ready storyname to open
    fname = fname.split('-')
    fname = fname[0] + "-" + fname[1]

    # ready what kind of storyname to open
    if "|" in q_type:
        q_type = q_type.split(' | ')
    else:
        q_type = [q_type]

    fname = [fname + '.' + t for t in q_type]

    # pass in q and filename(s), find best SENTENCE YEAAAAAA
    answer_sentence = find_best_sentence(question, fname)

    return answer_sentence

if __name__ == '__main__':
    fetch()














# EOF #