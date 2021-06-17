*** Settings ***
Documentation   Позитивные и негативные тесты, проверяющие работу обработчика запросов HTTP сервера
Metadata    Автор   Евгений Киятов
Resource  tests/tests_resources.robot
Test Setup      Test Setup
Test Teardown   Test Teardown
*** Test Cases ***
Check Responses Positive
    [documentation]  Проверка позитивных сценариев
    [template]  Do GET And Check Expected Status
    IMSI=_321oijsd_WET_2    200
    IMSI=_  200
    IMSI=f  200
    IMSI=Fd     200
    IMSI=Usij_42II0ps0_     200
    IMSI=isj__sW23 PU=9123_%%3a23jde    200
Check Responses Negative
    [documentation]  Проверка негативных сценариев
    [template]  Do GET And Check Expected Status
    IMSI=p123_ses--    500
    IMSI=      500
    IMSI=idoskapIUj2___ii    500
    ISMI=329__dAWd    500
    IMSI=*  500

