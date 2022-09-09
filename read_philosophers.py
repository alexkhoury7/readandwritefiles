def main():
    outfile = open('philosophers.txt','r')
    line1 = outfile.readline().rstrip('\n')
    line2 = outfile.readline().rstrip('\n')
    line3 = outfile.readline().rstrip('\n')


    print(line1)
    print(line2)
    print(line3)
    outfile.close()

main()