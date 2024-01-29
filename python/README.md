### Integration example using Python 3

The script in this directory will show you how to authenticate
to the PaidRight data platform (dpw) and upload csv files for 
validation. 

## Development 

set up your python environment by installing the following pip
packages

```
python -m pip install requests json
```


To generate some credentials and a tenant which you will need
access the PaidRight system, It is recommended to use the staging 
environment while you are in development. You can access by 
navigating your web browser to: 
```
https://app-stg.paidright.io
```

Sign up for a new account, log in using your credentials and 
create your first tenant. Once you can browse around your empty
tenant then you can retrieve your tenant id from the url. 

```
https://app-stg.paidright.io/16e8c270d7bf1dedaff58714/files

then your tenant id is: 16e8c270d7bf1dedaff58714
and your dpw url is: https://dpw-stg.paidright.io/api
```
Open up the main.py file and enter the 4 variables found at the
top of the script. Once you are ready you can give it a try:

```
python main.py 
```

You should see output that looks like this. 

```
Sign into the PaidRight data platform api and upload files

dpw_url: https://dpw-stg.paidright.io/api
tenant_id: c99e0982f6d747c2cbe72858


signing in and fetching the auth_token...
auth_token: 2e1af4b918e7d6cf128a3f73


uploading files..
timesheet: {"contents":{"category":"FileCategoryTimesheet","columns":7,"created":"2024-01-29T04:02:49.351836Z","hiveGCSName":"timesheet/tenant_key=c99e0982f6d747c2cbe72858/file_key=47f1e8a2427b7772ed6499eb/47f1e8a2427b7772ed6499eb.csv","id":"47f1e8a2427b7772ed6499eb","name":"../fixtures/timesheet.csv","owner":"9bf589eb84a4c6eb8cd026b2","rows":446,"size":0,"sourceGCSBucket":null,"sourceGCSMD5Hash":null,"sourceGCSName":null,"tenantId":"c99e0982f6d747c2cbe72858"},"tag":"ValidatedFile"}


roster: {"contents":{"category":"FileCategoryRoster","columns":6,"created":"2024-01-29T04:02:49.548449Z","hiveGCSName":"roster/tenant_key=c99e0982f6d747c2cbe72858/file_key=2d50abab1677fd234ffdf463/2d50abab1677fd234ffdf463.csv","id":"2d50abab1677fd234ffdf463","name":"../fixtures/roster.csv","owner":"9bf589eb84a4c6eb8cd026b2","rows":441,"size":0,"sourceGCSBucket":null,"sourceGCSMD5Hash":null,"sourceGCSName":null,"tenantId":"c99e0982f6d747c2cbe72858"},"tag":"ValidatedFile"}


masterfile: {"contents":{"category":"FileCategoryMasterfile","columns":14,"created":"2024-01-29T04:02:49.665572Z","hiveGCSName":"employee/tenant_key=c99e0982f6d747c2cbe72858/file_key=cc269afae8b47b1d3aaf7190/cc269afae8b47b1d3aaf7190.csv","id":"cc269afae8b47b1d3aaf7190","name":"../fixtures/emp-events.csv","owner":"9bf589eb84a4c6eb8cd026b2","rows":9,"size":0,"sourceGCSBucket":null,"sourceGCSMD5Hash":null,"sourceGCSName":null,"tenantId":"c99e0982f6d747c2cbe72858"},"tag":"ValidatedFile"}


payments: {"contents":{"category":"FileCategoryPayRecords","columns":5,"created":"2024-01-29T04:02:49.822526Z","hiveGCSName":"payment/tenant_key=c99e0982f6d747c2cbe72858/file_key=99e76a301052f593a4a052fd/99e76a301052f593a4a052fd.csv","id":"99e76a301052f593a4a052fd","name":"../fixtures/payments.csv","owner":"9bf589eb84a4c6eb8cd026b2","rows":41,"size":0,"sourceGCSBucket":null,"sourceGCSMD5Hash":null,"sourceGCSName":null,"tenantId":"c99e0982f6d747c2cbe72858"},"tag":"ValidatedFile"}


complete.
```

## Production 

To launch your script into a Production environment you can use
the following dpw url: `https://dpw.paidright.io/api`

You will need to configure a separate username / password for the production environment. 
