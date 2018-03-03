IF MESSAGE : Store mode?
LABEL : x
Mouse : 777 : 56 : LeftButtonDown : 0 : 0 : 0
DELAY : 150
Mouse : 1055 : 48 : LeftButtonUp : 0 : 0 : 0
DELAY : 150
Keyboard : Enter : KeyPress
DELAY : 150
GOTO : x
ELSE
LABEL : y
Mouse : 1055 : 48 : LeftButtonDown : 0 : 0 : 0
DELAY : 150
Mouse : 771 : 48 : LeftButtonUp : 0 : 0 : 0
DELAY : 150
Keyboard : Enter : KeyPress
DELAY : 150
GOTO : y
ENDIF
