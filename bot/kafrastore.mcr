IF MESSAGE : Store mode?
LABEL : x
Mouse : 823 : 61 : LeftButtonDown : 0 : 0 : 0
DELAY : 100
Mouse : 1128 : 57 : LeftButtonUp : 0 : 0 : 0
DELAY : 100
Keyboard : Enter : KeyPress
DELAY : 100
GOTO : x
ELSE
LABEL : y
Mouse : 1128 : 57 : LeftButtonDown : 0 : 0 : 0
DELAY : 100
Mouse : 823 : 61 : LeftButtonUp : 0 : 0 : 0
DELAY : 100
Keyboard : Enter : KeyPress
DELAY : 100
GOTO : y
ENDIF
