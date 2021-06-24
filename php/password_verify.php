<?php
$password = $argv[1];
$hashed_password = $argv[2];

$result = password_verify($password, $hashed_password);
if (!$result) {
    exit(1);
}
