def main():
    outfile = open('clients.txt','r')
    a=0
    for line in outfile:
        a+=1
        numberedlin = line.rstrip('\n')
        print(a,'. ', numberedlin, sep = '')
    outfile.close()

main()