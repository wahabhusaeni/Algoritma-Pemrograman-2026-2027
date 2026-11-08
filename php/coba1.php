<?php
$nim = "1.2220222";
$nama = 'Muhamad Wahab usaeni';
$umur = 20;
$nilai = 92.75;
$status = TRUE;

echo "NIM: ".$nim. "<br>";
echo "Nama: $nama<br>";
print "Umur: ".$umur;
print "<br>";
printf("Nilai: %.3f<br>", $nilai);

if ($status)
    echo "Status: Aktif";
else
    echo "Status: Tidak Aktif";
?>