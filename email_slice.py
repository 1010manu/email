def main():
    print('welcome to email slicer')
    email=input('enter the email:')
    if '@' in email and '.' in email:
        (user,domain)=email.split('@')
        (domain,extension)=domain.split('.')
        print('user:',user)
        print('domain:',domain)
        print('extension:',extension)
    else:
        print('invalid')
while True:
    main()
    break
