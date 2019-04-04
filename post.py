import requests

endpoint = "http://localhost:5021/user"


def match_username_and_password():
    id_start = 1
    id_end = 70
    login_string = "mathe"
    leading_zero = "0"

    for i in range(id_start, id_end):
        if i < 10:
            u = login_string + leading_zero + str(i)
            print(u)

            data = {
                'user_name': u,
                'user_password': u
            }

            req = requests.post(url=endpoint, data=data)
            res = req.text
            print(res)

        else:
            u = login_string + str(i)
            print(u)

            data = {
                'user_name': u,
                'user_password': u
            }

            req = requests.post(url=endpoint, data=data)
            res = req.text
            print(res)


match_username_and_password()
