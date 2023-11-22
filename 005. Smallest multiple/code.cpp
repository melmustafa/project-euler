#include <iostream>

using std::cout;
using std::endl;

int GreatestCommonDivisor(int number1, int number2) {
  if (number2 == 0)
    return number1;
  return GreatestCommonDivisor(number2, number1 % number2);
}

int main(int argc, char const* argv[]) {
  int factor = 20;
  for (int i = 1; i < 20; ++i) {
    factor = factor * i / GreatestCommonDivisor(factor, i);
  }
  cout << "The smallest number that is divisible by all the numbers between 1 "
          "and 20 is "
       << factor << "." << endl;
  return 0;
}
