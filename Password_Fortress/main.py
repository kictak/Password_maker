# import PASSWORD
import secrets
import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def roll_dice():
    for _ in range(30):
        print(r"""
                       Good!!!
                Now I'll roll the dice
                        $ _ $
                    ____
                   /\' .\    _____ 
                  /: \___\  / .  /\
                  \' / . / /____/  \
                   \/___/  \'  '\ ./
                            \'__'\/

            """)
        time.sleep(0.3)
        clear_screen()
        print(r"""
                       Good!!!
                Now I'll roll the dice
                        $ _ $
                    ____ 
                (  /\' .\ )) _____ ))
                  /: \___\  / .  /\
                  \' / . / /____/  \ ))
                (( \/___/  \'  '\ ./
                         )  \'__'\/
                                        
            """)
        time.sleep(0.3)
        clear_screen()
        print(r"""
                       Good!!!
                Now I'll roll the dice
                        $ _ $
                             ____   
                   _____    /\' .\  
                  / .  /\  /: \___\ 
                 /____/..\ \' / . / 
                 \'  '\  /  \/___/  
                  \'__'\/                
                                        
            """)
        time.sleep(0.3)
        clear_screen()
        print(r"""
                       Good!!!
                Now I'll roll the dice
                        $ _ $
                             ____   
                   _____ (( /\' .\ }) 
                  / .  /\  /: \___\ 
            ((   /____/..\ \' / . / 
                 \'  '\  /{(\/___/  
                  \'__'\/         ))       
                {        }}                   
            """)
        time.sleep(0.3)
        clear_screen()


def main():
    print("""
                    Hi i'm Passw ^_^\n
          I'm generate for you strong passwod\n
            Please input something like this\n
                890yh334ih2903yhf0#H9-1
          """)
    user_input = input("         ->")
    clear_screen()
    roll_dice()
    password = PASSWORD.generate_password(user_input)
    print(f"""
            Here you pass ^_-
             {password}
          """)


if __name__ == "__main__":
    main()
