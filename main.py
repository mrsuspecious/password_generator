import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase  #string docs python
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    # now we have 4 string and i will create password from them
    pslen = int(input("Enter password length\n"))  #concating string to int
    s = [] #blank string
    s.extend(list(s1))  #we are extending list means put elemets of s1 into s list
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    #for shuffling the list just like uno cards
    random.shuffle(s)
    #print(s)
    print("Your password is:")
    print("".join(random.sample(s,pslen)))
    #print("".join(s[0:pslen])) #join is sued to join pslen with the string 