/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x = x.toString();
    x1 = x.split('');
    
    while (x1.length > 1) {
        if (x1.shift() !== x1.pop()) {
            return false
        }
    }
    return true
};