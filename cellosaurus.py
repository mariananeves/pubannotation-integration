
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

# text: text to be processed
# cell lines predicted by the annotator: http://pubannotation.org/annotators/Cellosaurus_v33
# entities predicted by the PubTator annotator: http://pubannotation.org/annotators/PubTator
# cell lines and entities should be a Python dictionary following the JSON format supported by PubAnnotation
def filter_cell_lines(text,cell_lines,entities):
	#print(entities)
	filtered = []
	for cell_line in cell_lines:
		begin = int(cell_line['span']['begin'])
		end = int(cell_line['span']['end'])
		span = text[begin:end]
		if is_short_entity(span):
			continue
		if not is_alphanumeric(span):
			continue
		if is_stopword(span):
			continue
		if entities!=None and is_overlap_entity(begin,end,entities):
			continue
		filtered.append(cell_line)
	return filtered

def is_overlap_entity(begin,end,entities):
	for entity in entities:
		#print(entity)
		if (begin>=entity['span']['begin'] and begin<=entity['span']['end']) or (end>=entity['span']['begin'] and end<=entity['span']['end']):
			return True
	return False

def is_alphanumeric(span):
	if span.isalnum():
		return True
	return False

def is_short_entity(span):
	if len(span)<=2:
		return True
	return False

def is_stopword(span):
	if span in stopWords:
		return True
	return False

if __name__ == '__main__':
	main()
