data segment
array db 3,9,7,8,1,0
min db ?
max db ?
data ends

code segment
assume cs:code, ds:data        
start:
mov ax,data
mov ds,ax
               
LEA SI,array
mov al,[SI]

mov min,al
mov max,al
mov cl,05

up: inc SI
mov al,[SI]
cmp min,al
JC lmax
mov min,al
lmax:
cmp max,al
JNC label1
mov max,al
label1: dec cl
JNZ up

mov bl,min
call convert

mov bl,max
call convert

mov ah,4ch
int 21h


convert proc
                mov al,bl
                and al,0F0h
                ror al,04h
                cmp al,0Ah
jc l1
                add al,37h
jmp l2
                l1: add al, 30h
                l2: mov dl,al
                mov ah,02h
                int 21h

mov al,bl
                and al,0Fh
                cmp al,0Ah
                jc l3
                add al,37h
                jmp l4
                l3: add al, 30h
                l4: mov dl,al
                mov ah,02h
                int 21h
                ret                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
endp

code ends
end start
