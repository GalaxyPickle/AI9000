##############
# Alex Lang
# Conor Rogers
#
# HW 7
#
# DEP PARSE
#	Function holder for all-purpose dependency parsing
#	Modified for zipfiles from the stub-code
##############
import zipfile, os
import re, sys, nltk, operator
import pickle
from nltk.parse import DependencyGraph

def unzip_corpus(input_file, name,type_call=False):
    zip_archive = zipfile.ZipFile(input_file)
    if type_call == True:
        return zip_archive.open(name,'r').read().decode('utf-8')

    contents = [zip_archive.open(fn, 'r').read().decode('utf-8') for fn in zip_archive.namelist() if fn == name]

    return ''.join(contents)

def update_inconsistent_tags(old):
    return old.replace("root", "ROOT")

def read_dep(fh,filename):
    dep_lines = []
    qID = filename
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
def read_dep_parses(inputfile,depfile,filename=' ',make_graph=False):
    fh = unzip_corpus(inputfile,depfile,True).splitlines()

    # list to store the results
    graphs = []
    
    # Read the lines containing the first parse.
    dep, qID = read_dep(fh,filename)

    # print(qID)
    # While there are more lines:
    # 1) create the DependencyGraph
    # 2) add it to our list
    # 3) try again until we're done   
    while dep is not None:
        #creates dependency graph
        if(make_graph):
        	graph = DependencyGraph(dep)
        else:
        	graph = dep
        	
        graphs.append((qID,graph))
        
        #removes lines that were present in dep
        n = len(dep.splitlines() + [qID]) + 1            
        fh = fh[n:]

        dep, qID = read_dep(fh,filename)

    #returns a tuple (questionID, DependencyGraph)
    return graphs

# Return the word of the root node
def find_root_word(graph):
    for node in graph.nodes.values():
        if node['rel'] == 'ROOT':
            return node["word"]
    return None

# find the node with similar word
def find_node(word, graph):
    for node in graph.nodes.values():
        if 'word' in node and node["word"] == word:
            return node
    return None

def get_dependents(node, graph):
    results = []
    for item in node["deps"]:
        address = node["deps"][item][0]
        dep = graph.nodes[address]
        results.append(dep)
        results += get_dependents(dep, graph)
    return results

def pretty_question(qgraph):
    question = []
    for q in qgraph.nodes.values():
        if 'word' in q and q['word'] is not None:
            question.append(q['word'])
    return " ".join(question)

def find_answer(qgraph, sgraphs):
    qword = find_root_word(qgraph)
    # look for answer in the sgraphs, return the first match
    for sgraph in sgraphs:
        snode = find_node(qword, sgraph)
        if snode is None or 'address' not in snode:
            continue
        for node in sgraph.nodes.values():
            #print("node in nodelist:", node)
            #print("Our relation is:", node['rel'], ", and word is:", node['word'])
            #print("Our node is:", node)
            if node is None or 'head' not in node:
                continue
            if node['head'] == snode["address"]:
                if node['rel'] == "nmod":
                    deps = get_dependents(node, sgraph)
                    deps.append(node)
                    deps = sorted(deps, key=operator.itemgetter("address"))
                    return " ".join(dep["word"] for dep in deps)