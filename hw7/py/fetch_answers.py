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

import pickle, re, collections
from nltk.parse import DependencyGraph
import fetch_sentence, cull_words, process_questions, dep_parse

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

    #load regular questions, in format:
    #[(questionID, question, Type, Answer), ...]
    reg_ques = []
    for file in filenames:
        reg_ques += load_pickle(pickles_path + pickles_normal_path + file + '.pickle')

    reg_ques = collections.OrderedDict.fromkeys(reg_ques)
    print(reg_ques)


    # #to differentiate example:
    # ques_ID = 'fables-01'
    # all_in_fables_01 = [x for x in reg_ques if ques_ID in x[0]]    
    # #or just do it one at a time... :' - (
    # all_in_fables_01 = load_pickle(pickles_path + pickles_normal_path + 'fables-01' + '.pickle')

    #load dep questions, in format:
    #[(questionID, string_garbage), ...]
    dep_ques = []
    for file in filenames:
        dep_ques += load_pickle(pickles_path + pickles_dep_path + file + '.dep.pickle')

    #grow some dependency trees :)
    #to fully load into dependency graphs just load the following into variable (depending on which story):
    dependency_graph_list = [(questionID, DependencyGraph(string_garbage)) for (questionID, string_garbage) in dep_ques]
    #the above will then create a list of tuples.. [(questionID, DependencyGraphs), ...] 
    
    #the rest is just getting story-graphs and then it's plug and play functions...
    #read_dep_parses takes 2 arguments, and 2 optional: read_dep_parses('zipfile_path','file_path',forced_ID=' ',make_graph=false)
    #we set forcedID to equal our filename, and we set make_graph = True so it will just auto make the dep-graphs for us
    story_graphs_listofeach = [dep_parse.read_dep_parses(input_file,'hw7_dataset/' + filenames[i] + '.story.dep',filenames[i],True) for i in range(len(filenames))]
    
    #have to do this because 'read_dep_parses' returns a list.. so we flatten:
    story_graphs = [j for i in story_graphs_listofeach for j in i]
    #GG EZ (you need to do this with .sch.dep later)
    
    #now we just use dep_parse:
    for name in filenames:
        sgraphs = [y for (x,y) in story_graphs if name in x]
        # print(name + ': ' + str(sgraphs))
        for qgraph in dependency_graph_list:
            if name in qgraph[0]:
                print(c.OKGREEN + "Question:" + c.ENDC, dep_parse.pretty_question(qgraph[1]), "?")
                answer = dep_parse.find_answer(qgraph[1], sgraphs)
                if(answer != None):
                    print(c.OKGREEN + "Answer:", answer + c.ENDC)
                else:
                    print(c.FAIL +  "Error: cannot answer this yet" + c.ENDC)
                print()

    ########## WARNING!!! ############
    #the above code will return 'None' for most... this is OK for now.
    #look hard enough, some of the answers will be real! : - )))))
    ##################################




    #load par questions, in format:
    #... not yet




    ################
    ##EXAMPLE CODE##
    ################


    # # 1.
    # #these are dict's of each question
    # #the key will be the QuestionID and the value will be a tuple of question and type
    # #Example --> {'<QuestionID>' : ('<Question>', '<Type>'), ...}
    # all_questions = {**load_pickle(blog_f), **load_pickle(fable_f)}
    
    # #python 2
    # # all_questions = load_pickle(blog_f)
    # # all_questions.update(load_pickle(fable_f))
    # #print(all_questions)

    # # 2.
    # # now we want to read from the proper story/sch for each question and find answer sentence
    # answer_sentences = [fetch_sentence.fetch(key, value[0].lower(), value[1].lower()) 
    #     for key, value in all_questions.items()]

    # # print(answer_sentences)

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