import libvoikko
libvoikko.Voikko.setLibrarySearchPath("c:/Voikko")
v = libvoikko.Voikko(u"fi")
word = "koirienkin"

print(f"Analyze word: {word}")
print(v.analyze(word))

word = "koirienkkin"
print(f"Check spelling for {word}")
print(str(v.spell(word)))

print(f"Suggest correct word for {word}")
print(v.suggest(word))
