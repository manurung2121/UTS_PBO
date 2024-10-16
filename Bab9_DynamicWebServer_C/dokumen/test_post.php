<?php
$username = $_POST['username']; //dimodul user perbaiki pd saat eksekusi
$passwd = $_POST['passwd'];
if( ($username == 'manurung2102@gmail.com') && ($passwd == '211')) {
echo "<h1>Proses Login Berhasil</h1>\n";
echo "<p>User Name anda : $username</p>\n";
} else {
    echo "<h1>Anda Gagal Login!</h1>\n";
echo "<p>User Name $username anda salah</p>\n";
echo "<p>Atau password $passwd ini salah</p>\n";
}
?>