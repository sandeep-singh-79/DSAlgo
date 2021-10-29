# print the duplicate word from the string
# Input : "I am ok but not ok I am i was"
# output: I am ok

def printDuplicateWords(string: str):
    if string:
        wordFrequency = dict()

        words = string.upper().split(" ")

        # capture the frequency of each of the words in the sentence
        for word in words:
            if word in wordFrequency.keys():
                wordFrequency[word] += 1
                print(word, end=" ")
            else:
                wordFrequency[word] = 1
        
        # print the words with frequency > 1
        # for key in wordFrequency.keys():
        #     if wordFrequency[key] > 1:
        #         print(key, end= " ")


if __name__ == "__main__":
    printDuplicateWords("I am ok but not ok I am i was")