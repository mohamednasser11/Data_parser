from parsers.handler import Handler
def main():
###main funtion where all the client operations happen###
    file = input('Please enter the file path \n')
    Handler(file)
if __name__== "__main__":
    main()