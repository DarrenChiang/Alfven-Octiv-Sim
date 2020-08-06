#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_data.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
        assign($response);
    } else {
        $response = array();
        $response["timestamp"] = rand();
        $response["frequency"] = rand();
    }

    #Assuming these arrays must be of same length. 
    $len = rand(1, 10);
    $response["voltage"] = int_arr_rand($len, true);
    $response["current"] = int_arr_rand($len, true);
    $response["phase"] = int_arr_rand($len, true);

    echo json_encode($response, JSON_PRETTY_PRINT);
?>