int romanToInt(char* s) {
    int size = strlen(s);
    int result[size]; 
    int count = 0;

for (int i = 0; i < size; i++) {
    switch (s[i]) {
        case 'I':
            result[i] = 1;
            break;
        case 'V':
            result[i] = 5;
            break;
        case 'X':
            result[i] = 10;
            break;
        case 'L':
            result[i] = 50;
            break;
        case 'C':
            result[i] = 100;
            break;
        case 'D':
            result[i] = 500;
            break;
        case 'M':
            result[i] = 1000;
            break;
        default:
            break;
    }
}

    for (int i = 0; i < size - 1; i++) {
        if (result[i] >= result[i+1]) {
            count += result[i];
        } 
        else {
            count -= result[i];
        }
    }
    count += result[size-1];
    
    return count;
}