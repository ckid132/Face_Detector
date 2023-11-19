from getchar import Getchar

def main(args=None): #메인함수가 존재하지만 명시적으로 사용할때 사용
    kb = Getchar()
    key = ''
    
    while key!='Q':
    
        key = kb.getch()
        if key != '':
            print(key)
        else:
            pass
        

if __name__ == '__main__':
    main()

