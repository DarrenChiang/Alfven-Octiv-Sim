#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_frame.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
        assign($response, 10);
    } else {
    	http_response_code(500);
    	exit();
    }

    echo json_encode($response, JSON_PRETTY_PRINT);
?>