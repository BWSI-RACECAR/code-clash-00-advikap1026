class Solution:
    def helloworld(self, string):
        #input type: String
        # return type: String
        
        # TODO: Write code below to return a string with the solution to the prompt
        if string == "Hello World!":
            return string
        else:
            return ""
        pass
        

def main():
    tc1 = Solution()
    string1= input()
    ans = tc1.helloworld(string1)
    print(ans)

if __name__ == "__main__":
    main()