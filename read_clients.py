def main():
    
    client_no = 0
    infile = open('clients.txt','r')

    for line in infile:
        client_no += 1
        client = line.rstrip('\n')
        print(f'{client_no}. {line}')


    print(f'\n{"Total number of clients: "}{client_no}')


main()