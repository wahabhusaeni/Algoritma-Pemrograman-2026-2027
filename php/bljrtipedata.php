<?php
$nim = 'A';
$nama = "Muhamad Wahab Husaeni";
$umur = 20;
$nilai = 99.25;
$status = TRUE;

echo "---Belajar Tipe Data --- <br><br>";
echo "Tipe Data Char: ". $nim. "<br>";
echo "Tipe Data String: $nama<br>";
print "Tipe Data Int: ". $umur;
print "<br>";
printf("Tipe Data Float: %.5f<br><br>", $nilai);
echo "Tipe Data Boolean: <br><br>";

if ($status)
    echo "Status: Aktif";
else
    echo "Status: Tidak Aktif";
?>