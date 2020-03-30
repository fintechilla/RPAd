class Word:
    def splitAndRemoveLeadBlanks(self, line, separator):
        split_words = line.split(separator)
        outLine = []
        for word in split_words:
            outLine.append(word.lstrip(" "))

        return outLine
