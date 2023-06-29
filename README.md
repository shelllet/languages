# WinUi++ 支持语言

* en-US
* zh-Hans-CN 
* zh-TW

# 生成配置

* en-US
  
    .\makepri createconfig /cf .\config\en-US\priconfig.xml /dq lang-en-US /o /pv 10.0.0

*  zh-Hans-CN 

    .\makepri createconfig /cf .\config\zh-Hans-CN\priconfig.xml /dq lang-zh-Hans-CN /o /pv 10.0.0

*  zh-TW
   
    .\makepri createconfig /cf .\config\zh-TW\priconfig.xml /dq lang-zh-TW /o /pv 10.0.0

# 生成命令

* en-US
    
    .\makepri new /pr .\Strings\en-US /cf .\config\en-US\priconfig.xml /o /of ./Translations/en-US


*  zh-Hans-CN 

    .\makepri new /pr .\Strings\zh-Hans-CN /cf .\config\zh-Hans-CN\priconfig.xml /o /of ./Translations/zh-Hans-CN

*  zh-TW
   
    .\makepri new /pr .\Strings\zh-TW /cf .\config\zh-TW\priconfig.xml /o /of ./Translations/zh-TW

# [dump](https://learn.microsoft.com/en-us/windows/uwp/app-resources/localize-strings-ui-manifest)

    .\makepri dump /if ./Translations/zh-Hans-CN.pri /o /of resources.pri.xml