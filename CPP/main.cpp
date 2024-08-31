//백준 문제 풀이를 위한 파일.
// 7662번
// 사용할 자료구조 : 이진트리 (not AVL)
// 구현방법 : 구조체와 포인터

#include <iostream>

struct Node{
    int value;
    Node* left;  // Smaller value only
    Node* right;  // Larger value only
    explicit Node(int val=0) : value(val), left(nullptr), right(nullptr) {}
};


Node* find_min(Node* node){
    if(node->left == nullptr){
        return node;
    }
    return find_min(node->left);
}

Node* find_max(Node* node){
    if(node->right == nullptr){
        return node;
    }
    return find_max(node->right);
}

Node* insertion(int n, Node* node){
    if(!node){
        return new Node(n);
    }
    if(node->value <= n){
        node->left = insertion(n, node->left);
    }
    else{
        node->right = insertion(n, node->right);
    }
    return node;
}

Node* deletion(int n, Node* node, int size){
    if(size == 0){
        return node;
    }
    if(n == 1){  // delete max
        Node* max_node = find_max(node);
        delete max_node;
    }
    else{

    }
}


void print_result(Node* head, int size){
    if(size == 0){
        std::cout << "EMPTY" << std::endl;
    }
    int min = find_min(head)->value;
    int max = find_max(head)->value;
    std::cout << min << " " << max << std::endl;
}

int main() {
    using namespace std;
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int k;  // number of operations
        int size = 0;  // size of Queue
        cin >> k;
        Node* head = new Node;
        for(int j = 0; j < k; j++){
            char op;
            int num;
            cin >> op >> num;
            cout << "op: " << op << " num: " << num;
            if(op == 'I'){
                insertion(num, head);
                size++;
            }
            else if(op == 'D'){
                head = deletion(num, head, size);
                size--;
            }
        }
        print_result(head, size);
    }
}

