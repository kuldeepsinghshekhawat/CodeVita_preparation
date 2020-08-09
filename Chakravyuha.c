# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:00:49 2020

@author: Kuldeep Singh 
This is 2D array problem

"""

#include<stdio.h>

int isDiv(int);

int main(){

    int n;
    scanf("%d",&n);

    //check contraint
    if(n<=0 || n>100){
        return 0;
    }

    int a[100][100]; // main matrix

    int counter=1; // keeps track of number

    int i,j; //keeps track of position

    int w;   // w - window 

    int size=n-1; // size - size of segment of window

    for( w = 0 ; w < n / 2 ; w++){
        i = w;
        j = w;

        //go right
        for( j = j ; j < size + w ; j++){
            a[ i ][ j ] = counter;
            counter++;
        }

        //go down
        for( i = i ; i < size + w ; i++){
            a[ i ][ j ] = counter;
            counter++;
        }

        //go left
        for( j = j ; j > w ; j--){
            a[ i ][ j ] = counter;
            counter++;
        }

        //go up
        for( i = i ; i > w ; i--){
            a[ i ][ j ] = counter;
            counter++;
        }
        size = size-2;
    }
    if( n % 2 != 0){
        a[ w ][ w ] = counter;      
    }

    //print matrix
    for( i = 0 ; i < n ; i++){
        for( j = 0 ; j < n ; j++){
            printf("%d\t", a[ i ][ j ]);
        }
        printf("\n");
    }

    int no_div = (n*n)/11 + 1 ; // no of divisibles

    printf("Total Power points : %d\n",no_div);

    printf("(0,0)\n");

    size=n-1;

    //print positions
    for( w = 0 ; w < n / 2 ; w++){
        i = w;
        j = w;

        //go right
        for( j = j ; j < size + w ; j++){
            if(isDiv( a[ i ][ j ] )){
                printf("(%d,%d)\n", i, j);
            }
        }

        //go down
        for( i = i ; i < size + w ; i++){
            if(isDiv( a[ i ][ j ] )){
                printf("(%d,%d)\n", i, j);
            }
        }

        //go left
        for( j = j ; j > w ; j--){
            if(isDiv( a[ i ][ j ] )){
                printf("(%d,%d)\n", i, j);
            }
        }

        //go up
        for( i = i ; i > w ; i--){
            if(isDiv( a[ i ][ j ] )){
                printf("(%d,%d)\n", i, j);
            }
        }
        size = size-2;
    }
    if( n % 2 != 0){
        if(isDiv( a[ i ][ j ] )){
            printf("(%d,%d)\n", i, j);
        }       
    }

    return 0;
}

int isDiv(int x){
    if( x % 11 == 0 ){
        return 1;
    }
    else{
        return 0;
    }
}