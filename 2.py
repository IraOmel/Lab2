import os.path

class Text:
    """A class that get file direction."""
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise OSError("no such direction")
        self.filename = filename

    def characters(self):
        """"Function that counting of characters in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            count_characters = len(data)
        myfile.close()
        return f'Characters: {count_characters},'

    def words(self):
        """"Function that counting of word in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            count_words = len(data.split())
        myfile.close()
        return f'Words: {count_words},'

    def sentences(self):
        """"Function that counting of sentences in file and return their amount."""
        with open(self.filename, 'r') as myfile:
            data = myfile.read()
            number_of_str = data.count(".") + data.count("?") + data.count("!")
        myfile.close()
        return f'Sentences: {number_of_str}.'


obj1 = Text('text.txt')
print(obj1.characters() + ' ' + obj1.words() + ' ' + obj1.sentences())
