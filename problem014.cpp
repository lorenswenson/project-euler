// The following iterative sequence is defined for the set of positive integers:

// n → n/2 (n is even)
// n → 3n + 1 (n is odd)

// Using the rule above and starting with 13, we generate the following sequence:
// 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

// It can be seen that this sequence (starting at 13 and finishing at 1) contains
// 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
// that all starting numbers finish at 1.

// Which starting number, under one million, produces the longest chain?

// NOTE: Once the chain starts the terms are allowed to go above one million.

#include <iostream>
#include <iterator>
#include <algorithm>

#include <vector>
#include <unordered_map>

#include <time>

using namespace std;

inline long get_next_colatz (const long n) {
  if (n <= 0) cout << "Error: " << n << endl;
  if (n % 2 == 0){
    return n / 2;
  }
  else {
    return 3*n + 1;
  }
}

long find_chain_length (const long n) {
  static unordered_map<signed long, signed long> memo;
  // cout << n << endl;
  if (n <= 1) return 1;
  if (memo.count(n) > 0) return memo[n];
  // else
  long ret = find_chain_length(get_next_colatz(n)) + 1;
  memo[n] = ret;
  return ret;
}

int main()
{
  long max_chain_length = 0;
  long chain_seed = 0;  // number that generated max_chain_length
  long current_length;
  for (long n = 1; n<1000000; n++) {
    current_length = find_chain_length(n);
    // cout << "" << endl;
    // cout << n << endl;
    // cout << current_length << endl;
    if (current_length >= max_chain_length) {
        max_chain_length = current_length;
        chain_seed = n;
    }
  }

  cout << "Chain seed: " << chain_seed << endl;
  cout << "Longest Chain: " << max_chain_length << endl;
  return 0;  
}
