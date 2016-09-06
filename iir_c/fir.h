/* ==================================================================== 
 * Title:     fir.h                                                  
 *                                                                      
 * Purpose:                                                             
 *            Present typedefs, global variables declaration and       
 * function prototypes.                                                 
 *                                                                      
 * Copyright 2008 National Instruments Corporation. All rights reserved.       
 * ==================================================================== 
 */

#ifndef __fir_DIRECT_FIR_H__
#define __fir_DIRECT_FIR_H__

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "nidfdtyp.h"

#ifdef __cplusplus
extern "C"{
#endif

/* ----Typedef---- */
typedef I16* fir_State;

/* ----Create/Dispose State---- */
fir_State fir_CreateState ( );
void fir_DisposeState (fir_State state);

/* ----Initialize State---- */
void fir_InitState (fir_State state);

/* ----Filter Implementation---- */
I16 fir_Filtering (I16 sampleIn, fir_State state);

/* ----Demo Program---- */
/* void main()
 * {
 *     //Declare and create State
 *     fir_State state;
 *     state = fir_CreateState();
 *
 *     ...
 *
 *     //Initialize State
 *     fir_InitState (state);
 *
 *     ...
 *
 *     //Processing
 *     while ()
 *     {
 *         ...
 *         y = fir_Filtering(x, state);
 *         ...
 *     };
 *
 *     ...
 *
 *     //Dispose State
 *     fir_DisposeState (state);
 *
 *     ...
 *
 *     return;
 * }
 */

#ifdef __cplusplus
}
#endif

#endif //#ifndef __fir_DIRECT_FIR_H__
