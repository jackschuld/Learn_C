class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLastWord($s) {
        $words = array_filter(explode(" ", $s));
        return strlen(end($words));
    }
}