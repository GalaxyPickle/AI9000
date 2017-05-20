# import os
##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# DRIVER
#	is the driver, calls all supporting files
##############

def load_pickle(filename):
    f = open(filename,'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

if __name__ == '__main__':


    exec(open('process_questions.py').read())


