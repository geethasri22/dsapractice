#Question - 1 : Bubble Sort

'''Input : 

a [ ] = { 12, 2, 3, 4, 5, 6, 7, 11 }

Output : 

Out [ ] = { 2, 3, 4, 5, 6, 7, 11, 12 }

Solution : 
'''
// Online C compiler to run C program online
/*
int temp=0;
int a=90; int b = 45;

temp = a;
a = b;
b = temp;



*/
#include <stdio.h>

int main() {
    // Write C code here
    int len=0;
    printf("\nEnter length of the array : ");
    
    scanf(" %d ",&len);
    
    int arr[len];
    
    printf("Enter elements in array :  ");
    for(int i=0; i<len; i++){
        scanf(" %d ",&arr[i]);
    }
    
    
printf("\nMy Original elements in array : \n ");
    for(int i=0; i<len; i++){
        printf(" %d ",arr[i]);
    }
int temp = 0;    
   for(int i=0; i<len; i++){
       for(int j=0; j<len; j++){
           if( arr[j] > arr[j+1] ){
               temp = arr[j];
               arr[j] = arr[j+1];
               arr[j+1] = temp;
           }
       }
   }
    
 printf("\nMy elements after sorting in array : \n ");
    for(int i=0; i<len; i++){
        printf(" %d ",arr[i]);
    }   

    return 0;
}
