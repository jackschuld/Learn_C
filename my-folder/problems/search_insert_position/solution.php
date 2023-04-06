class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        $first = 0;
        $last = count($nums) - 1;
        while ($first <= $last) {
            $mid = floor(($first + $last) / 2);
            if ($nums[$mid] == $target) {
                return $mid;
            }
            if ($nums[$mid] < $target) {
                $first = $mid + 1;
            }
            else {
                $last = $mid - 1;
            }
        }
        return $first;
    }
}