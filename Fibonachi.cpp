#include <iostream>
using namespace std;
int main(){
    int n;
    int a = 0;
    int b = 1;
    int sum = b;
    cin>>n;
    cout<<a<<" "<<b<<" ";
    for(int i = 0;i<=n-3;i++){
        cout<<sum<<" ";
        a = b;
        b = sum;
        sum = a + b;
        cout<<endl;
    }

main();
}