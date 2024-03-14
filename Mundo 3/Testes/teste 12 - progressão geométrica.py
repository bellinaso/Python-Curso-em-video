n=1
a0=1
q=4
while True:
    progressão=a0*((q**n)-1)/(q-1)
    print(f'{n}: {progressão:.0f}')
    n+=1
    if progressão==89478485:
        break
