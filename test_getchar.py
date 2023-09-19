import getchar

def main(args=None):


    kb = getchar.Getchar()
    key = ''
        
    while key!='Q':

        key = kb.getch()
        if key != '':
            print(key)
        else:
            pass
           
if __name__ == '__main__':
    main()