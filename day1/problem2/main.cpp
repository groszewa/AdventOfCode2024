#include <fstream>
#include <vector>
#include <unordered_map>

#include <iostream>

using namespace std;

int main() {
    ifstream infile("input.txt");
    vector<int> left_vec;
    unordered_map<int, int> right_histogram;
    int left, right;
    while(infile >> left >> right) {
        left_vec.push_back(left);
        right_histogram[right]++;
    }
    unsigned int similarity_score = 0;
    for (auto left_item : left_vec) {
        int freq_in_right = right_histogram.count(left_item)>0 ? right_histogram[left_item] : 0;
        similarity_score += left_item * freq_in_right;
    }
    cout << "Similarity score is " << similarity_score << endl;
    return 0;
}
