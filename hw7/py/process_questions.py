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
from nltk.parse import DependencyGraph


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
def unzip_corpus(input_file, name,type_call=False):
    zip_archive = zipfile.ZipFile(input_file)
    if type_call == True:
        return zip_archive.open(name,'r').read().decode('utf-8')

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

def dep_question_process(raw_text,offset=0):
    split_text = []
    for i in range(len(raw_text)):
        split_text += raw_text[i].splitlines() + ['']
    print(split_text)
    # questionID = get_qfactor(split_text,0,offset) #questionID start at line 0 and continue every 4th line


def pickler(filename,data):
    f = open(filename,'wb')
    pickle.dump(data,f)
    f.close()

def get_file_order(filename):
    return unzip_corpus('../hw7_dataset.zip','hw7_dataset/' + filename).splitlines()

def quick_mkdir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def update_inconsistent_tags(old):
    return old.replace("root", "ROOT")

def read_dep(fh):
    dep_lines = []
    qID = None
    for line in fh:
        # print(line)
        line = line.strip()
        # print(line)
        if len(line) == 0:
            return update_inconsistent_tags("\n".join(dep_lines)), qID
        elif re.match(r"^QuestionId:\s+(.*)$", line):
            # print(line)
            qID = line.split(': ',1)[1]
            # You would want to get the question id here and store it with the parse
            continue
        dep_lines.append(line)
        # print(qID)
    if len(dep_lines) > 0:
        return update_inconsistent_tags("\n".join(dep_lines)), qID
    else:
        return None, None

# Read the dependency parses from a file
#inputfile = zipfiles: '../hw7_dataset.zip'
#depfile = 'hw7_dataset/' + question_order[i] + '.questions.dep' 
#question_order[] is a list of strings pulled from process_stories.txt
#returns a tuple (questionID, strings_for_DependencyGraph)
def read_dep_parses(inputfile,depfile):
    fh = unzip_corpus(inputfile,depfile,True).splitlines()

    # list to store the results
    graphs = []
    
    # Read the lines containing the first parse.
    dep, qID = read_dep(fh)

    # print(qID)
    # While there are more lines:
    # 1) create the DependencyGraph
    # 2) add it to our list
    # 3) try again until we're done   
    while dep is not None:
        #creates dependency graph
        # graph = DependencyGraph(dep)
        graph = dep
        graphs.append((qID,graph))
        
        #removes lines that were present in dep
        n = len(dep.splitlines() + [qID]) + 1            
        fh = fh[n:]

        dep, qID = read_dep(fh)

    #returns a tuple (questionID, DependencyGraph)
    return graphs


def start(filename_arg):
    questions = []

    #makes directories
    question_order = get_file_order(filename_arg)
    pickles_path = '../pickles/'
    pickles_normal_path = '/regular/'
    pickles_dep_path = '/dep/'
    pickles_par_path = '/par/'
    quick_mkdir(pickles_path)
    quick_mkdir(pickles_path + pickles_normal_path)
    quick_mkdir(pickles_path + pickles_par_path)
    quick_mkdir(pickles_path + pickles_dep_path)


    input_file = "../hw7_dataset.zip"

    #Questions:
    # question_raw = [unzip_corpus(input_file, 'hw7_dataset/' + question_order[i] + '.questions') for i in range(len(question_order))]
    # f_questionID, f_questions, f_q_type = question_process(question_raw_fables)


    #Questions + Answers:
    answer_raw = [unzip_corpus(input_file, 'hw7_dataset/' + question_order[i] + '.answers') for i in range(len(question_order))]
    questionID, questions, q_type, answer = question_process(answer_raw,1,True)


    #Dep questions:
    dep_graphs_listofEachFile = [read_dep_parses(input_file,'hw7_dataset/' + question_order[i] + '.questions.dep') for i in range(len(question_order))]
    dep_graphs = [j for i in dep_graphs_listofEachFile for j in i]
    # [print(DependencyGraph(y)) for val in dep_graphs for (x,y) in val]
    # print(dep_graphs)

    #Par questions:
    #...
    

    # [print(str(questionID[i]) + ' ' + str(questions[i]) + ' ' + str(answer[i]) + ': ' + str(q_type[i])) for i in range(len(questionID))]


    #basic:
    #[(questionID, question, Type, Answer), ...]
    for i in range(len(questionID)):
        questions += [(questionID[i], questions[i], q_type[i], answer[i]) for i in range(len(questionID))]

    for file in question_order:
        pickler(pickles_path + pickles_normal_path + file + '.pickle',[x for x in questions if file in x[0]])

    #dep:
    #[(questionID, string_stuff), ...] 
    #to fully load into dependency graphs just load the following into variable (depending on which story):
    #example_dependency_graph_list = [DependencyGraph(string_stuff) for (questionID,string_stuff) in dep_graph_file]
    #this will make a list of dependencygraphs. (you cannot store a list of dependency graphs)
    for file in question_order:
        pickler(pickles_path + pickles_dep_path + file + '.dep.pickle',[x for x in dep_graphs if file in x[0]])





if __name__ == '__main__':
    start('process_stories.txt')



















# EOF #