#Email Validator
"""It is used to check whether your email format is correct or not.
Format of the Email:-
(i) The length of email should be greater than 6.
(ii) First letter of email should be small letter.
(iii) Single "@" should be used. 
(iv) In the last of the email, you have to use either ".in" or ".com"
(v) You should not have to use the space and uppercase letter in the email."""
email=input("Enter the Email :")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if(email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or "@" or ".":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("You should have to avoid space and uppercase letter in the email.")
                else:
                    print("Congratulation! Your email format is totally correct.")
            else:
                print("Either you have to use .in or .com in the end of the email.")
        else:
            print("There should be one @ symbol in email and the use of a @ is compulsory.")
    else:
        print("First letter of the email should be small letter.Please make it correct!")
else:
    print("Your email is too shorter.Make it in proper way.")