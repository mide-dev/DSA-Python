try:
    for line in sys.stdin:
        print(line)
        
except EOFError:
    print('yh')
