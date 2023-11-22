#include <iostream>

using std::cout;
using std::endl;

int main(int argc, char const* argv[]) {
  int squares_sum, sum, sum_squared;
  int number_of_terms = 100;
  sum_squared = number_of_terms * (number_of_terms + 1) / 2;
  sum_squared = sum_squared * sum_squared;
  squares_sum =
      number_of_terms * (2 * number_of_terms + 1) * (number_of_terms + 1) / 6;
  sum = sum_squared - squares_sum;
  cout << sum << endl;
  return 0;
}
