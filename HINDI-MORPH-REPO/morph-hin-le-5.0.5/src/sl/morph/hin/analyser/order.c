/**
 * File Name : order.c
 */

/** 
  *Function: order
  *This program gives descrption of category-enumerator-file based on feature-enumerator-file
  */
#include "struct.h"
struct order_info order[11]={
      {
	"v",
	"tam",
	"gender",
	"number",
	"person",
	"v_type",
	"spec",
	"emph",
	"dubi",
	"conj",
	"hon",
	"voice",
	"case",
	"finiteness",
	"suff",
	},
       {
	"vn",
	"gender",
	"number",
	"case",
	"parsarg",
	"tam"
	},
       {
	"n",
	"gender",
	"number",
	"case",
	"parsarg",
	"person",
	"cm",
	"spec",
	"emph",
	"dubi",	
	"interj",
	"conj",
	"hon",
	"arg_gen",
	"agr_num",
	"arg_per",
	"suff",
         },
       {
	"p",
	},
       {
	"adj",
	"gender",
	"number",
	"case",
	"person",
	"degree",
	"like",
	"dubi",
	"interj",
	"emph",
	"conj",	
	"?spec",
	"suff",
	 },
        {
	"P",
	"gender",
	"number",
	"case",
	"person",
	"dubi",
	"interj",
	"emph",
	"conj",
	"?spec",
	"suff",
	  },
         {
	   "Avy",
          },
         {
	"avy",
	  },
/* Added for Sanskrit, avy is better than Avy, Hint: view in devenagari */
/* Afterwords delete Avy category, and also make changes in Ca Ce Fe files of other langauges. */
         {
	   "sh_n",
	   "number",
	   "gender",
           "number1",
           "case",
           "parsarg",
          },
         {
	    "D",
	    "gender",
	    "number",
	    "case",
	    "parsarg",
	    },
          {
	    "sh_P",
	    "gender",
	    "number",
	    "person",
	    "case",
	    "parsarg",
	    "emph",
	    "gen1",
	    "num1",
	    "cas1",
             }
     };
