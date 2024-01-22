/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    let returnArray = [];
    let keyValues = {}; // variable to put key value pairs
    for (let i = 0; i < groupSizes.length; i++) {
        if (keyValues[groupSizes[i]] && keyValues[groupSizes[i]].length < groupSizes[i]) {
            console.log(keyValues[groupSizes[i]])
            keyValues[groupSizes[i]].push(i);
        }
        else {
            keyValues[groupSizes[i]] = [i];
        }

        if (keyValues[groupSizes[i]].length === groupSizes[i]) {
            returnArray.push(keyValues[groupSizes[i]]);
        }
    }
    return returnArray;
};