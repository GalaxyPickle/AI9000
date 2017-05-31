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
def start(response):
	with open('train_my_answers.txt', 'w') as f:
		[f.write('QuestionID: {0}\nAnswer: {1}\n\n'.format(q, a))
			for q, a in response]

if __name__ == '__main__':
	start()














# EOF #