
def build_profile(firstname, lastname, **user_info):
    ''' build a dictionary containing everything we know about a user '''
    profile = {}
    profile['first'] = firstname
    profile['last'] = lastname

    for key, value in user_info.items():
        profile[key] = value
    return profile

profile_info = build_profile('gowtham', 'sridhar', location='thanjavur', occupation='engineer')
print(profile_info)