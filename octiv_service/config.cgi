#!C:\xampp\php\php.exe

<?php
    #echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_config.json";
    http_response_code(200);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $post = json_decode(file_get_contents('php://input'), true);

        if ($post["refresh_rate"] < 0) {
            http_response_code(400);
            exit();
        }

        if (count($post["selected_harmonics"]) > 30) {
            http_response_code(400);
            exit();
        }

        if (!in_array($post["signal_lock"], array('V', 'C'))) {
            http_response_code(400);
            exit();
        }

        $response = $post;
    } else {
        if (file_exists($file)) {
            $response = json_decode(file_get_contents($file), true);
            assign($response);
        } else {
            $response = array();
            $response["refresh_rate"] = rand();
            $response["selected_harmonics"] = int_arr_rand();
            $response["signal_lock"] = rand(0, 1) ? 'V' : 'C'; 
        }
    }
     
    echo json_encode($response, JSON_PRETTY_PRINT);
?>