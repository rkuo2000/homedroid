//
// UART0_RX : UART0 RX recieve and display Text
//
// Board       : Nu-LB-NUC140
// MCU         : NUC140VE3CN (LQFP100)
// UART0       : baudrate=115200, databit=8, stopbit=1, paritybit=0, flowcontrol=None

#include <stdio.h>
#include <math.h>
#include <string.h>
#include "NUC100Series.h"
#include "MCU_init.h"
#include "SYS_init.h"
#include "LCD.h"

// Global Variables 
char     InText[8];
char     Text[16];
uint8_t  comRbuf[256];
volatile uint8_t comRbytes = 0;
volatile uint8_t RX_Flag =0;

void UART02_IRQHandler(void)
{
	uint8_t c, i;
	uint32_t u32IntSts = UART0->ISR;
	
	if(u32IntSts & UART_IS_RX_READY(UART0)) // check ISR on & RX is ready
  {
		while (!(UART0->FSR & UART_FSR_RX_EMPTY_Msk)){ // check RX is not empty
			UART_Read(UART0, InText, 8); // read UART RX data
		  RX_Flag=1;	                 // set flag when BT command input
		}		
	}
}

void Init_UART0(void)
{ 
  UART_Open(UART0, 9600);                     // set UART0 baud rate
  UART_ENABLE_INT(UART0, UART_IER_RDA_IEN_Msk); // enable UART0 interrupt (triggerred by Read-Data-Available)
  NVIC_EnableIRQ(UART02_IRQn);		              // enable Cortex-M0 NVIC interrupt for UART02
}


int32_t main()
{
	uint8_t i =0;
	char sensor_data[9];
	SYS_Init();   // initialize MCU
  init_LCD();   // initialize LCD
  clear_LCD();  // clear LCD screen	
	print_Line(0, "UART-to-Comport");
	
	Init_UART0(); // initialize UART1 for Bluetooth

	sprintf(sensor_data, "data= 00\n");
	
  while(1){
    if (RX_Flag==1) {
			sprintf(Text, InText);
			print_Line(2, Text);
			RX_Flag=0;
		}
		
		sensor_data[7] = 0x30+i;
		UART_Write(UART0, sensor_data, 9);		
		i++;
		if (i>9) i=0;
	}
}
