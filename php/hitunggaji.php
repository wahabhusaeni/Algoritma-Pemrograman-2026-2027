<?php
$gaji = 10000000;
$tunjangan = 1000000;
$pajak = 0.1;

$bruto = $gaji + $tunjangan;
$thp = $bruto - ($bruto * $pajak);

echo "Gaji sebelum pajak = Rp " . number_format($bruto) . "\n";
echo "Gaji bersih = Rp " . number_format($thp);