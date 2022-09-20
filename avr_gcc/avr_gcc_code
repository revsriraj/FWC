#include<avr/io.h>
#include<stdbool.h>
int main(void){

bool x,y,z,g,h,s,l,a;
DDRB = 0b00000111; //8&9 as inputs
PORTB= 0b11111000;
DDRD = 0b00000100; //2as output

//DDRB |= (1<<DDB5);


while(1)
   {
	   x = (PINB & (1<<PINB0)) == (1<<PINB0);	
	   y = (PINB & (1<<PINB1)) == (1<<PINB1);
	   z = (PINB & (1<<PINB2)) == (1<<PINB2);
	   g=!(x&&y);
	   s=!(g&&!y);
	   l=!(s&&y);
	   h=!(s||!z);
	   a=!(h||l) ;
	   PORTD |= (a<<2);

   }

	return 0;
}
