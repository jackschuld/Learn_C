int romanToInt(char* s) {
    int size = strlen(s);
    int result[size]; 
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (s[i]=='I') {
            result[i] = 1;
            }
        else if (s[i]=='V') {
            result[i] = 5;
            }
        else if (s[i]=='X') {
            result[i] = 10;
            }
        else if (s[i]=='L') {
            result[i] = 50;
        }
        else if (s[i]=='C') {
            result[i] = 100;
        }
        else if (s[i]=='D') {
            result[i] = 500;
        }
        else if (s[i]=='M') {
            result[i] = 1000;
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