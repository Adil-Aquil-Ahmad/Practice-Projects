#include <iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    int i;
    for(i = 2;i<a;i++){
        if(a%i==0){
            cout<<"it is a composite no.";
            break;
        }
        else {
            continue;
        }

    }
    if(i==a){
        cout<<"a is a prime no.";
    }
    return 0;
}