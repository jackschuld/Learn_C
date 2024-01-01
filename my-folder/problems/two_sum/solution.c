#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < numsSize; j++) {
            if (i == j) {
                continue; 
            }
            if (nums[i] + nums[j] == target) {
                int* result = (int*)malloc(2 * sizeof(int));
                if (result == NULL) {
                    return NULL;
                }

                result[0] = i;
                result[1] = j;
                *returnSize = 2;

                return result;
            }
        }
    }
    return NULL;
}