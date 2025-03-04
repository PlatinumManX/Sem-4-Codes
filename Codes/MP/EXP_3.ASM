DATA SEGMENT
a DB ?
b DB ?
msg DB 0Dh,0Ah,"Enter the 1st No $"
msg1 DB 0Dh,0Ah,"Enter the 2nd No $"
msg2 DB 0Dh,0Ah,"The result of the addition for AHMED ANSARI C11_09 is $"
msg3 DB 0Dh,0Ah,"The result of the subtraction for AHMED ANSARI C11_09 is $"
DATA ENDS

CODE SEGMENT
ASSUME CS:code, DS:data
start:
MOV ax, data
MOV ds, ax

MOV dx, OFFSET msg
MOV ah, 09h
int 21h

CALL input
MOV a, bl

MOV dx, OFFSET msg1
MOV ah, 09h
int 21h

CALL input
MOV b,bl

MOV dx, OFFSET msg2
MOV ah, 09h
int 21h

MOV cl, 00
ADD bl, a
JNC l3
INC cl

l3:
MOV dh, bl
MOV bl, cl
AND bl, 0Fh
CALL convert
MOV dl, bl
MOV ah, 02h
int 21h

MOV bl, dh
AND bl, 0F0h
ROR bl, 04h

CALL convert
MOV dl,bl
MOV ah, 02h
int 21h

MOV bl, dh
AND bl, 0Fh
CALL convert

MOV dl, bl
MOV ah, 02h
int 21h

mov dx, OFFSET msg3
mov ah, 09h
int 21h

mov cl,00
mov bl,a
sub bl,b

JNC l4
INC cl

l4:
MOV dh, bl
MOV bl, cl
AND bl, 0Fh
CALL convert
MOV dl, bl
MOV ah, 02h
int 21h

MOV bl, dh
AND bl, 0F0h
ROR bl, 04h

CALL convert
MOV dl,bl
MOV ah, 02h
int 21h

MOV bl, dh
AND bl, 0Fh
CALL convert

MOV dl, bl
MOV ah, 02h
int 21h

MOV ah, 4ch
int 21h

input proc
MOV ah, 01h
int 21h

CALL ascii2hex
MOV bl, al
ROL bl, 4

MOV ah, 01h
int 21h
CALL ascii2hex
ADD bl, al
RET
ENDP

ascii2hex proc
CMP al, 41h
JC num
SUB al, 07h
num: SUB al, 30h
RET
ENDP

CONVERT proc
CMP bl, 0Ah
JC l1
ADD bl, 37h
JMP l2
l1: ADD bl, 30h
l2: RET
ENDP

CODE ENDS
END start














