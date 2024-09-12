def top_3_words(text):
    new_text = text
    invalid_chars = ["*",";",":","/",",",".","..","...","'''","-","_","!","?"]
    special_chars = ["'", " "]
    for t in text:
        if t in invalid_chars:
            new_text = new_text.replace(t, " ")
    words_array = new_text.split()
    i = 0
    for word in words_array:
        clean_word = word
        for c in word:
            if c in invalid_chars and c != "'":
                clean_word = word.replace(c, '')
                if len(clean_word) < 1:
                    i = i -1
        if len(clean_word) > 0:
            words_array[i] = clean_word.lower()
        
        if word in invalid_chars or word in special_chars:
            words_array.remove(word)
        else:
            i = i + 1

    unique = list(set(words_array))
    count = []
    final = []
    for v in unique:
        tim = 0
        for word in words_array:
            if v == word:
                tim = tim + 1
        count.append(tim)      
        
    if len(count) > 0:
        max_index = count.index(max(count))
    else:
        max_index = 0
    for i in range(3):
        if len(unique) > 0:
            final.append(unique[max_index])
            del unique[max_index]
            del count[max_index]
            if len(count) > 0:
                max_index = count.index(max(count))

    
    return final

