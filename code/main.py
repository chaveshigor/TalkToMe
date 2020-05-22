from getInput import GetInput
from verifySentencesFile import VerifySentenses as Vs

genericSentencesPath = "C:/Users/higor/OneDrive/scripts python/TalkToMe/sentencesFile/genericSentences.json"

input = GetInput().getTestInput()
response = Vs(input, genericSentencesPath).getResponse()

print(response)