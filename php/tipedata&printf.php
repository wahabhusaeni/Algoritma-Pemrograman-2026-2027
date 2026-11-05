<?php
$nim = "I.2220222";
$nama = "Muhamad Wahab Husaeni";
$umur = 20;
$nilai = 99.99;
$status = true;

echo "NIM : $nim\n";
echo "Nama : $nama\n";
echo "Umur : $umur\n";
printf("Nilai : %.3f\n", $nilai);
echo "Status : " . ($status ? "Aktif" : "Tidak Aktif");