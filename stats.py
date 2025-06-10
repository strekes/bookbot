

def word_count(text):
    words = text.split()
    return len(words)

def repeats(text):
    lc_text = text.lower()
    letter = ''
    count = 0
    count_dict = {}

    for each in lc_text: 
        if each.isalpha():  
            if each not in count_dict:
                count_dict[each] = 1
            else:
                count_dict[each] += 1
    return count_dict

def sort_dict(count_dict):
    sectioned_list = []
    for key, value in count_dict.items():
        sectioned_list.append({"char": key, "num": int(value)})
    
    return sorted(sectioned_list, key=lambda x: x["num"], reverse=True)
