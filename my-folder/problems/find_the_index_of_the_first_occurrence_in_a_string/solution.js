/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (let h = 0; h < haystack.length; h++) {
        if (haystack[h] === needle[0]) {
            let isSameWord = true;
            for (let n = 0; n < needle.length; n++) {
                if (needle[n] !== haystack[n + h]) {
                    isSameWord = false;
                }
            }
            if (isSameWord === true) {
                return h;
            }
        }
    }
    return -1;
};