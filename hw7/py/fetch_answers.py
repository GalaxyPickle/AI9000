##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH ANSWER
#	receives dic of Q, fetches the sentence from .story or .sch file that holds the correct answer to the Q
##############

# for coloring the terminal output 8)
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import pickle, re
import cull_words, process_questions, chunky

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
def start(filename_arg):
    # blog_f = 'questions_blogs.pickle'
    # fable_f = 'questions_fables.pickle'

    ################
    ##EXAMPLE CODE##
    ################

    #pickle directories
    pickles_path = '../pickles/'
    pickles_normal_path = 'regular/'
    pickles_dep_path = 'dep/'
    pickles_par_path = 'par/'

    #zipfile
    input_file = "../hw7_dataset.zip"

    #filenames such as fables-01, fables-02, ect.
    filenames = process_questions.get_file_order(filename_arg)

    # 1.
    #load regular questions, in format:
    #[(questionID, question, Type, Answer), ...]
    reg_ques = []
    for file in filenames:
        reg_ques += load_pickle(pickles_path + pickles_normal_path + file + '.pickle')

    print(reg_ques)

    # 2.
    # now we want to read from the proper story/sch for each question and find answer sentence
    answer_sentences = [chunky.chunk(a_id, q, q_type, a)
        for q_id, q, q_type, a in reg_ques]

    # print(answer_sentences)

    # # compile list of question/answer sentence
    # QandA = []
    # i = 0
    # for key, val in all_questions.items():
    #     QandA.append((val[0], answer_sentences[i]))
    #     i += 1
    # #print(QandA)

    # # 3.
    # # finally, we get the proper answer string for each sentence/question
    # answers = [cull_words.cull(question, sentence) for (question, sentence) in QandA]

    # QandA = []
    # i = 0
    # for key, val in all_questions.items():
    #     answer = ' '.join(w for w in answers[i])
    #     QandA.append(("QuestionID: " + key, "Answer: " + answer))
    #     i += 1
    # #print(QandA)

    # # 4.
    # # we return a list of tups [(Q1, A1), (Q2, A2), ...]
    # return QandA

#     -----------THIS IS THE FORMAT WE WANT OUR ANSWER LIST TO RETURN IN------------
#     # this is a list of lists
#     # each element in this list is a list corresponding the each pickle file (fables-01, fables-02, etc.)
#     # element of the inner lists is a tuple of type:
#     # (question ID, Question, Type, Answer)
#     # the whole thing looks like this:
#     # all_questions = 
#     # [
#     #     [ (fables-01-1, "What is Bob?", "Story", "Dumb"), (...), ...  ],
#     #     [ (fables-02-1, ..., ..., ...), (...), ... ],
#     #     ...
#     # ]

if __name__ == '__main__':
    start('process_stories.txt')















# EOF #