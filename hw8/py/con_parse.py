#!/usr/bin/env python
'''
Created on May 14, 2014
@author: reid

Modified on May 21, 2015
# '''

#             ())                           _|_
# '''''''''''(||)0                       _|_| |
#                                        | || |  /
#                                      \ |_||_| /
#                   (^)_(^) *ribbit*    \ | /| /
#        ~    ______(-----)_.__        ~ \|/ |/
#  ~       _..   _  /_____\  _ .._
#         :     / \/ |   | \/ \   `.
#     ~    `___ |_\__|___|__/_|     `.     ~
#              /|\  /|\ /|\  /|\      ;
#       .____.o o oo o o o oo o o     ;
#    ~  :                           _.        ~
#       :__                       __.
# ~       :_____         _____...
#               :.......:             ~
#           ~

import argparse, re, nltk, math, sys
from nltk.tree import Tree
import chunky
import process_questions

# Read the constituency parse from the line and construct the Tree
def read_con_parses(parfile):
    fh = open(parfile, 'r')
    lines = fh.readlines()
    fh.close()
    return [Tree.fromstring(line) for line in lines]

# See if our pattern matches the current root of the tree
def matches(pattern, root):
    # Base cases to exit our recursion
    # If both nodes are null we've matched everything so far
    if root is None and pattern is None: 
        return root
        
    # We've matched everything in the pattern we're supposed to (we can ignore the extra
    # nodes in the main tree for now)
    elif pattern is None:                
        return root
        
    # We still have something in our pattern, but there's nothing to match in the tree
    elif root is None:                   
        return None

    # A node in a tree can either be a string (if it is a leaf) or node
    plabel = pattern if isinstance(pattern, str) else pattern.label()
    rlabel = root if isinstance(root, str) else root.label()

    # If our pattern label is the * then match no matter what
    if plabel == "*":
        return root
    # Otherwise they labels need to match
    elif plabel == rlabel:
        # If there is a match we need to check that all the children match
        # Minor bug (what happens if the pattern has more children than the tree)
        for pchild, rchild in zip(pattern, root):
            match = matches(pchild, rchild) 
            if match is None:
                return None 
        return root
    
    return None
    
def pattern_matcher(pattern, tree):
    for subtree in tree.subtrees():
        node = matches(pattern, subtree)
        if node is not None:
            return node
    return None

def subtree_master(pattern,tree):
    subtree = pattern_matcher(pattern,tree)
    
    if subtree is None:
        # pattern = nltk.ParentedTree.fromstring("(NP (*) )")
        # subtree = pattern_matcher(pattern,tree)
        # print(subtree)
        # print(" ".join(subtree.leaves()))
        return 'nopes'


    # print(subtree)
    # print(" ".join(subtree.leaves()))
    return subtree


