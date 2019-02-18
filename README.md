# What is this
This is a data loader and data sync app to update the numbers from excel workbook to firebase database and vice versa (sync data from firebase to excel sheet on computer).
# Why is that
This is more robust to errors of deletion all numbers. more easy to understand and edit.
#What about backups
There is two different backups folder, first is "backups" which backup the data each time (within an hour) data loader is run meaning that it uploads the numbers to database and take a snapshot of current data.
"backups_sync" is the same functionality but for the reversed process of syncing data from firebase to computer.
# Usage
## overview
To user the code, you have to own your own project and get admin auth or database secret from service account in your project settings.
This enable you to control your project regardless of security rules.
Don't push the secret on github
## Where to put the secret
make a config.json file like this
```json
{
    "database secret": "[your database secret]",
    "database base url": "https://[your project id].firebaseio.com"
}
```
## where to put the data
The data should be an xlsx extension excel file named numbers, this is where "data loader" load numbers from.
