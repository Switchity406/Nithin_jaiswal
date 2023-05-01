import requests

def create_user(name, job):
    payload = {'name': name, 'job': job}
    response = requests.post("https://reqres.in/api/users", data=payload)
    if response.status_code == 201:
        new_user = response.json()
        return new_user['id']
    else:
        print(f"Error creating user. Status code: {response.status_code}")
        return None

# Example usage
new_user_id = create_user("John Doe", "Software Engineer")
print(new_user_id)
