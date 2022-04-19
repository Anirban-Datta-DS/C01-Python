def prime_list():
    
    p = int(input('How many prime numbers do you want?'))
    lst = []
    
    def check_prime(num):
        for i in range(2, num):
            if num%i == 0:
                return False
            else:
                return True
    
    while len(lst)<=p:
        i = 2
        if check_prime(i):
            lst.append(i)
            
        i += 1
    
    print(lst)
    

prime_list()