def FizzBuzz(number):
        ret=""
        if number%3==0:
            ret+="fizz"
        if number%5==0:
            ret+= "buzz"
        if ret=="":
            ret=int(number)
        return ret
