##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH SENTENCE
#	receives dic of Q, fetches the sentence from .story or .sch file that holds the correct answer to the Q
##############

import pickle, re
import fetch_sentence, cull_words

#loads pickles
def load_pickle(filename):
    f = open(filename,'rb')
    question_dict = pickle.load(f)
    f.close()
    return question_dict

# 1. reads the pickles
# 2. finds correct answer sentence
# 3. culls words from correct answer sentence
# 4. returns a list of tups [(Q1, A1), (Q2, A2), ...]
def start():
    blog_f = 'questions_blogs.pickle'
    fable_f = 'questions_fables.pickle'

    # 1.
    #these are dict's of each question
    #the key will be the QuestionID and the value will be a tuple of question and type
    #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}
    all_questions = {**load_pickle(blog_f), **load_pickle(fable_f)}
    
    #python 2
    # all_questions = load_pickle(blog_f)
    # all_questions.update(load_pickle(fable_f))
    #print(all_questions)

    # 2.
    # now we want to read from the proper story/sch for each question and find answer sentence
    answer_sentences = [fetch_sentence.fetch(key, value[0].lower(), value[1].lower()) 
        for key, value in all_questions.items()]

    # print(answer_sentences)

    # compile list of question/answer sentence
    QandA = []
    i = 0
    for key, val in all_questions.items():
        QandA.append((val[0], answer_sentences[i]))
        i += 1
    #print(QandA)

    # 3.
    # finally, we get the proper answer string for each sentence/question
    answers = [cull_words.cull(question, sentence) for (question, sentence) in QandA]

    QandA = []
    i = 0
    for key, val in all_questions.items():
        answer = ' '.join(w for w in answers[i])
        QandA.append(("QuestionID: " + key, "Answer: " + answer))
        i += 1
    #print(QandA)

    # 4.
    # we return a list of tups [(Q1, A1), (Q2, A2), ...]
    return QandA


if __name__ == '__main__':
    start()















# EOF #