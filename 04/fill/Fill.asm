// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
 ///Assumption R0 contains 8192 (Max adress)
@Fill
M=0
@0
D=M
@n
M=D
(Poll)
	@KBD
	D=M		//D=KEYBOARD
	@Pressed	
	D;JGT		//goto Pressed if KEYBOARD>0
	@Fill		
	D=M		//D=Fill
	@Poll
	D;JEQ		//goto Poll if Fill=0

	//Fill=-1 and KEYBOARD=0
	@Fill
	M=0
	@Screen_fill
	0;JMP

	(Pressed)
		@Fill
		D=M+1		//D=Fill+1
		@Poll
		D;JEQ		//goto Poll if Fill=-1

		//Fill=0 and KEYBOARD>0
		@Fill
		M=-1
		@Screen_fill
		0;JMP

(Screen_fill)
	
	@i 
	M=0		//i=0
	@SCREEN
	D=A
	@addr
	M=D		//addr=Screen address

	(LOOP)
		@i
		D=M
		@n
		D=D-M
		@Poll
		D;JEQ	//if i==n goto Poll

		@Fill
		D=M
		
		@addr
		A=M
		M=D	//M[addr]=Fill
		
		@addr
		M=M+1	//addr=addr+1
		@i
		M=M+1	//i=i+1
		@LOOP
		0;JMP	//Continue loop
	
	




