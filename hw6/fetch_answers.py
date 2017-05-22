##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH SENTENCE
#	recieves dic of Q, fetches the sentence from .story or .sch file that holds the correct answer to the Q
##############

import pickle
import fetch_sentences, cull_words

#loads pickles
def load_pickle(filename):
    f = open(filename,'rb')
    question_dict = pickle.load(f)
    f.close()
    return question_dict

# 1. reads the pickles
# 2. finds correct answer sentence
# 3. culls words from correct answer sentence
# 4. returns tuple of lists ([questions], [answers])
def start():
    blog_f = 'questions_blogs.pickle'
    fable_f = 'questions_fables.pickle'

    #these are dict's of each question
    #the key will be the QuestionID and the value will be a tuple of question and type
    #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}
    questions_blogs = load_pickle(blog_f)
    questions_fables = load_pickle(fable_f)

    print(questions_blogs)
    print(questions_fables)

    # now we want to fetch the BEST sentence that contains the answer



    # we return a tup of ([questions], [answers])



if __name__ == '__main__':
    start()















# EOF #