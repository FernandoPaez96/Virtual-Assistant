import wikipedia

wikipedia.set_lang("es")
print(wikipedia.summary("que es newells", sentences=1))