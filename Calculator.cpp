#include <iostream>
using namespace std;
int main(){
    float a,b;
    cout<<"Enter two numbers: "<<endl;
    cin>>a>>b;
    char op;
    cout <<"Enter an operator: "<<endl;;
    cin>>op;

    switch (op)
    {
    case '+':
    cout<< a+b;
        break;
    case '-':
    cout<< a-b;
        break;
    case '*':
    cout<< a*b;
        break;
    case '/':
    cout<< a/b;
        break;   
    default:
        break;
    }
}