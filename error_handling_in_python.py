''' PART-1 
In this part one f you have any doubt on any part of the code,
                      then place the code in the try block so that the error cannot get executed in the program'''

# print('python program')                                                      # python program
# print('coding environment')                                                  # coding environment
# try:
#     print(hh)                                                                # NameError
# except:
#     print('you have not defined the name')                                   # you have not defined the name
# print("Hello world!")                                                        # Hello world!
# print("Welcome!!")                                                           # Welcome!!



# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# try:
#     a='hello'
#     print(int(a))                                                             
# except:
#     print('you cannot convert the str into int')                             # # you cannot convert the str into int
# print("Hello world!")                                                        # Hello world!
# print("Welcome!!")                                                           # Welcome!!


''' PART-2 
If there  is no error in the try block then the code does not go to the except block 
        it will jump directly to the next code of line'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# try:
#     print(15/3)                                                                # 5.0                                            
# except:
#     print('you cannot convert the str into int')                             
# print("Hello world!")                                                          # Hello world!
# print("Welcome!!")                                                             #Welcome!


''' PART-3 
In this part we have mentioned the specific name in the except block so that 
code will run only when it consider the error as ZeroDivisionError other than that we will get error'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a='hello'
# try:
#     print(b)                                                                    # NameError                                                            
# except ZeroDivisionError:
#     print('you cannot convert the str into int')                             
# print("Hello world!")                                                        
# print("Welcome!!")


''' PART-4'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a='hello'
# try:
#     print(a)                                                                    # 'hello
#     print(b)                                                                    # NameError                                                            
# except ZeroDivisionError:
#     print('you cannot convert the str into int')                             
# print("Hello world!")                                                        
# print("Welcome!!")


'''PART- 5'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# try:
#     print(a/3)                                                                 # 3.3333333333333335
#     print(a/0)                                                                                                                              
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                           # You cannot divide the number with the 0            
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!")                                                             # Welcome!


'''PART-6 
we can have multiple except block in your code'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# try:
#     print(a/3)                                                                 # 3.3333333333333335
#     print(b)                                                                                                                              
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                                     
# except NameError:
#     print("you have not defined the name")                                     # you have not defined the name
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!") 

''' In this part if you are using two kind of except block then the 1st line of code error will get executed 
and then comes out of the try block and print the remaining ones'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# try:
#     print(a/3)                                                                 # 3.3333333333333335
   
#     print(5/0)       
#     print(b)                                                                                                                     
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                                     
# except NameError:
#     print("you have not defined the name")                                     # you have not defined the name
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!") 


'''PART-7 '''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# try:
#     print(a/3)                                                                 # 3.3333333333333335
#     print(a)                                                                   # 10
#     print(5/0)       
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                           # You cannot divide the number with the 0                                 
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!")                                                             # Welcome!


''' PART-8'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# try:
#     print(a/3)                                                                 # 3.3333333333333335
#     print(a)                                                                   # 10
#     print(5/0) 
#     print(a+'shahed')                                                          # line no 143 has not been printed 
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                           # You cannot divide the number with the 0                                 
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!")   

''' PART-9'''

# print('python program')                                                        # python program
# print('coding environment')                                                    # coding environment
# a=10
# b=3.14
# try:
#     print(a/3)                                                                 # 3.3333333333333335
#     print(5/0)                                                                
#     print(a+b)                                                                 # line no 158 not printed
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                           # You cannot divide the number with the 0                                 
# print("Hello world!")                                                          # Hello world!                                            
# print("Welcome!!")                                                             # Welcome!

''' PART-10'''
# same as PART-9

''' PART-11'''

# print('python program')                                                        
# print('coding environment')                                                    
# a=10
# b=3.14
# try:
#     print(a/3)                                                                 
#     print(,)                                                                   # SyntaxError(Cannot be get fixed because it's a big error)                                                              
# except SyntaxError:
#     print('You cannot divide the number with the 0')                                                           
# print("Hello world!")                                                                                                   
# print("Welcome!!")                                                             
# Same for the indentationError has well.

''' PART-12'''

# print('python program')                                                         # python program                                              
# print('coding environment')                                                     # coding environment                                              
# a=10
# b=3.14
# try:
#     print(a/7)                                                                  # 1.4284                                                                                                                      
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0') 
# finally:
#     print('It\'s okay next time do not divide it by 0')                         #  It's okay next time do not divide it by 0                                                     
# print("Hello world!")                                                           # Hello world!                                                                                                  
# print("Welcome!!")                                                              # Welcome!!                                                             


''' PART-13 '''

# print('python program')                                                         # python program                                              
# print('coding environment')                                                     # coding environment                                              
# a=10
# b=3.14
# try:
#       print(a/7)                                                                # 1.4284                                                                                                                      
#       print(a/0)
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                            # You cannot divide the number with the 0
# finally:
#     print('It\'s okay next time do not divide it by 0')                         #  It's okay next time do not divide it by 0                                                     
# print("Hello world!")                                                           # Hello world!                                                                                                  
# print("Welcome!!")                                                              # Welcome!


''' PART-14'''

# print('python program')                                                         # python program                                              
# print('coding environment')                                                     # coding environment                                              
# a=10
# b=3.14
# try:
#       print(a/7)                                                                # 1.4284                                                                                                                      
#       print(a/10)                                                               # 1.0
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                            
# else:
#     print('It\'s okay next time do not divide it by 0')                         #  It's okay next time do not divide it by 0                                                     
# print("Hello world!")                                                           # Hello world!                                                                                                  
# print("Welcome!!")                                                              # Welcome!

''' In this part the else block will not get executed because we have the ZeroDivisionError hence the else part is not get executed'''

# print('python program')                                                         # python program                                              
# print('coding environment')                                                     # coding environment                                              
# a=10
# b=3.14
# try:
#       print(a/7)                                                                # 1.4284                                                                                                                      
#       print(b/0)
# except ZeroDivisionError:
#     print('You cannot divide the number with the 0')                            # You cannot divide the number with the 0
# else:
#     print('It\'s okay next time do not divide it by 0')                                                                             
# print("Hello world!")                                                           # Hello world!                                                                                                  
# print("Welcome!!")   



