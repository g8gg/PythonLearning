# G8GG's quote
# for testing access global variables from importing(part) function
global_data = "马骏"


def get_quote():
    """Return random sayings from G8GG"""
    from random import choice  # import special function from module
    possibilites = ['锅巴GG是个好人', '锅巴GG是个男人', '锅巴GG是个技术人', '锅巴GG是个社区人']
    return choice(possibilites)


def fake():
    """just demo import function"""
    pass


def get_author():
    global global_data
    return global_data


def set_author(new):
    global global_data
    global_data = new
    return global_data
