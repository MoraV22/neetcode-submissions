class TreeNode:
    def __init__(self, val=""):
        self.val=val
        self.children={}
        
    
    def add(self, s):
        if not s:
            return
        try:
            node= self.children[s[0]]
        except:
            self.children[s[0]]=TreeNode(s[0])
        self.children[s[0]].add(s[1:])

    def look(self, val):
        children=self.children
        for char in val:
            try:
                node=children[char]
                children= node.children
            except:
                return False
        return True     
            


class PrefixTree:

    def __init__(self):
        self.words=set()
        self.trie= TreeNode()

    def insert(self, word: str) -> None:
        self.words.add(word)
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return word in self.words
        

    def startsWith(self, prefix: str) -> bool:
        return self.trie.look(prefix)
        
        