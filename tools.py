import wptools

def get_meta(title):
    soup = wptools.page(title).get_parse()
    infobox = soup.data['infobox']
    return infobox