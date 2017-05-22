##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# WRITE ANSWERS
#	recieves the final answers and writes them to a file and the console
##############

# this writes to the output file [question, answer, newline] ...
def start(responses):
	with open('train_my_answers.txt', 'r') as f:
		[f.write('{0}\n{1}\n'.format(questions, answers)) 
			for questions, answers in responses]





if __name__ == '__main__':
	start()














# EOF #