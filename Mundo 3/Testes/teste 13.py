a0=1
q=4
for n in range(1,15):
    progressão=a0*((q**n)-1)/(q-1)
    print(f'{n}: {progressão:.0f}')
