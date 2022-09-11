stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
win = """YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU     WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNN
Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U     W::::::W                           W::::::WI::::::::IN:::::::N       N::::::N
Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U     W::::::W                           W::::::WI::::::::IN::::::::N      N::::::N
Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU     W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::N
YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U       W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::N
   Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U        W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::N
    Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U         W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::N
     Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U          W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::N
      Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U           W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::N
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U            W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::N
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U             W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::N
       Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U              W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::N
       Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U               W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::N
    YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU                 W:::::W         W:::::W          I::::::::IN::::::N       N:::::::N
    Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU                    W:::W           W:::W           I::::::::IN::::::N        N::::::N
    YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU                       WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNN
                                                                                                                                               """
lose = """YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU     LLLLLLLLLLL                  OOOOOOOOO        SSSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEE
Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U     L:::::::::L                OO:::::::::OO    SS:::::::::::::::SE::::::::::::::::::::E
Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U     L:::::::::L              OO:::::::::::::OO S:::::SSSSSS::::::SE::::::::::::::::::::E
Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU     LL:::::::LL             O:::::::OOO:::::::OS:::::S     SSSSSSSEE::::::EEEEEEEEE::::E
YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U        L:::::L               O::::::O   O::::::OS:::::S              E:::::E       EEEEEE
   Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::OS:::::S              E:::::E             
    Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O S::::SSSS           E::::::EEEEEEEEEE   
     Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O  SS::::::SSSSS      E:::::::::::::::E   
      Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O    SSS::::::::SS    E:::::::::::::::E   
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O       SSSSSS::::S   E::::::EEEEEEEEEE   
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O            S:::::S  E:::::E             
       Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U        L:::::L         LLLLLLO::::::O   O::::::O            S:::::S  E:::::E       EEEEEE
       Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U      LL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::OSSSSSSS     S:::::SEE::::::EEEEEEEE:::::E
    YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU       L::::::::::::::::::::::L OO:::::::::::::OO S::::::SSSSSS:::::SE::::::::::::::::::::E
    Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU         L::::::::::::::::::::::L   OO:::::::::OO   S:::::::::::::::SS E::::::::::::::::::::E
    YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU           LLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO      SSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEE"""