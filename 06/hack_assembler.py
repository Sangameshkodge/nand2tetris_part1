#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:04:54 2020

@author: skodge
"""
import argparse
parser = argparse.ArgumentParser(description='Hack Computer Assembler', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--file',           default='pong/Pong.asm',  type=str,     help='File name to be assembled')

global args
args = parser.parse_args()


dest={
      'null':'000',
      'M'   :'001',
      'D'   :'010',
      'MD'  :'011',
      'A'   :'100',
      'AM'  :'101',
      'AD'  :'110',
      'AMD' :'111',
      }

jump={
      'null'    : '000',
      'JGT'     : '001',
      'JEQ'     : '010',
      'JGE'     : '011',
      'JLT'     : '100',
      'JNE'     : '101',
      'JLE'     : '110',
      'JMP'     : '111'
      }

comp={
      '0'   : '0101010',
      '1'   : '0111111',
      '-1'  : '0111010',
      'D'   : '0001100',
      'A'   : '0110000',
      'M'   : '1110000',
      '!D'  : '0001101',
      '!A'  : '0110001',
      '!M'  : '1110001',
      '-D'  : '0001111',
      '-A'  : '0110011',
      '-M'  : '1110011',
      'D+1' : '0011111',
      'A+1' : '0110111',
      'M+1' : '1110111',
      'D-1' : '0001110',
      'A-1' : '0110010',
      'M-1' : '1110010',
      'D+A' : '0000010',
      'D+M' : '1000010',
      'D-A' : '0010011',
      'D-M' : '1010011',
      'A-D' : '0000111',
      'M-D' : '1000111',
      'D&A' : '0000000',
      'D&M' : '1000000',
      'D|A' : '0010101',
      'D|M' : '1010101', 
      }


symbol_table={
        'R0'    : '000000000000000',
        'R1'    : '000000000000001',
        'R2'    : '000000000000010',
        'R3'    : '000000000000011',
        'R4'    : '000000000000100',
        'R5'    : '000000000000101',
        'R6'    : '000000000000110',
        'R7'    : '000000000000111',
        'R8'    : '000000000001000',
        'R9'    : '000000000001001',
        'R10'   : '000000000001010',
        'R11'   : '000000000001011',
        'R12'   : '000000000001100',
        'R13'   : '000000000001101',
        'R14'   : '000000000001110',
        'R15'   : '000000000001111',
        'SP'    : '000000000000000',
        'LCL'   : '000000000000001',
        'ARG'   : '000000000000010',
        'THIS'  : '000000000000011',
        'THAT'  : '000000000000100',
        'SCREEN': '100000000000000',
        'KBD'   : '110000000000000'
        
        }
## Open File
F=open(args.file,'r')
## Load all the files 
symbolic_code=F.readlines()


line_counter=0


for line in symbolic_code:
    line=line.split('//')[0]
    line=line.strip()
    
    if (line==''):
        continue
    if (line[0]=='(' and line[-1]==')'):
        
        symbol_table[line[1:-1]]=''
        for i in range( 15- len(bin(line_counter)[2:]) ):
            symbol_table[line[1:-1]]+='0'
        symbol_table[line[1:-1]]+=bin(line_counter)[2:]
    
    else:
        line_counter+=1
    
temp_reg=16
for line in symbolic_code:
    line=line.split('//')[0]
    line=line.strip()
    
    if (line==''or (line[0]=='('and line[-1]==")")):
        continue
    if(line[0]=='@'):
        if (line[1:].isnumeric()):
            instruction='0'
            for i in range( 15- len(bin(int(line[1:]))[2:]) ):
                instruction+='0'
            instruction+=bin(int(line[1:]))[2:]
              
        else:
            if line[1:] not in symbol_table.keys():
                symbol_table[line[1:]]=''
                for i in range( 15- len(bin(temp_reg)[2:]) ):
                    symbol_table[line[1:]]+='0'
                symbol_table[line[1:]]+=bin(temp_reg)[2:]
                temp_reg+=1
                
            instruction='0'+symbol_table[line[1:]]
        print(instruction)
        
    else:
        instruction='111'
        line = line.split(';')
        
        if len(line)==1:
            inst_jump='null'
        else:
            inst_jump=line[1].strip()
        line=line[0].strip()
                
        line = line.split('=')
        if len(line)==1:
            inst_dest='null'
            inst_comp=line[0].strip()
        else:
            inst_dest=line[0].strip()
            inst_comp=line[1].strip()
        instruction+=comp[inst_comp]+dest[inst_dest]+jump[inst_jump]
        print(instruction)
    