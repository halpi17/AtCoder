S1 = input()
S2 = input()
S3 = input()
S4 = input()

pencils = ['H', '2B', '3B', 'HR']

def pencil_confirmation(pencils, confirm_pencil):
    try:
        pencils.remove(confirm_pencil)
    except:
        pass

pencil_confirmation(pencils, S1)
pencil_confirmation(pencils, S2)
pencil_confirmation(pencils, S3)
pencil_confirmation(pencils, S4)

if pencils:
    print('No')
else:
    print('Yes')