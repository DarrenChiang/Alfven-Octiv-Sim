#!C:\xampp\php\php.exe

<?php
    #echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_info.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
        assign($response);
    } else {
        $response = array();
        $response["serial_number"] = str_rand();
        $response["sensor_type"] = str_rand();
        $response["frequencies"] = int_arr_rand();
        $response["harmonics"] = int_arr_rand();
        $response["firmware"] = str_rand();
        $response["firmware_rev"] = str_rand();
        $response["fpga_rev"] = str_rand();    
    }
    
    echo json_encode($response, JSON_PRETTY_PRINT);    
?>