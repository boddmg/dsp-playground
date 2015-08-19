/* ==================================================================== 
 * Title:     iir.h                                                  
 *                                                                      
 * Purpose:                                                             
 *            Present typedefs, global variables declaration and       
 * function prototypes.                                                 
 *                                                                      
 * Copyright 2008 National Instruments Corporation. All rights reserved.       
 * ==================================================================== 
 */

#ifndef __iir_DIRECT_FIR_H__
#define __iir_DIRECT_FIR_H__

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "nidfdtyp.h"

#ifdef __cplusplus
extern "C"{
#endif

/* ----Typedef---- */
typedef I16* iir_State;

/* ----Create/Dispose State---- */
iir_State iir_CreateState ( );
void iir_DisposeState (iir_State state);

/* ----Initialize State---- */
void iir_InitState (iir_State state);

/* ----Filter Implementation---- */
I16 iir_Filtering (I16 sampleIn, iir_State state);

/* ----Demo Program---- */
/* void main()
 * {
 *     //Declare and create State
 *     iir_State state;
 *     state = iir_CreateState();
 *
 *     ...
 *
 *     //Initialize State
 *     iir_InitState (state);
 *
 *     ...
 *
 *     //Processing
 *     while ()
 *     {
 *         ...
 *         y = iir_Filtering(x, state);
 *         ...
 *     };
 *
 *     ...
 *
 *     //Dispose State
 *     iir_DisposeState (state);
 *
 *     ...
 *
 *     return;
 * }
 */

#ifdef __cplusplus
}
#endif

#endif //#ifndef __iir_DIRECT_FIR_H__
