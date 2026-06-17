def make_snippet(text):
    words = text.split()

    if len(words) > 5:
        first_five = words[:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    return text 