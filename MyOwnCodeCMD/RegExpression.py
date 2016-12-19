import sys

class RegExpression:


    optionalLeftParanthesis = '' 
    optionalRightParanthesis = ''
    httpVersios = ''
    anyCharacter = ''
    whiteSpcae = ''
        
    def __init__(self):
        self.optionalLeftParanthesis = "\(?"
        self.optionalRightParanthesis = "\)?"
        self.httpVersios = "((http://)|(https://))"
        self.anyCharacter = "\S+"
        self.whiteSpcae = "\s"
        self.optionalWhiteSpace= "\s?"
        self.atSign = "\@"
        self.mentionString = "([A-Za-z0-9_]+)"
        self.HashtagString = "[A-Za-z0-9][A-Za-z0-9_-]*"
        self.Hashtag = "#"
        self.EmoticonPart = "[A-Za-z0-9_-]*"
        self.EmoticonMark = "[\?]+"

    def buildMentions(self):
        #\(?\@([A-Za-z0-9_]+)\)?\s?
        return self.optionalLeftParanthesis + self.atSign + self.mentionString + self.optionalRightParanthesis + self.optionalWhiteSpace 

     
    def buildURLs(self):
        #
        return self.optionalLeftParanthesis + self.httpVersios + self.anyCharacter + self.optionalRightParanthesis + self.optionalWhiteSpace 

    def buildHashtags(self):
        # #([A-Za-z0-9_-]+)
        return self.Hashtag + self.HashtagString


    def buildEmoticons(self):
        # #([A-Za-z0-9_-]*?+[A-Za-z0-9_-]*)
        return  self.EmoticonPart + self.EmoticonMark + self.EmoticonPart
