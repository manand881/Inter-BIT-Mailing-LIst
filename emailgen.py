course_prefix="mca"
number_prefix_list=['250','400','450','100']
number_prefix=str()
email_list=list()
year=20

for z in range(19,21):
    year=z

    for y in number_prefix_list:
        number_prefix=y
        iterator=1

        for x in range (50):

            if len(str(iterator))==1:
                temp=course_prefix+number_prefix+str(0)+str(iterator)+"."+str(year)+"@bitmesra.ac.in"
                email_list.append(temp)
                iterator+=1

            if len(str(iterator))==2:
                temp=course_prefix+number_prefix+str(iterator)+"."+str(year)+"@bitmesra.ac.in"
                email_list.append(temp)
                iterator+=1
      

print(*email_list, sep = "\n ") 
print(len(email_list))     
