<?php
    /**
     * Attempting to generate a singe precision
     * floating point number.
     * Unused for now.
     */
    function random_single_prec_float() {
        $sign = pow(-1, rand(0, 1));
        $exp = rand(0, pow(2, 8) - 1);
        $mant = rand(0, pow(2, 23) - 1);
        return true;
    }

    /**
     * Generates random string.
     * 
     * @param {$max_len} the max possible length of the generated string
     * @param {$max} whether to always use $max_len as length of the string
     */
    function str_rand($max_len = 10, $max = false) {
        $charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        $str = "";
        $len = $max_len;

        if (!$max) {
            $len = rand(1, $max_len);
        }

        for ($i = 0; $i < $len; $i++) {
            $str .= substr($charset, rand(0, strlen($charset)), 1);
        }

        return $str;
    }

    /**
     * Generates random int array with random int from 0 to 100.
     * 
     * @param {$max_len} the max possible length of the generated array
     * @param {$max} whether to always use $max_len as the length of the array
     */
    function int_arr_rand($max_len = 10, $max = false) {
        $arr = array();
        $len = $max_len;

        if (!$max) {
            $len = rand(1, $max_len);
        }

        for ($i = 0; $i < $len; $i++) {
            $arr[$i] = rand(0, 100);
        }

        return $arr;
    }
?>