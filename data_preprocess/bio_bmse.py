inputf = "/Users/liuman/Documents/NLP/NER/mrc-for-flat-nested-ner-master/data_preprocess/example/ace05/test.bio2"
outputf = "/Users/liuman/Documents/NLP/NER/mrc-for-flat-nested-ner-master/data_preprocess/example/ace05/test.bsme"
data_li = []
with open(inputf) as inf:
	inf_d = [line.strip() for line in inf.readlines()]
	for idx, line in enumerate(inf_d):
		if not line:
			data_li.append(line)
		else:
			li = line.split()
			word, pos = li[0], li[-1]
			curtag = pos[2:]
			nextline = inf_d[idx+1] if idx < len(inf_d) else ""
			nextpos = nextline if not nextline else nextline.split()[-1]
			nexttag = "" if not nextpos else nextpos[2:]
			if pos.startswith("B-"):
				if not nextpos or nextpos == "O":
					new_line = "{} S-{}".format(word, pos[2:])
				else:
					new_line = "{} B-{}".format(word, pos[2:])
			elif pos.startswith("I-"):
				if not nextpos or nextpos == "O":
					new_line = "{} E-{}".format(word, pos[2:])
				else:
					new_line = "{} M-{}".format(word, pos[2:])
			else:
				new_line = "{} {}".format(word, "O")
			data_li.append(new_line)


with open(outputf, "w") as outf:
	for line in data_li:
		outf.write(line + "\n")