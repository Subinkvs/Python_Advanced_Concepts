class Language:
    
    def __init__(self, name):
        self.name = name
        
    def message(self):
        print(self.name)
        
        
Languages = [Language("Python"), Language("Javascript")]


for language in Languages:
    language.message()