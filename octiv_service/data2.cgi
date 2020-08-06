#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_data2.json";
    http_response_code(200);

    if (file_exists($file)) {
        $response = json_decode(file_get_contents($file), true);
        assign($response);
    } else {
        $response = array();
        $response["ion_flux"] = rand();

    }
    
    $len = rand(1, 10);
    $channel = array();
    $chan_file = "responses/octivchannel.json";

    for ($i = 0; $i < $len; $i++) {
        if (file_exists($file)) {
            $chan = json_decode(file_get_contents($chan_file), true);
            assign($chan);
        } else {
            $chan = array();
            $chan["timestamp"] = rand();
            $chan["frequency"] = rand();
            $chan["power"] = rand();
            $chan["forward_power"] = rand();
            $chan["reflected_power"] = rand();
            $chan["standing_wave_ratio"] = rand();        
        }

        #Assuming these arrays must be of same length. 
        $len2 = rand(1, 10);
        $chan["voltage"] = int_arr_rand($len2, true);
        $chan["current"] = int_arr_rand($len2, true);
        $chan["phase"] = int_arr_rand($len2, true);
        $channel[$i] = $chan;
    }

    $response["channel"] = $channel;

    echo json_encode($response, JSON_PRETTY_PRINT);
?>