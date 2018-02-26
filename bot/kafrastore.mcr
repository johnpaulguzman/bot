IF MESSAGE : Store mode?
LABEL : x
Mouse : 834 : 52 : LeftButtonDown : 0 : 0 : 0
DELAY : 100
Mouse : 1055 : 48 : LeftButtonUp : 0 : 0 : 0
DELAY : 100
Keyboard : Enter : KeyPress
DELAY : 100
GOTO : x
ELSE
LABEL : y
Mouse : 1055 : 48 : LeftButtonDown : 0 : 0 : 0
DELAY : 100
Mouse : 834 : 52 : LeftButtonUp : 0 : 0 : 0
DELAY : 100
Keyboard : Enter : KeyPress
DELAY : 100
GOTO : y
ENDIF
