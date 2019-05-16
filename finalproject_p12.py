#Final Project
#
#Sadi Saydam
#
#Part 1
#
#Building an initial text model


#testing code


#Question 3

def clean_text(txt):
        """ takes a string of text and returns a cleaned list"""
        c_list = ''
        for pun in txt:
            if pun not in '.,/?!$%&':
                c_list += pun
        return c_list.lower().split(' ')

def stem(s):
        """accepts a string as a parameter, returns the stem of s."""
        

class TextModel:

#Question 1
    def __init__(self, model_name):
        """ constructs new TextModel object"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.less_freq = {}   #count the words containing less frequent letters in the english language

#Question 2

    def __repr__(self):
        """Return a string representation of the TextModel."""
        
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        return s

#Question 4
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """

        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        word_list = clean_text(s)

        # Template for updating the words dictionary.
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

#Question 5

    def add_file(self, filename):
        """ dds all of the text in the file identified by filename to the model."""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        txt = f.read()
        self.add_string(txt)

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
        

        

                
 
