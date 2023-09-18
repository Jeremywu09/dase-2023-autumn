def getMaxDupChar(s,startIndex,curMaxLen,maxLen):
    if startIndex == len(s)-1:
        return max(curMaxLen,maxLen)
        if list(s)[startIndex] == list(s)[startIndex + 1]:
            return getMaxDupChar(s,startIndex + 1,curMaxLen + 1,maxLen)
        else:
            return getMaxDupChar(s,startIndex + 1,1,max(curMaxLen,maxLen))
            if_name_ == '_main_':
            s = getMaxDupChar('abbabc',0,1,1)
            print(s)