import requests

flag=0

while(True):

    # Printing options
    print('1. Get movie details. \n'
          '2. Get movie details sorted by name/rating/release date/duration. \n'
          '3. Search movies by name or description')

    choice = int(input("Enter your choice [1,2 or 3]"))

    if(int(choice) in [1,2,3]):

        if(flag!=1):
            loginID = input("Enter the login ID:")
            password = input("Enter the password:")
            flag = 1

        if(choice == 1):
            mv_name = input("Enter the name of the movie:")
            s = "-"
            mv_name = s.join(mv_name.lower().strip().split())
            print(requests.get('http://localhost:8080/getMovie/'+mv_name, data={}, auth=(loginID, password)).text)

        elif (choice == 2):
            field = input("Enter the field by which you want to sort [movie/imdb/year/duration]:")
            field = field.strip().lower()
            c = input("Enter asc for ascending and desc for descending")
            c = c.strip()
            print(requests.get('http://localhost:8080/sortBy/' + field + '/' + c, data={}, auth=(loginID, password)).text)

        elif (choice == 3):
            field = input("Enter the field by which you want to search [movie/description]:")
            field = field.strip().lower()
            keyword = input("Enter the keywords for searching:")
            s = "-"
            keyword = s.join(keyword.lower().strip().split())
            print(requests.get('http://localhost:8080/searchBy/' + field + '/' + keyword, data={}, auth=(loginID, password)).text)

    else:
        print("Please enter a valid option")
        continue

    while(True):
        i = input("Do you wish to continue? [y/n]").lower()
        if(i!='y' and i!='n'):
            print("Please enter a valid option.")
            continue
        break

    if(i=='y'):
        continue
    else:
        break




