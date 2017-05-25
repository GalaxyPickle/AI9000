# import word_category_counter
##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# CULL WORDS
#	recieves a correct answer sentence, eliminates extraneous words (w/ respect to Answer)
##############

import re, nltk, argparse
from nltk.stem.wordnet import WordNetLemmatizer

def get_words_tags(text):
    words = []
    tags = []
    # tokenization for each sentence
    for sent in nltk.sent_tokenize(text):           
        for word, pos in nltk.pos_tag(nltk.word_tokenize(sent)):
            checked_word = normalize(word)
            if checked_word is None:
                continue
            words.append(checked_word)
            tags.append(pos)
    return words, tags

def get_bi_tags(bigram):
    words = []
    tags = []
    for word, pos in nltk.pos_tag(bigram):
        words.append(checked_word)
        tags.append(pos)
    return tags

#keeps the keep_words
def normalize(token):
    keep_words = ['the','a','to','of','on']
    stopwords = [x for x in nltk.corpus.stopwords.words('english') if x not in keep_words]
    if token.lower() not in stopwords and re.search(r'\w', token):
        return token.lower()
    return None

def get_bigram(tokens):
    # uni = tokens
    bi = nltk.bigrams(tokens)
    # tri = nltk.trigrams(tokens)
    return bi

#returns lemma of word added 
def lemmatizer(tokens):
    lem_tokens = []
    # this little bit is because wordnet lemmas don't play nicely with things verb infinitives....... [very rough fix
    second_form_same_vinfinitive = [('felt','feel'),('fell','fall'),('stood','stand')]

    vinfinitive_check = [a for (a,b) in second_form_same_vinfinitive]
    for token in tokens:
        for (a,b) in second_form_same_vinfinitive:
            if a == token:
                lem_tokens += [b]
        if token not in vinfinitive_check:
            lem_tokens += [WordNetLemmatizer().lemmatize(token,'v')]

    return lem_tokens

#roughly determines what tag would fit the question...
def determine_type(question):
    q = question.lower()
    if 'what' in q:
        if 'did' in q:
            if 'have' in q:
                return ['DT','NN','IN']
            return ['VBN','VBD','NN']

        if 'if' in q:
            return ['PRP','DT','NN','NNS','NNP','NNPS','JJ']
        if (len(question.split())) == 1:
            return ['sentence']
        return ['NN','NNP','DT','JJ']
    if 'who' in q:
        if 'they' in q:
            return ['NNS', 'NNPS']
        # if 'was' in q:
        #     return ['NNP','DT']
        return ['NN','NNP','DT']
    if 'how' in q:
        return ['PRP','DT','NN','NNS','NNP','NNPS','JJ']
    if 'when' in q:
        return ['CD','NN','JJ']
    if 'where' in q:
        return ['NN','NNP','DT', 'IN']
    if'why' in q:
        return ['NN','VBD']
    return ['ambiguous']

#culls all words without the correct tag (determined by determine_type())
def get_correct_words(qtype,sentence_words,sentence_tags):
    ans = []
    for x in range(len(sentence_words)):
        if sentence_tags[x] in qtype:
            if sentence_words[x] not in ans:
                ans += [sentence_words[x]]

    if ans == []:
        ans = ['']

    return ans

#
def cull(question, sentence):
    qtype = determine_type(question)

    # print(question + '-> ' + str(qtype))
    sentence_words, sentence_tags = get_words_tags(sentence)
    question_words, question_tags = get_words_tags(question)
    # print(str(sentence_words) + ' ' + str(sentence_tags))
    # bi_sentence_words = get_bigram(sentence_words)
    # print(get_bi_tags(bi_sentence_words))
    # print(str(sentence_words) + ' ' + str(sentence_tags))
    # print(str(question_words) + ' ' + str(question_tags))
    # print(sentence_words)
    # print(sentence_tags)
    # lemma_sentence = lemmatizer(sentence_words)
    # lemma_question = lemmatizer(question_words)
    if (qtype[0] != 'ambiguous') or (qtype[0] != 'sentence'):
        rough_ans = get_correct_words(qtype,sentence_words,sentence_tags)
    else:
        rough_ans = sentence_words
    
    # print(rough_ans)

    
    return rough_ans

if __name__ == '__main__':
    cull('What did the crow feel?',' The crow felt that the fox had flattered her and cawed loudly in order for she to show him that she was able to sing.')
    cull('Who is the man?', 'The crow met The Man.')
    cull('when did I meet you?', 'The two met at 12:40, there was a giant football in the field and we danced')
    cull('Where was the crow sitting?','The crow was sitting on a branch of a tree')
    cull('Who was persuaded by this flattery?','The Bull was foolish enough to be persuaded by this flattery to have his horns cut off; and, having now lost his only means of defense, fell an easy prey to the Lion.')
    cull('Who was foolish?', 'There once was a fat bull.')
    cull('When did the G20 summit start?','A summit meeting named G20 summit started on eventful today.')
    cull("Why didn't the lion attack the bull?","The lion didn't attack the bull because the lion feared sharp every horn of the bull.")
    cull("What did the crow have in her beak?","A Crow was sitting on a branch of a tree with a piece of cheese in her beak when a Fox observed her and set his wits to work to discover some way of getting the cheese.")
    cull("What did the fox do to the cheese?","The fox snatched the cheese, said that the crow was able to sing and the fox said that the crow needed wits.")