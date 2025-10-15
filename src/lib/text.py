import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.split() #Create a list to remove the specials chars.
    text=" ".join(text) #Join the elementes on the list, separating by one space.
    if casefold: #If casefold not disabled
        text = text.casefold() # do the caefold(). It's Like lowerse() forced.
    if yo2e: #If yo2e not disabled:
        #do the lower case. Subs all "Ё/ё"  by "E/e".
        text = text.replace("Ё", 'E').replace('ё','e') 
    return text

def tokenize(text: str) -> list[str]:
    # The regular expression finds (and put it in var "default"):
        # 1. Words containing a hyphen (\w+-\w+)
        # 2. Numbers (\d+)
        # 3. Letter/number/underscore pattern words (\w+)
    default = r"\w+-\w+|\d+|\w+"
    #Find all pattern characters in text and return only these.
    return re.findall(default, text.lower())

def count_freq(tokens: list[str]) -> dict[str, int]:
    dictionary={} #Our dictionary
    tokens=sorted(tokens) #Organizing the list alphabetically
    for letters in tokens: #Loop to count all letters/chars
        if letters in dictionary: #if finded letter is already in dictionary:
            dictionary[letters] +=1 #So, incrise d times its repeated.
        else: #Otherwise:
            dictionary[letters]=1 #It's d 1st time.
    return dictionary

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    #Basecaly "freq.items()" return a tuple
        #"key=lambda item:item[1]" index 1 will be the main item to make sorted()
        # "reverse=True" - descendent order.
    sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    #Return the new "sorted_items" 'till index "n".
    return sorted_items[:n]