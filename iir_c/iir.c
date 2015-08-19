/* ==================================================================== 
 * Title:     iir.c                                                  
 *                                                                      
 * Purpose:                                                             
 *            Implement a Fixed-Point filter.                          
 *                                                                      
 * Comments:                                                            
 *                                                                      
 * Structure type:     FIR Direct Form
 * 
 * Fixed-Point Models:
 *
 * CoefficientB Quantizer:
 *           Word Length:  16
 *   Integer Word Length:  -7
 *         Overflow Mode:  Saturation
 *        Round-off Mode:  Nearest
 * 
 * Input Quantizer:
 *           Word Length:  16
 *   Integer Word Length:  1
 *         Overflow Mode:  Saturation
 *        Round-off Mode:  Nearest
 * 
 * Output Quantizer:
 *           Word Length:  16
 *   Integer Word Length:  -3
 *         Overflow Mode:  Wrap
 *        Round-off Mode:  Truncation
 * 
 * Multiplicand Quantizer:
 *           Word Length:  16
 *   Integer Word Length:  1
 *         Overflow Mode:  Wrap
 *        Round-off Mode:  Truncation
 * 
 * Product Quantizer:
 *           Word Length:  32
 *   Integer Word Length:  -3
 *         Overflow Mode:  Wrap
 *        Round-off Mode:  Truncation
 * 
 * Sum Quantizer:
 *           Word Length:  32
 *   Integer Word Length:  -3
 *         Overflow Mode:  Wrap
 *        Round-off Mode:  Truncation
 * 
 * Delay Quantizer:
 *           Word Length:  16
 *   Integer Word Length:  1
 *         Overflow Mode:  Wrap
 *        Round-off Mode:  Truncation
 * 
 *                                                           
 * Copyright 2008 National Instruments Corporation. All rights reserved.       
 * ==================================================================== 
 */

#include "iir.h"


/* ---- Constants ----*/
#define IIR_N_TAPS 33
#define IIR_N_STATES IIR_N_TAPS

/* ---- Global Variables Declaration ----*/
static I16 iir_Coef[IIR_N_TAPS];
static I32 iir_Mult(I16 x, I16 coef);


/* ---- SHFT Define ---- */
#define SUM2OUT 16                      /* SUM2OUT RightShift 16 */


/* ---- Create State of iir ---- */ 
iir_State iir_CreateState ( )
{
	iir_State state = NULL;
	
	state = (iir_State)malloc(sizeof(I16) * IIR_N_STATES);
	
	return state;
}

/* ---- Dispose State of iir ---- */
void iir_DisposeState (iir_State state)
{
	free(state);
	
	return;
}

/* ---- Initialize the State of iir ---- */
void iir_InitState(iir_State state)
{
	int i;
	
	for (i=0; i < IIR_N_STATES; i++)
		state[i] = 0;
	
	return;
}


/* ---- Implement the Fixed-Point Filter ---- */ 
I16 iir_Filtering (I16 sampleIn, iir_State state)
{
	I32 accA;
	int i;

	/* Update the internal states */
	state[0] = sampleIn;

	/* Filtering */
	accA = 0;
	for (i=IIR_N_TAPS-1; i >= 0; i--)
	{
		accA += iir_Mult(state[i], iir_Coef[i]);
		state[i] = (i==0) ? 0 : state[i-1];
	}

	accA = (accA >> SUM2OUT);

	return (I16)accA;
}

/* ---- Internal Functions ---- */
/* ==================================================================== 
 *  Fixed-Point Multiplication:
 *              x     *   coef    =>   prod
 *           Q1.15   *  Q-7.23   =>  Q-3.35
 * ==================================================================== 
 */

static I32 iir_Mult(I16 x, I16 coef)
{
	I32 prod;
	
	prod = ((I32)x * coef) >> 3;

	return prod;
}



/* ---- Filter Coefficients ---- */
static I16 iir_Coef[] = {
	2154,
	1887,
	2664,
	3586,
	4645,
	5825,
	7103,
	8447,
	9821,
	11182,
	12486,
	13685,
	14738,
	15603,
	16246,
	16643,
	16777,
	16643,
	16246,
	15603,
	14738,
	13685,
	12486,
	11182,
	9821,
	8447,
	7103,
	5825,
	4645,
	3586,
	2664,
	1887,
	2154
};
