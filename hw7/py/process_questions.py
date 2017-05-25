##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# PROCESS QUESTIONS
#	recieves a file, reads questions, and returns a dic of Q and Q type
##############

import zipfile, os
import re, nltk
import pickle

#global variables for executable extraction.



###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive.
# It first creates a ZipFile object.
# Using a list comprehension it creates a list where each element contains
# the raw text of the fable file.
# We iterate over each named file in the archive:
#     for fn in zip_archive.namelist()
# For each file that is named 'name' we open the file in read only
# mode:
#     zip_archive.open(fn, 'rU')
# Finally, we read the raw contents of the file:
#     zip_archive.open(fn, 'rU').read()
def unzip_corpus(input_file, name):
    zip_archive = zipfile.ZipFile(input_file)
    contents = [zip_archive.open(fn, 'r').read().decode('utf-8') for fn in zip_archive.namelist() if fn == name]
    return ''.join(contents)

#takes start, then steps through for every 4th line and splits it off at the ':' delimiter
def get_qfactor(split_text, start,offset=0,step=5):
    return [split_text[i].split(': ',1)[1] for i in range(start,len(split_text),step + offset)]

#gets questionIDs, questions, and types from specified question files
def question_process(raw_text, offset=0,answer=False):
    split_text = []
    for i in range(len(raw_text)):
        split_text += raw_text[i].splitlines() + ['']
    #print(split_text)
    questionID = get_qfactor(split_text,0,offset) #questionID start at line 0 and continue every 4th line
    questions = get_qfactor(split_text,1,offset)
    q_type = get_qfactor(split_text,3,offset)

    # print("questionID: {0}".format(questionID))
    # print("questions: {0}".format(questions))
    # print("type: {0}".format(q_type))
    if answer == True:
        questionID = get_qfactor(split_text,0,offset) #questionID start at line 0 and continue every 4th line
        questions = get_qfactor(split_text,1,offset)
        q_type = get_qfactor(split_text,4,offset)
        answer = get_qfactor(split_text,2,offset)
        return questionID, questions, q_type, answer
    return questionID, questions, q_type

def pickler(filename,data):
    f = open(filename,'wb')
    pickle.dump(data,f)
    f.close()

def get_file_order(filename):
    return unzip_corpus('../hw7_dataset.zip','hw7_dataset/' + filename).splitlines()

def quick_mkdir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def start(filename_arg):
    questions = []


    question_order = get_file_order(filename_arg)
    pickles_path = '../pickles/'
    pickles_normal_path = '/regular/'
    pickles_dep_path = '/dep/'
    pickles_par_path = '/par/'
    quick_mkdir(pickles_path)
    quick_mkdir(pickles_path + pickles_normal_path)
    quick_mkdir(pickles_path + pickles_par_path)
    quick_mkdir(pickles_path + pickles_dep_path)


    # blogs_qfilename = ["hw6_dataset/blogs-01.questions"]
    # fables_qfilename = ["hw6_dataset/fables-01.questions","hw6_dataset/fables-02.questions"]
    input_file = "../hw7_dataset.zip"

    #Questions:
    # question_raw = [unzip_corpus(input_file, 'hw7_dataset/' + question_order[i] + '.questions') for i in range(len(question_order))]

    # f_questionID, f_questions, f_q_type = question_process(question_raw_fables)


    #Questions + Answers:
    answer_raw = [unzip_corpus(input_file, 'hw7_dataset/' + question_order[i] + '.answers') for i in range(len(question_order))]

    questionID, questions, q_type, answer = question_process(answer_raw,1,True)


    #Dep questions:

    #Par questions:

    

    # [print(str(questionID[i]) + ' ' + str(questions[i]) + ' ' + str(answer[i]) + ': ' + str(q_type[i])) for i in range(len(questionID))]



    #[(questionID, question, Type, Answer), ...]
    for i in range(len(questionID)):
        questions += [(questionID[i], questions[i], q_type[i], answer[i]) for i in range(len(questionID))]

    for file in question_order:
        pickler(pickles_path + pickles_normal_path + file + '.pickle',[x for x in questions if file in x[0]])




    #these are dict's of each question
    #the key will be the QuestionID and the value will be a tuple of question and type
    #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}

    # pickler('questions_blogs.pickle',questions_blogs)

    # pickler('questions_fables.pickle',questions_fables)

if __name__ == '__main__':
    start('process_stories.txt')



















# EOF #