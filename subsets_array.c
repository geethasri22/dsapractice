#Question 3 : Subset of Arrays
'''
Input : 

A[]  = { 1, 34, 16, 1, 4, 3, 18, 19 };
B[]  = {  1, 4, 3 };

Output : 
3 4 5

Solution : 
'''
// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    printf("Subset arrays : ");
    
    int    a[]  = { 1, 1, 1, 1, 4, 3, 18, 19 };
    int b[]  = {  1, 1, 1, 1 };
    
    int len_a = sizeof(a)/sizeof(a[0]);
    int len_b = sizeof(b)/sizeof(b[0]);
    
    for(int i=0; i<len_a - len_b;  i++){
      int flag = 1;
      for(int j=0; j<len_b; j++){
          if( a[ i+j ] != b[j]){
              flag = 0;
              break;
          }
      }
      
      if(flag){
         for(int k=0; k<len_b; k++){
             printf(" %d ", i+k);
         } 
         printf("\n");
      }
    }
    
    


    return 0;
}
