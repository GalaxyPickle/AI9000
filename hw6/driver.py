##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# DRIVER
#	is the driver, calls all supporting files
##############

import process_questions, fetch_answers, write_answers

def load_pickle(filename):
    f = open(filename,'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

if __name__ == '__main__':

	# make some pickles of dic type for questions and type
    process_questions.start()
    # call helper files to find and return Q & the best A 
    #	tuple of lists ([questions], [answers]) 
    responses = fetch_answers.start()
    # write the questions and answers to a file in the proper format
    write_answers.start(questions, answers)







# EOF #