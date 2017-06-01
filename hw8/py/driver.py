# ██████╗ ██████╗ ██╗██╗   ██╗███████╗██████╗ 
# ██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔══██╗
# ██║  ██║██████╔╝██║██║   ██║█████╗  ██████╔╝
# ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
# ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝

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
import sys

if __name__ == '__main__':

    # get command line argument for the file to process story Q's in order
    if len(sys.argv) - 1 is not 1:
        print("Usage: python3 driver.py <story_order_filename>")
    else:
	   # make some pickles of dic type for questions and type
        process_questions.start(sys.argv[1])

        # call helper files to find and return Q & the best A 
        #	list of tups [(Q1 {fables-01-1}, guess-A1, correct-A1), (Q2 {fables-01-2}, guess-A2, correct-A2), ...]
        response = fetch_answers.start(sys.argv[1])

        # testing
        # response = [
        # 	("Q1: xxx", "A1: sacked"), 
        # 	("Q2: yyy", "A2: flipped"), 
        # 	("Q3: etc", "A3: etc")
        # 	]

        # writes answers to "train_my_answers.txt"
        write_answers.start(response)