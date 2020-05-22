import json

class VerifySentenses:

    def __init__(self, input, filePath):
        
        self.input = input
        self.filePath = filePath
        self.response = ''

    def getResponse(self):
        
        genericSentencesPath = self.filePath
        with open(genericSentencesPath, 'r') as json_file:
            dados = json.load(json_file)

        return dados['saudation'][self.input]


