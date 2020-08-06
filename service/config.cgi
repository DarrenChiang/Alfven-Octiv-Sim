#!C:\xampp\php\php.exe

<?php
    echo "Content-Type: application/json\n\n";

    include "../utils.php";

    $file = "responses/server_config.json";
    http_response_code(200);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $post = json_decode(file_get_contents('php://input'), true);
        $response = $post;
    } else {
        if (file_exists($file)) {
            $response = json_decode(file_get_contents($file), true);
            assign($response);
        } else {
            $response = array();
            $response["frequency_limit"] = int_arr_rand(2, true);
            $response["refresh_rate"] = rand();
            $response["signal_lock"] = rand(0, 1) ? 'V' : 'I';
            $response["signal_base_threshold"] = rand();
            $response["noise_filter_length"] = rand();
            $response["event_max_length_1"] = rand();
            $response["event_min_amplitude_1"] = rand();
            $response["event_max_length_2"] = rand();
            $response["event_min_amplitude_2"] = rand();
            $response["event_max_length_3"] = rand();
            $response["event_max_amplitude_3"] = rand();
            $response["capture_switch_on_events"] = rand(0, 1) ? 'Y' : 'N';
            $response["min_switch_off_length"] = rand();
            $response["event_points"] = rand();
            $response["voltage_factor"] = rand();
            $response["current_factor"] = rand();
            #Incomplete.
        }
    }

    echo json_encode($response, JSON_PRETTY_PRINT);
?>