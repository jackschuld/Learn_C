

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    *returnSize = numsSize;
    int* results = malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        results[i] = i % 2 == 0 ? nums[i/2] : nums[n + (i/2)];
    }
    return results;
}