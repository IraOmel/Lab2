class Text:
    def __init__(self, filename):
        self.filename = filename

    def work_with_text(self):
        try:
            with open(self.filename, 'r') as myfile:
                data = myfile.read()
        except FileNotFoundError:
            quit("File not found")
        numberOfStr = data.count(".") + data.count("?") + data.count("!")
        return f'Characters: {len(data)}, Words: {len(data.split())}, Sentences: {numberOfStr}'


obj1 = Text('text.txt')
print(obj1.work_with_text())
