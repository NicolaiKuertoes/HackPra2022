<?php
include("user.php");
if ($_POST) {
    if ($_POST['user'] === "admin") {
        die("YOU CAN'T BE ADMIN!!");
    } else {
        $u = new User($_POST['user']);
        setcookie("user", base64_encode(serialize($u)));
        header("Location: app.php");
    }
}
if (isset($_GET['source'])) {
    highlight_file(__FILE__);
}
?>