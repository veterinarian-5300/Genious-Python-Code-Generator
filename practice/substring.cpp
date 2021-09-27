#include<bits/stdc++.h>
#include<fstream>

using namespace std;

int countChange(string ss) {
    int count = 0;
    stack<char>st;
    for (int i = 0; i < ss.length(); i++) {
        if (st.size() == 0) {
            st.push(ss[i]);
        } else if ((st.top() == 'X' && ss[i] == 'O') || (st.top() == 'O' && ss[i] == 'X')) {
            count++;
            st.push(ss[i]);
        } else if (ss[i] == 'F') {
            continue;
        } else {
            st.push(ss[i]);
        }
    }
    return count;
}

int ssFind(string s, int n) {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= n - i; j++) {
            ans += countChange(s.substr(i, j));
        }
    }
    return ans % 1000000007;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;//8000000
        cin >> n;
        string s;
        cin >> s;
        if (s.length() != n) {
            return -1;
        }
        cout << "Case #" << i << ": " << ssFind(s, n) << endl;
    }
    return 0;
}