import tldextract, emoji

def is_link(url):
    extracted = tldextract.extract(url)
    return bool(extracted.suffix and extracted.domain)

def len_word(word):
    return 24 if (is_link(word) and len(word) <= 1972) else (len(word) + emoji.emoji_count(word) + 1) 


def split_text(text, limit=280):
    
    MAX_CH = limit-6
    words = text.split(' ')
    current_part = ''
    current_len = 0
    parts = []

    for word in words:
        word_len = len_word(word)    

        while word_len > MAX_CH:
            if current_part:
                current_part = ' '.join((current_part, word[:(MAX_CH-current_len)]))
            else:
                current_part = word[:MAX_CH]
            parts.append(current_part)
            word = word[MAX_CH-current_len:]
            word_len = len_word(word)
            current_part = ''
            current_len = 0
            

        if current_len + word_len <= MAX_CH:
            if current_part:
                current_part = ' '.join((current_part, word))
            else: 
                current_part = word
            current_len += word_len
        else:
            parts.append(current_part)
            current_part = word
            current_len = word_len
    else: parts.append(current_part)

    if(parts[0]):
        for ind in range(len(parts)):
            parts[ind]+=f' {ind+1}/{len(parts)}'
    else: parts = []    

    return parts

