#include <iostream>
#include <string>
using namespace std;

int main() {
    string nama, kota;
    int umur;
    
    cout << "Nama : ";
    getline(cin, nama);
    cout << "Umur : ";
    cin >> umur;
    cin.ignore(); 
    cout << "Kota : ";
    getline(cin, kota);
    
    cout << nama << ", " << umur << " tahun, dari " << kota << '\n';
    cout << "Tahun depan umur " << umur + 1 << '\n';
}