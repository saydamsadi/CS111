#Final Project
#
#Sadi Saydam
#
#Part III-IV
#
#Creating a text comparison 


def summer(s):
        """Helper function to sum all values from less_freq dictionary""" 
        summ = 0
        for n in s:
                if n not in 'abcdefghijklmnopqrstuvwxyz':
                      summ += n
        return summ

def clean_text(txt):
        """ takes a string of text and returns a cleaned list"""
        c_list = ''
        for pun in txt:
            if pun not in '.,/?!$%&':
                c_list += pun
        return c_list.lower().split(' ')

def prefix(s):
        """helper function for stem, that takes out the prefix in a word s"""
        if (s[:4] == 'semi' or s[:4] == 'anti' or s[:4] == 'fore' or s[:4] == 'over') and len(s)>= 7:
                s = s[4:]
                return s
        if (s[:3] == 'pre' or s[:3] == 'non' or s[:3] == 'mid' or s[:3] == 'mis' or s[:3] == 'sub') \
           and len(s) >= 6:
                s = s[3:]
                return s
        if (s[:2] == 'un' or s[:2] == 're' or s[:2] == 'in' or s[:2] == 'im' or s[:2] == 'de' \
            or s[:2] == 'en' or s[:2] == 'in') and len(s) >= 5:
                s = s[2:]
                return s
        return s

def stem(s):
        """accepts a string as a parameter, returns the stem of s."""
        c_prefix = prefix(s) 
        s = c_prefix
        #4 letter suffixes
        if len(s) <= 4:
                return s
        if (s[-4:] == 'able' or s[-4:] == 'ible' or s[-4:] == 'tion' or s[-4:] == 'less' or s[-4:] == 'ness' \
            or s[-4:] == 'ment' or s[-4:] == 'sion' or s[-4:] == 'ance' or s[-4:] == 'ence') and len(s) >= 7:
                s = s[:-4]
                if len(s) > 4:
                        if s[-1] == s[-2]:
                                s = s[:-1]
                                return s
                return s
        #3 letter suffixes
        if (s[-3:] == 'est' or s[-3:] == 'ful' or s[-3:] == 'ing' or s[-3:] == 'ity' or s[-3:] == 'acy' \
            or s[-3:] == 'dom' or s[-3:] == 'ism' or s[-3:] == 'ify' or s[-3:] == 'ize' \
            or s[-3:] == 'ish' or s[-3:] == 'ive' or s[-3:] == 'ous') and len(s) >= 6:
                s = s[:-3]
                if len(s) > 4:
                        if s[-1] == s[-2]:
                                s = s[:-1]
                                return stem(s)
                return stem(s)
        #2 letter suffixes
        if (s[-2:] == 'ed' or s[-2:] == 'en' or s[-2:] == 'er' or s[-2:] == 'ly' or s[-2:] == 'al' \
            or s[-2:] == 'ty' or s[-2:] == 'or' or s[-2:] == 'es' or s[-2:] == 'ic') and len(s) >= 5:
                s = s[:-2]
                if len(s) > 4:
                        if s[-1] == s[-2]:
                                s = s[:-1]
                                return stem(s)
                return stem(s)
        #1 letter suffixes
        if s[-1] == 's' and len(s) > 3:
                s = s[:-1]
                return stem(s)
        
        return s
#Naive Bayes Algorithm part
def compare_dictionaries(d1, d2):
        """takes 2 dictionaries and computes their log similarity score"""
        score = 0
        total = 0
        for x in d1:
                total += d1[x]
        for x in d2:
                if x in d1:
                       score += math.log(d1[x]/total) * d2[x]
                else:
                       score += math.log(0.5/total) * d2[x]
        return score

# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def test():
    """ Test the program for source 1 and source2 """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ Test the program for source 1 and source2 and different texts"""
    source1 = TextModel('jrrtolkien')
    source1.add_file('jrrtolkien.txt')

    source2 = TextModel('grrmartin')
    source2.add_file('grrmartin.txt')

    new1 = TextModel('random drwho')
    new1.add_file('drwho.txt')
    new1.classify(source1, source2)

    new1 = TextModel('random startrek')
    new1.add_file('startrek.txt')
    new1.classify(source1, source2)

    new1 = TextModel('random nytimes')
    new1.add_file('nytimes.txt')
    new1.classify(source1, source2)

    new1 = TextModel('ame')
    new1.add_file('ame.txt')
    new1.classify(source1, source2)
        
import math

class TextModel:

#Question 1
    def __init__(self, model_name):
        """constructs new TextModel object"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.less_freq = {}   #count the number of less frequent letters in the english 
                              # language in the text per sentence
                              # letters used are qjzxvkwQJZXVKW 
        
