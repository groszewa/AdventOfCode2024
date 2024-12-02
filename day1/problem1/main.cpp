#include <fstream>
#include <queue>
#include <vector>

#include <iostream>

using namespace std;

int main() {
    ifstream infile("input.txt");
    priority_queue<int, vector<int>, greater<int>> minHeapLeft, minHeapRight;
    int left, right;
    while(infile >> left >> right) {
        minHeapLeft.push(left);
        minHeapRight.push(right);
    }
    unsigned int total_distance = 0;
    while(!minHeapLeft.empty()) {
        total_distance += abs(minHeapLeft.top() - minHeapRight.top());
        minHeapLeft.pop();
        minHeapRight.pop();
    }
    cout << "Total distance is " << total_distance << endl;
    return 0;
}
