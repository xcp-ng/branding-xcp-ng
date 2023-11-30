from datetime import date

def get_branding_dict(inputfile):
    branding = {}
    with open(inputfile, 'r') as inputfd:
        for line in inputfd.readlines():
            [key, value] = line.strip().split('=')
            branding[key] = value.replace("@@CURRENT_YEAR@@", str(date.today().year))
    return branding

