
# Write  a program to print the following pattern
#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *



for i in range (0,6,1):
    print( ' '  * (5-i)  + "*"  ' '  *  i)