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
# 4. returns a list of tups [(Q1, A1), (Q2, A2), ...]
def start():
    blog_f = 'questions_blogs.pickle'
    fable_f = 'questions_fables.pickle'

    #these are dict's of each question
    #the key will be the QuestionID and the value will be a tuple of question and type
    #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}
    questions_blogs = load_pickle(blog_f)
    questions_fables = load_pickle(fable_f)

    # compile all questions into a mega dic
    all_questions = {**questions_blogs, **questions_fables}
    # print(all_questions)

    # now we want to read from the story 

    all_answers = []

    # we return a list of tups [(Q1, A1), (Q2, A2), ...]
    return 


if __name__ == '__main__':
    start()















# EOF #