#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, char const* argv[]) {
  long long int number = 600851475143;
  int largest_factor = 0;
  for (int i = 2; i <= number && number > 1; ++i) {
    largest_factor = (number % i == 0) * i + (number % i > 0) * largest_factor;
    while (number % i == 0) {
      number = number / i;
    }
  }
  cout << "The largest prime divisor of " << number << " is " << largest_factor
       << "." << endl;
  return 0;
}
