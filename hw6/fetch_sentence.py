import pickle

##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH SENTENCE
#	recieves dic of Q, fetches the sentence from .story or .sch file that holds the correct answer to the Q
##############

#loads pickles
def load_pickle(filename):
    f = open(filename,'rb')
    question_dict = pickle.load(f)
    f.close()
    return question_dict

if __name__ == '__main__':
    blog_f = 'questions_blogs.pickle'
    fable_f = 'questions_fables.pickle'

    #these are dict's of each question
    #the key will be the QuestionID and the value will be a tuple of question and type
    #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}
    questions_blogs = load_pickle(blog_f)
    questions_fables = load_pickle(fable_f)

    # print(questions_blogs)
    # print(questions_fables)
