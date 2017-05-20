import zipfile, os
import re, nltk
##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# PROCESS QUESTIONS
#	recieves a file, reads questions, and returns a dic of Q and Q type
##############

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
    contents = [zip_archive.open(fn, 'rU').read().decode('utf-8') for fn in zip_archive.namelist() if fn == name]
    return ''.join(contents)

#takes start, then steps through for every 4th line and splits it off at the ':' delimiter
def get_qfactor(split_text, start):
    return [split_text[i].split(': ',1)[1] for i in range(start,len(split_text),5)]

def question_process(raw_text):
    for i in range(len(raw_text)):
        split_text = raw_text[i].splitlines() 
    questionID = get_qfactor(split_text,0) #questionID start at line 0 and continue every 4th line
    questions = get_qfactor(split_text,1)
    q_type = get_qfactor(split_text,3)

    # print("questionID: {0}".format(questionID))
    # print("questions: {0}".format(questions))
    # print("type: {0}".format(q_type))

    return questionID, questions, q_type





if __name__ == '__main__':

    questions_blogs = {}
    questions_fables = {}

    blogs_qfilename = ["hw6_dataset/blogs-01.questions"]
    fables_qfilename = ["hw6_dataset/fables-01.questions","hw6_dataset/fables-02.questions"]
    input_file = "hw6_dataset.zip"

    question_raw_blogs = [unzip_corpus(input_file,blogs_qfilename[i]) for i in range(len(blogs_qfilename))]
    question_raw_fables = [unzip_corpus(input_file,fables_qfilename[i]) for i in range(len(fables_qfilename))]

    b_questionID, b_questions, b_q_type = question_process(question_raw_blogs)

    f_questionID, f_questions, f_q_type = question_process(question_raw_fables)



    for i in range(len(b_questionID)):
        questions_blogs.update({b_questionID[i] : (b_questions[i], b_q_type[i])})

    for i in range(len(f_questionID)):
        questions_fables.update({f_questionID[i] : (f_questions[i], f_q_type[i])})

    

