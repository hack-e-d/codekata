#include <iostream>

using namespace std;

int main(){
    int a,b,c[10],s=0;
    cin>>a>>b;
    for(int i=0;i<a;i++){
        cin>>c[i];
    }
    for(int i=0;i<b;i++){
        s+=c[i];
    }
    cout<<s;
}