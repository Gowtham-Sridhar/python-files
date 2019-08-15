
unconfirmed_users = ['sudhakar', 'monesh', 'mani', 'siva']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed.')
for confirmed_user in confirmed_users:
    print('\t' + confirmed_user.title())