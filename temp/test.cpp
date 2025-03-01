#include <iostream>
#include <vector>


class Test {
public:
    std::string name;
};

int main() {
    Test x;
    x.name = "hi";
    int z = 10;

    std::cout << z << std::endl;

    z++;

    std::cout << z << std::endl;

    ++z;

    std::cout << z << std::endl;

    int* p = new int(10);

    std::vector<int> v = {1, 2, 3, 4, 5};


    std::cout << "Hello, World!" << std::endl;

    return 0;
}