def q_determine(question,tree):
    search_words = question.lower().split()
    # print(search_words)
    if 'who' in search_words:
        print('who')


        if 'did' in search_words:
            pattern = nltk.ParentedTree.fromstring("(VP  )")
        
            # # Match our pattern to the tree  
            subtree = subtree_master(pattern,tree)       
            
            # create a new pattern to match a smaller subset of subtree
            pattern = nltk.ParentedTree.fromstring("(NP)")

            # Find and print the answer
            subtree2 = subtree_master(pattern,subtree)

            return subtree2

        # elif 'was' in search_words:
        #     pattern = nltk.ParentedTree.fromstring("(VP  )")
        
        #     # # Match our pattern to the tree  
        #     subtree = subtree_master(pattern,tree)       
            
        #     # create a new pattern to match a smaller subset of subtree
        #     pattern = nltk.ParentedTree.fromstring("(NP)")

        #     # Find and print the answer
        #     subtree2 = subtree_master(pattern,subtree)

        #     if subtree2 == 'nopes':
        #         return subtree

        #     pattern = nltk.ParentedTree.fromstring("(NP)")

        #     # Find and print the answer
        #     subtree3 = subtree_master(pattern,subtree2)

        #     if subtree3 == 'nopes':
        #         return subtree2

        #     return subtree3




        pattern = nltk.ParentedTree.fromstring("(NP (*) )")
        
        # Match our pattern to the tree  
        subtree = subtree_master(pattern,tree) 

        pattern = nltk.ParentedTree.fromstring("(EX)")

        if subtree_master(pattern, subtree) == 'nopes':

            pattern = nltk.ParentedTree.fromstring("(PRP)")
            if subtree_master(pattern, subtree) == 'nopes':
                return subtree
            else:
                pattern = nltk.ParentedTree.fromstring("(S (NP) )")
                # Match our pattern to the tree  
                subtree = subtree_master(pattern,tree) 

                if subtree == 'nopes':
                    pattern = nltk.ParentedTree.fromstring("(NP (*) )")        
                    # Match our pattern to the tree  
                    subtree = subtree_master(pattern,tree) 
                    return subtree

                pattern = nltk.ParentedTree.fromstring("(NP)")
                # Match our pattern to the tree  
                subtree = subtree_master(pattern,subtree) 
                return subtree
        else:
            pattern = nltk.ParentedTree.fromstring("(VP (*) (NP))")
        
            # Match our pattern to the tree  
            subtree = subtree_master(pattern,tree) 

            pattern = nltk.ParentedTree.fromstring("(NP)")

            subtree = subtree_master(pattern,subtree) 

            
            return subtree


        
        # # create a new pattern to match a smaller subset of subtree
        # pattern = nltk.ParentedTree.fromstring("(NN)")

        # # Find and print the answer
        # subtree2 = subtree_master(pattern,subtree)

        return subtree


    # WHAT - tricky, reads Q last 2 words, then searches for words after them
    elif 'what' in search_words:
        print('what')

        if 'did' in search_words:
            print('what did')
            pattern = nltk.ParentedTree.fromstring("(VP  )")
        
            # # Match our pattern to the tree  
            subtree = subtree_master(pattern,tree)       
            
            # create a new pattern to match a smaller subset of subtree
            pattern = nltk.ParentedTree.fromstring("(NP)")

            # Find and print the answer
            subtree2 = subtree_master(pattern,subtree)

            return subtree2

        elif 'happened' in search_words:
            print('what happened')

        elif 'was' in search_words:
            print('what was')

        pattern = nltk.ParentedTree.fromstring("(NP (*) )")
        
        # Match our pattern to the tree  
        subtree = subtree_master(pattern,tree)       
        
        return subtree

        
        # pattern = nltk.ParentedTree.fromstring("(VP  )")
        
        # # Match our pattern to the tree  
        # subtree = subtree_master(pattern,tree)       

        # pattern = nltk.ParentedTree.fromstring("(PP)")

        # subtree1 = subtree_master(pattern,subtree)

        # if (subtree1 == 'nopes'):

        #     pattern = nltk.ParentedTree.fromstring("(NP  )")
        
        #     # Match our pattern to the tree  
        #     subtree = subtree_master(pattern,tree) 

        #     return subtree

        # pattern = nltk.ParentedTree.fromstring("(NP)")

        # subtree2 = subtree_master(pattern,subtree1)  

        # if (subtree2 == 'nopes'):
        #     return subtree1     




        # return subtree2


        

    # WHERE - looks for POS tag "IN" "DT" "NN" ?
    elif 'where' in search_words:
        print('where')

        pattern = nltk.ParentedTree.fromstring("(PP (IN) (*) )")
        
        # # Match our pattern to the tree  
        subtree = subtree_master(pattern,tree)       
        
        # # create a new pattern to match a smaller subset of subtree
        # pattern = nltk.ParentedTree.fromstring("(IN)")

        # # Find and print the answer
        # subtree2 = subtree_master(pattern,subtree)

        return subtree

    # WHEN - tricky as well, looks for POS "IN"
    elif 'when' in search_words:
        print('when')
        pattern = nltk.ParentedTree.fromstring("(SBAR (*) )")
        
        # # Match our pattern to the tree  
        subtree = subtree_master(pattern,tree)  
        
        # # create a new pattern to match a smaller subset of subtree
        # pattern = nltk.ParentedTree.fromstring("(PP)")

        # # Find and print the answer
        # subtree2 = subtree_master(pattern,subtree)

        return subtree

    # WHY - looks for the word "because" or just the Q and words after it
    elif 'why' in search_words:
        print('why')

        pattern = nltk.ParentedTree.fromstring("(SBAR (IN) (*))")
        
        subtree = subtree_master(pattern,tree)         

        
        # # # create a new pattern to match a smaller subset of subtree
        # pattern = nltk.ParentedTree.fromstring("(IN (*))")

        # # Find and print the answer
        # subtree2 = subtree_master(pattern,subtree)

        return subtree



    elif 'how' in search_words:
        print('how')

        pattern = nltk.ParentedTree.fromstring("(VP (*))")
        
        subtree = subtree_master(pattern,tree)

        pattern = nltk.ParentedTree.fromstring("(ADVP)")
        
        subtree = subtree_master(pattern,subtree)         


        return subtree         


