class ProductOfNumbers {
public:
    std::vector<int> mults;

    //Since we start with inserting a 1, we treat everything as if it is 1 indexed
    int oneindexedsize = 0;
    ProductOfNumbers() {
        mults.push_back(1);
    }
    
    void add(int num) {
        if(num == 0) {
            mults = {1};
            oneindexedsize = 0;
        }
        else {
            mults.push_back(mults[oneindexedsize] * num);
            oneindexedsize += 1;
        }
    }
    
    int getProduct(int k) {
        if(k > oneindexedsize) {
            return 0;
        }
        
        //Interesting math concept with how prefix sums work. If you start with 1 and always calculate
        //The tail element * new element and append, the following formula will always work for retrieving
        //The multiplicative prefix of any stream of numbers...
        return mults[oneindexedsize] / mults[oneindexedsize - k];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
