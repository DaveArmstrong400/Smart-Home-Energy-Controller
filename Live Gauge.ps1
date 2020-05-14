#Import meter reading column from csv created in the image processing code
#and sum the contents to calculate the weeks total energy usage
# this is then sent to the live gauge on the app for consumer viewing

$Readings = (Import-Csv "C:\Users\Dave_\OneDrive\Documents\Uni Work\5. Fifth Year\Semester 2\Major Individual Design Project II\Code\Meter Readings Data.csv").Reading       #load readings column and set to variable readings


$Minimum = 0           #set minimum weekly value for gauge
$Maximum = 630         #set maximum weekly value for gauge
$Target = 90           #set daily target value for gauge
$Gauge = 0             #set variable for total weekly usage
$Record = 0            #set variable for archived readings for the week

foreach ($Reading in $Readings){                   #take each reading value from the csv file, note there will only be one entry as the local csv file is overwritten on each entry. The complete file with each entry is saved to H:Drive
    
    $Usage = $Reading - $Record                    #calculate the usage for that day by subtracting the current reading from the previous days reading
    $Record = $Reading                             #set the record value to the current value to be used in the next cycle
    $Gauge = $Gauge + $Usage                       #update the live visual gauge with the addition of the new days usage, resulting in a total weekly usage

    $endpoint = "https://api.powerbi.com/beta/377e3d22-4ea1-422d-b0ad-8fcc89406b9e/datasets/c28fefaa-f183-4dc5-91b9-9d30d1cfae43/rows?key=pasUdQR91MOZBlOXuk9gsx3O4YnYbHCjGDF38ZkDWuaz2yicYmXJOuWctN6wFfuaZqAub8G4mNaV6s5MFgT%2F6g%3D%3D"    #set the url to send the data to (app)
    $payload = @{                                  # set which of the variables/the payload/data to be sent to the app
        "Minimum" = $Minimum
        "Maximum" = $Maximum
        "Target" = $Target
        "Usage" = $Usage
        "Gauge" = $Gauge
    }

    Invoke-RestMethod -Method Post -Uri "$endpoint" -Body (ConvertTo-Json @($payload))       #complete a post request with the data converted to json format

    $Target = $Target + 90                         #update the daily target by 90 on each day of the week to give the target total for instance in the week

    Write-Output $Target                           #display the values of the variables in the console for testing
    Write-Output $Reading
    Write-Output $Usage
    Write-Output $Gauge
    }
