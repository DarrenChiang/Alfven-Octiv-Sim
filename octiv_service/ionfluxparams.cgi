#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/ion_flux_params.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
    } else {
        $response = array();
    }

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $response["voltage_drop"] = 0;
        $response["series_resistance"] = 0;
        $response["electrode_area"] = 1;
    } else {
        $response["voltage_drop"] = rand();
        $response["series_resistance"] = rand();
        $response["electrode_area"] = rand();
    }

    echo json_encode($response, JSON_PRETTY_PRINT);
?>