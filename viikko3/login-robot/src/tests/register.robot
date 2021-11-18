*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Register

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kallereg  kalle123
    Input Credentials  kallereg  kalle123
    Output Should Contain  User with username kallereg already exists

Register With Too Short Username And Valid Password
    Input Credentials  re  kalle123
    Output Should Contain  Username re is too short

Register With Valid Username And Too Short Password
    Input Credentials  kallereg  kalle12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallereg  kallekalle
    Output Should Contain  Password should contain numbers

*** Keywords ***
Input New Command And Register
    Input New Command


