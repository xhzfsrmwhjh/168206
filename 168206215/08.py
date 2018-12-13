start='hit'
end='cog'
adict=['hot','dot','dog','lot','log']
def find_path(start,end,paths):
    if start==end:
        return "start=end"
    else:
        visited =[]
        visited.append(start)
        for word in visited:
            print(word)
            for i in range(len(word)):
                for j in range(ord('a'),ord('z')+1):
                    word=word[:i]+chr(j)+word[i+1:]
                    print(word)
                    if word in paths:
                        visited.append(word)

find_path(start,end,adict)
