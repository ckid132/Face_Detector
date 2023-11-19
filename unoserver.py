from getchar import Getchar
import serial 

sp = serial.Serial('COM3', 9600, timeout = 1)
kb = Getchar()
key = ' '

while key != 'Q':
    key = kb.getch()
    if key == '.':
        sp.write('.'.encode())
    elif key ==',':
        sp.write(','.encode())
    elif key =='1':
        sp.write('1'.encode())
    elif key =='2':
        sp.write('2'.encode())
    elif key =='3':
        sp.write('3'.encode())
    
    else:
        pass