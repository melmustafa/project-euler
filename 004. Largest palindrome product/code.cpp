#include <iostream>

using std::cout;
using std::endl;
using std::max;
using std::string;

bool IsPalindrome(long long int number) {
  string number_string = std::to_string(number);
  return number_string == string(number_string.rbegin(), number_string.rend());
}

int main(int argc, char const* argv[]) {
  int palindrome = 0;
  for (int i = 999; i > 100 && i * 999 > palindrome; --i) {
    int loop_palindrome = 0;
    bool stop = false;
    for (int j = 999; j >= i && !stop; --j) {
      loop_palindrome = i * j;
      stop = IsPalindrome(loop_palindrome);
    }
    palindrome = max(palindrome, loop_palindrome * stop);
  }
  cout << "The largest palindromic multiply of two 3 digits number is "
       << palindrome << "." << endl;
  return 0;
}
