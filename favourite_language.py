
favourite_language = {
    'gowtham': ['python'],
    'monesh': ['java', 'c', 'c++'],
    'dinesh': ['c#', 'perl'],
    'chandru': ['java', 'c', 'python', 'perl'],
    'testuser': []
}

for name, languages in favourite_language.items():

    if len(languages) > 1:
        print('\n' + name.title() + ' favourite languages are:')
        for language in languages:
            print('\t' + language.title())
    else:
       print('\n' + name.title() + ' favourite languages are: ' + languages.pop())
