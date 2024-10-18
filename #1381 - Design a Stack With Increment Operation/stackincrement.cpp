class CustomStack {
public:

    int topIndex;
    int size;
    int maximum;
    int* stack;
    int* addednums;

    CustomStack(int maxSize) {
        stack = new int[maxSize];
        addednums = new int[maxSize];
        maximum = maxSize;
        size = 0;
        topIndex = -1;
    }
    
    void push(int x) {
        if (size >= maximum) {
            cout << "Stack overflow error." << endl;
            return;
        }
        else {
            topIndex++;
            stack[topIndex] = x;
            addednums[topIndex] = 0;
            size++;
        }
    }
    
    int pop() {
       if (topIndex == -1) {
        cout << "Stack underflow error." << endl;
        return -1;
       } 
       else {
        int popped = stack[topIndex] + addednums[topIndex];
        if (topIndex > 0) {
            addednums[topIndex - 1] += addednums[topIndex];
        }
        addednums[topIndex] = 0;
        topIndex--;
        size--;
        return popped;
       }
    }
    
void increment(int k, int val) {
    if (k <= 0) {
        return; 
    }
    if (size == 0) {
        return; 
    }
    if (k > size) {
        addednums[size - 1] += val;  
    } else {
        addednums[k - 1] += val;  
    }
}

};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
