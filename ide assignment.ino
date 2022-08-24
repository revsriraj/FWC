#include <Arduino.h>
int Z=1,Y=0,X=0;
int D,C,B,A;
int G,S,L,H;

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int D, int C, int B, int A) 
{
  digitalWrite(2, A); //LSB
}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  
}
void loop() {
 G=!(X&&Y);
 S=!(G&&!Y);
 L=!(S&&Y);
 H=!(S||!Z);
 A=!(H||L);
disp_7447(D,C,B,A);  
}