#Question 2

    def __repr__(self):
        """Return a string representation of the TextModel."""
        
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of less frequent letters: ' + str(sum((self.less_freq.values()))/len(self.sentence_lengths)) + '\n'
        return s

#Question 4
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        # Update Sentence Lengths
        sen_words = s.split()
        sen_list = []
        sen_len = 0
        for w in sen_words:
                sen_len += 1
                if w[-1] == '.' or w[-1] == '!' or w[-1] == '?':
                        sen_list += [sen_len]
                        sen_len = 0
        for i in sen_list:
                if i in self.sentence_lengths:
                        self.sentence_lengths[i] += 1
                else:
                        self.sentence_lengths[i] = 1
        # Update words dictionary 
        
        word_list = clean_text(s)
        
        for w in word_list:
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
            len_w = len(w)
            if len_w in self.word_lengths:
                self.word_lengths[len_w] += 1
            else:
                self.word_lengths[len_w] = 1
            if stem(w) in self.stems:
                self.stems[stem(w)] += 1
            else:
                self.stems[stem(w)] = 1
        # Update less_freq dictionary
        count_letter = 0
        for w in word_list:
                for i in w:
                    if i in 'qjzxvkwQJZXVKW':
                        count_letter += 1
                        if i in self.less_freq:
                                self.less_freq[i] += 1
                        else:
                                self.less_freq[i] = 1
                
        

#Question 5

    def add_file(self, filename):
        """ dds all of the text in the file identified by filename to the model."""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = f.read()
        self.add_string(txt)

#Part IV
#Question 2
        
    def similarity_scores(self, other):
        """ that computes and returns a list of log similarity scores
        measuring the similarity of self and other """
        score_list = []
        score_list += [compare_dictionaries(other.words, self.words)]
        score_list += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        score_list += [compare_dictionaries(other.stems, self.stems)]
        score_list += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        score_list += [compare_dictionaries(other.less_freq, self.less_freq)]
        return score_list
#Question 3
    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other “source”
            textModel objects (source1 and source2) and determines which of
            these other TextModels is the more likely source of the called TextModel."""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name, ': ', str(scores1), '\n')
        print('scores for', source2.name, ': ', str(scores2), '\n')

        weighted_sum1 = 5*scores1[0] + 5*scores1[1] + 7*scores1[2] + 9*scores1[3] + 20*scores1[4]
        weighted_sum2 = 5*scores2[0] + 5*scores2[1] + 7*scores2[2] + 9*scores2[3] + 20*scores2[4]
        if weighted_sum1 > weighted_sum2:
                print(self.name, 'is more likely to have come from', source1.name, '\n')
        else:
                print(self.name, 'is more likely to have come from', source2.name, '\n')
                

#Part II: Saving and retrieving a text model
#
#Question 1 
        
    def save_model(self):
        """ saves the TextModel by writing various feature dictionaries to files."""
        f = open(self.name + '_' + 'words', 'w')   
        f.write(str(self.words))              
        f.close()

        f = open(self.name + '_' + 'word_lengths', 'w')   
        f.write(str(self.word_lengths))              
        f.close()

        f = open(self.name + '_' + 'stems', 'w')   
        f.write(str(self.stems))              
        f.close()

        f = open(self.name + '_' + 'sentence_lengths', 'w')   
        f.write(str(self.sentence_lengths))              
        f.close()

        f = open(self.name + '_' + 'less_freq', 'w')   
        f.write(str(self.less_freq))              
        f.close() 

#Question 2

    def read_model(self):
        """ reads the stored dictionaries for the TextModel from the corresponding files"""   
        f = open(self.name + '_' + 'words', 'r')    
        words_str = f.read()          
        f.close()

        self.words = dict(eval(words_str))

        f = open(self.name + '_' + 'word_lengths', 'r')    
        word_lengths_str = f.read()          
        f.close()

        self.word_lengths = dict(eval(word_lengths_str))

        f = open(self.name + '_' + 'stems', 'r')    
        stems_str = f.read()          
        f.close()

        self.stems = dict(eval(stems_str))

        f = open(self.name + '_' + 'sentence_lengths', 'r')    
        sentence_lengths_str = f.read()          
        f.close()

        self.sentence_lengths = dict(eval(sentence_lengths_str))

        f = open(self.name + '_' + 'less_freq', 'r')    
        less_freq_str = f.read()          
        f.close()

        self.less_freq = dict(eval(less_freq_str))
        
        

        

                
 
