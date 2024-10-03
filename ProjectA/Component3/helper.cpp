#include "helper.h"

#include <iostream>

int doSomething(int a, int b) {
  std::cout << "I did something using " << a << " and " << b << std::endl;
  return a+b;
}
