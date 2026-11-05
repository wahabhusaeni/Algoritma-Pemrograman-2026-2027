#include <iostream>
#include <string>
using namespace std;

int main() {
    string nm1, nm2;

    cout << "Masukkan nama pertama = ";
    getline(cin, nm1);                 
    cout << "Masukkan nama kedua = ";
    cin >> nm2;                         

    cout << "Selamat Datang " << nm1 << '\n';
    cout << "Selamat Datang " << nm2 << '\n';
}