import requests
import json

print("Sign into the PaidRight data platform api and upload files\n")

dpw_url = 'https://dpw-stg.paidright.io/api'
tenant_id = 'TODO'
username = 'TODO'
password = 'TODO'

if tenant_id == 'TODO' or username == 'TODO' or password == 'TODO':
    print('Please complete the setup of your input variables:')
    if tenant_id == 'TODO':
        print('\ttenant_id is required')
    if username == 'TODO':
        print('\tusername is required')
    if password == 'TODO':
        print('\tpassword is required')
    exit(1)

print('dpw_url:', dpw_url)
print('tenant_id:', tenant_id)
print('\n')

# Lib functions 
#

def fetch_auth_token(): 
    body = {
      'email': username,  
      'password': password
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(
        f'{dpw_url}/login', 
        headers=headers, 
        data=json.dumps(body)
    )
    return r.text.replace('\"', '')

def upload_file(auth_token, file_name, file_category): 
    headers = {
        'Content-Type': 'application/octet-stream',
        'Authorization': auth_token,
        'File-name': file_name,
        'File-category': file_category
    }

    with open(file_name, 'rb') as f:
        data = f.read()
    
    r = requests.post(
      f'{dpw_url}/{tenant_id}/file', 
      headers=headers, 
      data=data
    )

    return r.text

# control flow
#

print('signing in and fetching the auth_token...')
auth_token = fetch_auth_token()
print('auth_token:', auth_token)
print('\n')

print("uploading files..")

timesheet = upload_file(
    auth_token, 
    '../fixtures/timesheet.csv', 
    'FileCategoryTimesheet'
)
print('timesheet:', timesheet)
print('\n')

roster = upload_file(
    auth_token, 
    '../fixtures/roster.csv', 
    'FileCategoryRoster'
)
print('roster:', roster)
print('\n')

masterfile = upload_file(
    auth_token, 
    '../fixtures/emp-events.csv', 
    'FileCategoryMasterfile'
)
print('masterfile:', masterfile)
print('\n')

payments = upload_file(
    auth_token, 
    '../fixtures/payments.csv', 
    'FileCategoryPayRecords'
)
print('payments:', payments)
print('\n')

print('complete.')
