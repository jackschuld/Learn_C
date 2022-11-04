class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [cha for cha in a]
        b = [chb for chb in b]
        carry = '0'
        
        # Makes lists equal length
        while len(a) != len(b):
            if len(a) < len(b):
                a.insert(0, '0')
            else:
                b.insert(0, '0')
        
        # Add
        for i in reversed(range(len(a))):
            print(a[i], b[i], carry)
            if a[i] == '1' and b[i] == '1':
                if carry == '0':
                    a[i] = '0'
                    carry = '1'
            elif a[i] == '1' or b[i] == '1':
                if carry == '0':
                    a[i] = '1'
                else:
                    a[i] = '0'
            elif a[i] == '0' and b[i] == '0' and carry == '1':
                a[i] = '1'
                carry = '0'
            
            
        # Add 1 to front if there is one left over
        if carry == '1':
            a.insert(0, '1')
            
        return ''.join(a)
                    
        
        

        
        
        
        
        
        
        #while len(b)<len(a):
        #    b='0'+b
        #while len(a)<len(b):
        #    a='0'+a
        #carry=0
        #a=[int(i) for i in a]
        #b=[int(i) for i in b]
        #ans=''
        #for i in range(len(a)-1,-1,-1):
        #    val=a[i]+b[i]+carry
        #    if val==3:
        #        carry=1
        #        ans='1'+ans
        #    elif val==2:
        #        carry=1
        #        ans='0'+ans
        #    elif val==1:
        #        ans='1'+ans
        #        carry=0
        #    else:
        #        ans='0'+ans
        #return str(carry)+ans if carry else ans