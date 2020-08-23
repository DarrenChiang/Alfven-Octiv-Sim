#!C:\xampp\php\php.exe

<?php
    #echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/ion_flux_params.json";
    http_response_code(200);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $post = json_decode(file_get_contents('php://input'), true);
        $response = $post;
    }  else {
        if (file_exists($file)) {
            $response = json_decode(file_get_contents($file), true);
            assign($response);
        } else {
            $response = array();
            $response["voltage_drop"] = rand();
            $response["series_resistance"] = rand();
            $response["electrode_area"] = rand();    
        }    
    }

    echo json_encode($response, JSON_PRETTY_PRINT);
?>