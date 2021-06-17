*** Settings ***
Resource    tests/resources/connections.robot
Resource    tests/resources/imports.robot
Library     tests.library.convert_to_dict
*** Keywords ***
Test Setup
    Create Session
Test Teardown
    Req.Delete All Sessions
Do GET And Check Expected Status
    [documentation]  Сравнение фактического ответа сервера с ожидаемым
    [arguments]   ${headers}     ${expected status}
    ${headers}  convert to dict   ${headers}
    ${response}     Req.GET On Session   alias   url=    headers=${headers}  expected_status=${expected status}