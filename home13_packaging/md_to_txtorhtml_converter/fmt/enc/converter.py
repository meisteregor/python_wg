from fmt.tokens import Header, Em, Strong


def convert(tokens, format):
    result = []
    for token in tokens:
        if isinstance(token, Header):
            result.append(format.convert_header(token))
        elif isinstance(token, Em):
            result.append(format.convert_em(token))
        elif isinstance(token, Strong):
            result.append(format.convert_strong(token))
        else:
            result.append(format.convert_text(token))
    return result
