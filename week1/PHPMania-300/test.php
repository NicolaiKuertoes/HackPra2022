<?php

require_once('flag.php');
error_reporting(0);

$getParams = [
    'msg' => 'data://text/plain;base64,aW1ub29iIQ==',
    'key1' => 1337,
    'key2' => '1337＄aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'cc[]' => 1234,
    'k1' => 2,
    'hack' => 2,
    'bb' => "print(\$flag);//"
];

if(!isset($getParams['msg'])){
    highlight_file(__FILE__);
    die();
}

@$msg = $getParams['msg'];
if(@file_get_contents($msg)!=="imnoob!"){
    die('nope!1');
}

echo "u nuhb!";

@$k1=$getParams['key1'];
@$k2=$getParams['key2'];

$cc = 1337;$bb = 42;

if(intval($k1) !== $cc || $k1 === $cc){
    die("no\n");
}

if(strlen($k2) == $bb){
    if(preg_match('/^\d+＄/', $k2) && !is_numeric($k2)){
        if($k2 == $cc){
            @$cc = $getParams['cc'];
        }
    }
}

list($k1,$k2) = [$k2, $k1];

if(substr($cc, $bb) === sha1($cc)){
    foreach ($_GET as $lel => $hack){
        $$lel = $hack;
    }
}

//‮‮ rtl
$‮b = "2";$a="‮b";//;1=b

if($$a !== $k1){
    die("lel no\n");
}

assert("$bb == $cc");

echo "gz ;)";

