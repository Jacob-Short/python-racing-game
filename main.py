print('''
*******************************************************************************
                              _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\";
                        .'                              ;   _____;   \\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":           """----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"        1 s t         .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------"
*******************************************************************************
''')
print("Welcome to Lake Oswego Drift")
print("Your mission is to place 1st and win the prize money $")
choice1 = input(
    'You\'ve just arrived at the rondevu. Drive "left" to the start line or drive "right" to the parking area?').lower()

if choice1 == 'left':
    choice2 = input('You pull up next to 3 other cars. 2 of which you know you can take. But you see your rival on the end. Drive "straight" to line \n up on the opposing end or drive "right" to leave while you still can before he sees you?').lower()
    if choice2 == 'straight':
        print("The race is getting ready to begin. To your mark.. Set. GO!")
        choice3 = input('Your rival takes the lead but you are not far behind him. Do you "smash" his car or go "around" him?').lower()
        if choice3 == 'around':
            print('You maneuver around your rival and speed up the right side! He cannot catch up with your excellent start. You win the race!  Collect Your prize!')
        else:
            print('You smash his car and you spin out of control. He speeds off with little damage and wins the race. Game over.')
    else:
        print('You not only miss out on the prize money, but your rival saw your car on the way out. Game over. ')
else:
    print('You drove over a nail in the road. Game over')
