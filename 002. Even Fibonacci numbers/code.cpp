#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const* argv[]) {
  int number_of_terms = 100;
  int upper_limit = 4000000;
  long long int fibonacci[number_of_terms];
  long long int sum = 0;
  fibonacci[0] = 0;
  fibonacci[1] = 1;
  for (int i = 2; fibonacci[i - 1] < upper_limit && i < number_of_terms; ++i) {
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    if (fibonacci[i] % 2 == 0)
      sum += fibonacci[i];
  }
  cout << sum;
  return 0;
}
