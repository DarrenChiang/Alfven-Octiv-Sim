#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_config.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
    } else {
        $response = array();
    }

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $post = json_decode(file_get_contents('php://input'));

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
        $response["refresh_rate"] = rand();
        $response["selected_harmonics"] = int_arr_rand();

        if (rand(0, 1)) {
            $response["signal_lock"] = 'V';
        } else {
            $response["signal_lock"] = 'C';
        }     
    }
     
    echo json_encode($response, JSON_PRETTY_PRINT);
?>