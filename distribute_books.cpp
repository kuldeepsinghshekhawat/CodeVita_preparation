#include<iostream>
using namespace std;
long long int fib(long int n)
{
    long long int f[n+1];
    long long int i;
    f[0]=1;
    f[1]=0;
    f[2]=1;

    for(i=3;i<=n;i++){
        f[i]=((i-1)*(f[i-1]+f[i-2]))%100000007;
    }
    return f[n];
}

int main()
{   long long int n;  
    cout<<"Data";
    cin>>n;
    if(n>0 && n<=1000000){
        cout<<fib(n);}
    return 0;
}