import requests


def get_users(page=1):
    response = requests.get(f"https://reqres.in/api/users?page={page}")
    if response.status_code == 200:
        users = response.json()['data']
        filtered_users = [{'first_name': user['first_name'], 'email': user['email']} for user in users]
        return filtered_users
    else:
        print(f"Error fetching users. Status code: {response.status_code}")
        return []


def get_user_by_id(user_id):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    if response.status_code == 200:
        user = response.json()['data']
        return user
    else:
        print(f"Error fetching user {user_id}. Status code: {response.status_code}")
        return {}


# Example usage
all_users = get_users()
print(all_users)

user_2 = get_user_by_id(2)
print(user_2)
