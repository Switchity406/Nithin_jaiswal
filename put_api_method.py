import requests

def update_user(user_id, name=None, job=None):
    payload = {}
    if name:
        payload['name'] = name
    if job:
        payload['job'] = job
    response = requests.put(f"https://reqres.in/api/users/{user_id}", data=payload)
    if response.status_code == 200:
        updated_user = response.json()
        return updated_user
    else:
        print(f"Error updating user. Status code: {response.status_code}")
        return None

# Example usage
new_user_id = create_user("John Doe", "Software Engineer")
print(new_user_id)

updated_user = update_user(new_user_id, name="Jane Doe")
print(updated_user)
