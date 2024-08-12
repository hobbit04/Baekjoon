#include "iostream"
#include "string"

int main()
{
    std::string ans;
    bool flag = true;
    while(flag){
        while(true){
            char stack[100];
            int len = 0;
            int c;
            scanf("%c",&c);
            if(c == '\0'){
                flag = false;
                break;
            }
            if(c == '.'){
                ans += "yes";
                break;
            }
            else if(c == '('){
                stack[len] = '(';
                len++;
            }
            else if(c == '['){
                stack[len] = '[';
                len++;
            }
            else if(c == ')'){
                if(stack[len] != '('){
                    ans += "no";
                    break;
                }
            }
            else if(c == ']'){
                if(stack[len] != '['){
                    ans += "no";
                    break;
                }
            }
        }
    }
    
    std::cout << ans;    
}