##############
# Alex Lang
# Conor Rogers
#
# HW 6
#
# FETCH SENTENCE
#	recieves Q, type, fetches the sentence from .story or .sch file that holds the correct answer to the Q
##############

def find_best_sentence(question, fnames):
	

	return

# 1. open story/sch file or both for q
# 2. use super s1ck algorithms to find the best sentence
#	(if story | sch, open both and find best matching sentence)
# 3. return best sentence
def fetch(fname, question, q_type):
	# ready storyname to open
	fname = fname.split('-')
	fname = fname[0] + "-" + fname[1]
	# print(fname)

	# ready what kind of storyname to open
	if "|" in q_type:
		q_type = q_type.split(' | ')
	else:
		q_type = [q_type]
	#print(q_type)

	fname = [fname + '.' + t for t in q_type]
	print(fname)

	# pass in q and filename(s), find best SENTENCE YEAAAAAA
	answer_sentence = find_best_sentence(question, fname)

	return answer_sentence

if __name__ == '__main__':
	fetch()