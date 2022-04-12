<?php
include "user.php";
include "flag.php";
$u = unserialize(base64_decode($_COOKIE['user']));

if ($u->name === "admin") {
    echo $flag;
}

highlight_file(__FILE__);