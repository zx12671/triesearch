import marisa_trie
# trie = marisa_trie.Trie([u"我", u'北京', u'天安门',"key1"])
trie = marisa_trie.Trie(['key1', 'key2', 'key12','我'])

trie.prefixes(u'我')
trie.prefixes('key12')
while True:
    print("input text")
    text = input()
    print(trie.prefixes(text))