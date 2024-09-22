#include <iostream> 
using namespace std; 
int main(){
    int Dec;
    string Bin;
    cout<<"Enter a Whole Number: ";
    cin>>Dec;
    while (Dec>=1){
        Bin = Bin + to_string(Dec%2);
        if (Dec%2==0){
            Dec = Dec/2;
            }
        else{
            Dec = Dec/2-1/2;
            }
    }
    for (int i = Bin.length();i>=0;i--){
        cout<<Bin[i];
    }
    cout<<endl;
main();
}