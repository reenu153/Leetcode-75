class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        dups=defaultdict(list)

        for path in paths:
            data=path.split()
            root=data[0]
            for file in data[1:]:
                name,_,content= file.partition("(")
                sign=root+"/"+name
                dups[content].append(sign)

        return [path for path in dups.values() if len(path)>1]

