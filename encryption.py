class Encryption:

    def __init__(self):
        self.key ="!@#$%^&*~?0123456789"
        self.secret = list(self.key)
        

    def encrypt(self, var, d):
        self.data = self.rotate(list(var),d)
        self.cry = dict()
        for dt in self.data:
            if dt not in self.cry:
                self.rotate(self.secret,d)
                self.cry[dt] = self.secret[0]
                filename = format(ord('d'),'b') + format(ord(self.secret[0]),'b')
                with open(filename,'w') as file:
                    for i in range(1,129+d):
                        file.write(format(ord("i"),'b'))
                    file.write(format(ord(dt),'b'))
                    for i in range(1,129-d):
                        file.write(format(ord("i"),'b'))

        cryloud = list(self.cry.values())
        self.encrypted = "".join(cryloud)
        return "encryption done"
            

    def rotate(self,arr,d):
        if d>=len(arr):
            print("condition: d < len(arr)")
            d = int(input("Enter d: "))
            return self.rotate(arr,d)
        if d<=0:
            return arr
        arr.append(arr.pop(0))
        return self.rotate(arr,d-1)

    def decrypt(self, var, d):
        #reset
        self.key ="!@#$%^&*~?0123456789"
        self.secret = list(self.key)
        self.decrypted = list()
        decr = list()
        for lt in var:
            self.rotate(self.secret,d)
            filename = format(ord('d'),'b') + format(ord(self.secret[0]),'b')
            data1 = list()
            data2 = list()
            
            for i in range(1,129+d):
                data1.append(format(ord("i"),'b'))
            data1 = "".join(data1)
            for i in range(1,129-d):
                data2.append(format(ord("i"),'b'))
            data2 = "".join(data2)

            with open(filename, 'r') as file:
                fdata = file.read()
                fdata = fdata.strip()
            #print(len(data1))
            #print(len(data2))
            
            remain = len(fdata[len(data1):]) - len(data2)
            #print(remain)
            #print(fdata[len(data1):(remain+1)])
            decr.append(fdata[len(data1):(len(data1)+remain)])
            
        for binary in decr:
            binary = int(binary)
            decimal, i, n = 0, 0, 0
            while(binary != 0):  
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)  
                binary = binary//10
                i += 1 
            self.decrypted.append(chr(decimal))    
        
        for counter in range(1,len(self.decrypted)):
            self.rotate(self.decrypted,d)
            
        self.decrypted = "".join(self.decrypted)
    
