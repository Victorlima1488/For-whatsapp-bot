<?php
$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot';
$conn = mysqli_connect($servidor,$usuario,$senha,$banco);

$phone_number = $_GET['phone'];
$msg = $_GET['msg'];
$user = $_GET['user'];
$response = '';

$sql = "SELECT * FROM usuario WHERE telefone = '$phone_number'";
$query = mysqli_query($conn, $sql);
$total = mysqli_num_rows($query);

if($query){
    $rows_usuarios = mysqli_fetch_array($query);
    if($rows_usuarios){
        $status = $rows_usuarios['status'];
    }
}

?>

<?php

$menu2 = 'Não sei quanto voce ganha, mas a oportunidade que hoje estou oferecendo é salario de 2 mil a 8 mil por mês trabalhando de um celular ou computador, inicialmente trabalhando apenas meio período, o serviço de Marketing online, você ja trabalhou com isso?'; 

$menu3 = 'Ainda tenho tres vagas na esquipe de vendas online, te interresa saber mais?';

$menu4 = 'da uma olhada nesse link  https://editacodigo.com.br/index/curso.php ';

$menu5 = "Entao como tinha te falado o link https://editacodigo.com.br/index/curso.php  responde a todas a suas duvidas.";

?>

<?php
if($total == 0){
    $sql = "INSERT INTO usuario (telefone, status) VALUES ('$phone_number', '1')";
    $query = mysqli_query($conn, $sql);

    if($query){
        echo "Olá, seja bem vindo ao futuro! Vi que é sua primeira vez aqui. Como posso lhe ajudar?";
    }
}

if($total == 1){
    
    if($status == 1){
        $response = $menu2;
    }
    
    if($status == 2){
        $response = $menu3;
    }
    
    if($status == 3){
        $response = $menu4;
    }

    if($status == 4){
        $response = $menu5;
    }

    if($status < 5){
        echo $response;

        $status2 = $status + 1;
        $sql = "UPDATE usuario SET status = '$status2' WHERE telefone = '$phone_number'";
        $query = mysqli_query($conn, $sql);
    }

    if($status >= 5){
        echo "Muito obrigado pela sua atenção!";

        $status2 = $status + 1;
        $sql = "UPDATE usuario SET status = '1' WHERE telefone = '$phone_number'";
        $query = mysqli_query($conn, $sql);
    }
}

$data = Date('d-m-Y');

$sql = "INSERT INTO historico (telefone, msg_cliente, msg_bot, data) VALUES ('$phone_number', '$msg', '$response', '$data')";
$query = mysqli_query($conn, $sql);
?>