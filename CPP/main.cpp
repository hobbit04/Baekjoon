//백준 문제 풀이를 위한 파일.

#include <iostream>
#include <string>
#include <stack>
using namespace std;

const int Max_digit = 100;

bool has_666(int n){

}

int main() {
    int cnt = 0;
    int num;
    int i = 665;
    cin >> num;

    while(true){
        if(has_666(i)){
            cnt++;
        }
        if(cnt == num){
            break;
        }
        i++;
    }
    return 0;
}

