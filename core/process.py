import config, re

def space(comment):
    return " ".join(comment.split())

def add_tags(comment):
    new_comment = re.sub(r'[^\w\s]','', comment) #del all what it isn't letter
    words = new_comment.split()
    tags = []
    if any(word.lower() in config.hate_words for word in words):
        tags.append("[HATE]")

    if any(word.lower() in config.vulgar_words for word in words):
        tags.append("[VULGAR]")

    if sum(word.isupper() for word in words) > 2:
        tags.append("[SHOUT]")

    return f"{comment} {''.join(tags)}" if tags else comment

def word_masking(comment):
    com = []
    for index, word in enumerate(comment.split()):
        if word.lower() in config.vulgar_words:
            com.append(f"{word[0]}{(len(word) - 1) * '*'}")
        else:
            com.append(word)
    return " ".join(com)

