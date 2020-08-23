#!C:\xampp\php\php.exe

<?php
    #echo "Content-Type: application/json\n\n";

    include "../utils.php";

    http_response_code(200);

    if (isset($_GET["index"])) {
        if (file_exists("responses/server_events-index.json")) {
            $response = json_decode(file_get_contents("responses/server_events-index.json"), true);
            assign($response, 10);

            if (isset($_GET["v_only"])) {
                if ($_GET["v_only"]) {
                    unset($response["Current_Ir"]);
                    unset($response["Current_Ii"]);                 
                }
            }

			if (!isset($_GET["Reduce_factor"])) {
                unset($response["Reduce_factor"]);
            }
        } else {
            http_response_code(500);
            exit();
        }
    } else {
        if (file_exists("responses/server_events.json")) {
            $response = json_decode(file_get_contents("responses/server_events.json"), true);
            assign($response, 10);
        } else {
            http_response_code(500);
            exit();
        }
    }

    echo json_encode($response, JSON_PRETTY_PRINT);
?>