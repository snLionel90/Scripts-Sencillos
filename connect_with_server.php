<?php

$hostname='localhost';
$database='db_server_name';
$username='root';
$password='';

$conexion=new mysqli($hostname,$username,$password,$database);
if($conexon->connect_errno){
    echo "lo sentimos, la conexion se ha perdido";
}

?>
