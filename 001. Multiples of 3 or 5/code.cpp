#include <iostream>

using std::cin;
using std::cout;
using std::endl;

long long int SumOf2IntegersMultiplies(int number1,
                                       int number2,
                                       int upper_limit) {
  long long int sum = 0;
  for (int i = number1; i < upper_limit; i += number1)
    sum += i;
  for (int i = number2; i < upper_limit; i += number2) {
    if (i % number1 == 0)
      continue;
    sum += i;
  }
  return sum;
}

int main(int argc, char const* argv[]) {
  int a, b, c;
  cout << "Please input the first number: ";
  cin >> a;
  cout << "Please input the second number: ";
  cin >> b;
  cout << "Please input the upper limit: ";
  cin >> c;
  long long int sum = SumOf2IntegersMultiplies(a, b, c);
  cout << "The sum of " << a << " and " << b << " multiplies less than " << c
       << " is " << sum << "." << endl;
  return 0;
}
