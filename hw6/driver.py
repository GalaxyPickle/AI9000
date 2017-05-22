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
    #	list of tups [(Q1, A1), (Q2, A2), ...]
    response = fetch_answers.start()

    # testing
    response = [
    	("Q1: xxx", "A1: sacked"), 
    	("Q2: yyy", "A2: flipped"), 
    	("Q3: etc", "A3: etc")
    	]

    # writes answers to "train_my_answers.txt"
    write_answers.start(response)