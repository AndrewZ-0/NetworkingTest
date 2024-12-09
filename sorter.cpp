#include <iostream>
#include <string>


void bubbleSort(int* vals, int len) {
    bool swapped;
    int temp;

    for (size_t i = 0; i < len - 1; i++) {
        swapped = false;
        for (size_t j = 0; j < len - i - 1; j++) {
            if (vals[j] > vals[j + 1]) {
                temp = vals[j];
                vals[j] = vals[j + 1];
                vals[j + 1] = temp;

                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

std::string joinArr(int* vals, int len) {
    std::string vals_str;

    for (size_t i = 0; i < len - 1; i++) {
        vals_str += std::to_string(vals[i]);
        vals_str += ',';
    }

    vals_str += std::to_string(vals[len - 1]);

    return vals_str;
}

int main() {
    int inp_len;

    while (true) {
        std::cin >> inp_len;

        int vals[inp_len];

        for (size_t i = 0; i < inp_len; i++) {
            std::cin >> vals[i];
        }

        bubbleSort(vals, inp_len);

        std::cout << joinArr(vals, inp_len) << '\n';   
    }

    return 0;
}