def get_index(answer_sentence,paths):
    fh = open(paths, 'r')
    lines = fh.read()
    fh.close()

    # fname = paths[0]
    # lines = [' '.join(x.splitlines()) for x in lines]
    lines = ''.join(lines.replace('"',''))
    lines = ' '.join(lines.splitlines())
    # lines = ' '.join(lines)
    # print(lines)
    lines = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z][a-z][a-z]\.)(?<![a-z]\.\.\.)(?<=\.|\?|\!)\s",lines) 
    # print(lines)
    # lines = [x.split('.') for val in lines for x in val if '' not in val]
    lines = [" ".join(x.split()) for x in lines]
    lines = [x.replace(' ','') for x in lines]
    # lines = [x.replace(',','') for x in lines]
    lines = [x.lower() for x in lines]
    lines = list(filter(None,lines))
    # print(lines)
    # answer_sentence = ' '.join(answer_sentence.replace('.','').split())
    # answer_sentence = ' '.join(answer_sentence.replace(',','').split())
    # answer_sentence = ' '.join(answer_sentence.replace(',','').split())

    answer_sentence = answer_sentence.lower()

    answer_sentence = answer_sentence.replace(' ','')
    answer_sentence = answer_sentence.replace("``",'')
    # answer_sentence = answer_sentence.replace('"','')


    # print(answer_sentence)


    # try:

    x = lines.index(answer_sentence.lower())

    # except ValueError:

    #     if len(paths) > 1:
    #         fh = open(paths[1], 'r')
    #         lines = fh.readlines()
    #         fh.close()

    #         fname = paths[1]

    #         print(paths[1])

    #         lines = [x.splitlines() for x in lines]
    #         lines = [x.split('.') for val in lines for x in val if '' not in val]
    #         lines = [" ".join(x.split()) for val in lines for x in val]
    #         lines = [x.replace(' ','') for x in lines]
    #         lines = [x.replace(',','') for x in lines]
    #         lines = [x.lower() for x in lines]
    #         lines = list(filter(None,lines))
    #         print(lines)
    #         answer_sentence = ' '.join(answer_sentence.replace('.','').split())
    #         answer_sentence = answer_sentence.replace(' ','')
    #         x = lines.index(answer_sentence)

    #         return x, fname

    #     else:
    #         return 0, paths[0]

    return x








def mr_toads_wild_ride(answer_sentence, question, fname):
    # text_file = "hw8_dataset/fables-02.sch"
    # par_file = "hw8_dataset/fables-02.sch.par"
    zip_folder = 'hw8_dataset.zip'
    folder = 'hw8_stub_code/hw8_dataset/'
    # fnames = [folder + x for x in fnames]
    # print(fnames)

    index = get_index(answer_sentence,folder + fname)

    #gets file name, ex: fables-02
    #how to append? .+type ex: .story ONLY SEND IN ONE TYPE AT A TIME
    par_path = folder + fname + '.par'
    # print(par_path)

    
    # Read the constituency parses into a list 
    trees = read_con_parses(par_path)
    # print(trees)
    
    # We choose trees[1] because we already know that the answer we're looking
    # for is in the second sentence of the text
    tree = trees[index]
    print(tree)

    answer = q_determine(question,tree)

    if answer is not None and answer is not 'nopes':
        print('answer: ' + ' '.join(answer.leaves()))
 


        return ' '.join(answer.leaves())
    else:
        return "answer was none."
    
    # # Create our pattern
    # pattern = nltk.ParentedTree.fromstring("(SBAR (*) )")
    
    # # # Match our pattern to the tree  
    # subtree = pattern_matcher(pattern, tree)
    # print(subtree)
    # print(" ".join(subtree.leaves()))
    
    # # # create a new pattern to match a smaller subset of subtree
    # # pattern = nltk.ParentedTree.fromstring("(PP)")

    # # # Find and print the answer
    # # subtree2 = pattern_matcher(pattern, subtree)
    # # print(" ".join(subtree2.leaves()))



if __name__ == '__main__':

    mr_toads_wild_ride("A trapper spread some net in order to catch a big game .","What did the hunter spread?",'fables-06.sch')
    mr_toads_wild_ride("The lion entangled himself in the net .","Who entangled himself in the meshing?",'fables-06.sch')
    mr_toads_wild_ride("The lion laughed aloud because he thought that the mouse is extremely not able to help him .","Why did the king of beasts laugh?",'fables-06.sch')
    mr_toads_wild_ride("One day the Lion got entangled in a net which had been spread for game by some hunters , and the Mouse heard and recognised his roars of anger and ran to the spot .","Where did the Lion get entangled in one day?",'fables-06.story')
    mr_toads_wild_ride("A few years ago , a young man died out on my front lawn when he crashed his motorbike .","When did the young man die?",'blogs-02.story')