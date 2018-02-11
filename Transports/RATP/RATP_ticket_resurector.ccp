// RATP ticket resurector (proto)
// CC 2012 furrtek - furrtek.org
// ATTiny25 8MHz AVRStudio 4
// PB0:LED, PB3:Head, PB4:Switch
    
#include <avr/io.h>
#include <util/delay.h>
// F2F bit write
void writebit(uint8_t bit) {
    if (bit) {
    	PORTB ^= _BV(PB3);
    	_delay_us(800);
    	PORTB ^= _BV(PB3);
    	_delay_us(800);
    } else {
    	PORTB ^= _BV(PB3);
    	_delay_us(1600);
    }
}
    
int main(void) {
	const uint8_t databits[69] = {};	// Only you know the magic code ;)
	uint8_t bits;
    
	WDTCR = (1<<WDCE) | (1<<WDE);
	WDTCR = 0x00;
    
	PORTB = _BV(PB4);;
	DDRB = 0b11101111;	// PB4 as an input
    
	for (;;) {
    	// Wait for ticket
    	while(bit_is_set(PINB,PB4)) {};
    	_delay_ms(20);	// time between microswitch close and write start
    	PORTB = _BV(PB0) | _BV(PB4);;
    	// Prelude
    	for (bits=0;bits<10;bits++) {
    		writebit(1);
    	}
    	// Data
    	for (bits=0;bits<69;bits++) {
    		writebit(databits[bits]);
    	}
    	// Prelude
    	for (bits=0;bits<10;bits++) {
    		writebit(1);
    	}
    	PORTB = _BV(PB4);
    }
}
