class Bank {
    vector<long long> balance;
public:
    Bank(vector<long long>& balance) : balance(balance) {}
    
    bool transfer(int account1, int account2, long long money) {
        if(account1 <= balance.size() && account1 >= 1 && account2 <= balance.size() && account2 >= 1) {
            if(balance[account1 - 1] < money) {
                return false;
            }
            else {
                balance[account1 - 1] -= money;
                balance[account2 - 1] += money;
                return true;
            }
        }
        else {
            return false;
        }
    }
    
    bool deposit(int account, long long money) {
        if(account <= balance.size() && account >= 1) {
            balance[account - 1] += money;
            return true;
        }
        else {
            return false;
        }
        return false;
    }
    
    bool withdraw(int account, long long money) {
        if(account <= balance.size() && account >= 1) {
            if(balance[account - 1] < money) {
                return false;
            }
            else {
                balance[account - 1] -= money;
                return true;
            }
        }
        else {
            return false;
        }
    }
};

// balance is balance[account1 + 1]

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
