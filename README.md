# tabby
tabby is a fancy dashboard for newly opened browser tabs. 
### preview
![dashboard preview](tabby.png)

### how does it work?
after coding the application i added the localhost alias 'tabby.dashboard' to the '/etc/hosts' file and flushed the dns cache to allow it to be recognized. i then wrote two launchd agents [com.name.tabby-fastapi.plist](./com.name.tabby-fastapi.plist) and [com.name.tabby-vue.plist](./com.name.tabby-vue.plist) to start both the api and the vue app on login. for the vue app i used the command *npm run preview* to get the newest prod version on every build. to avoid future conflicts with the *npm run preview* default port i picked a custom port.

### mockup
![dashboard mockup](mockup.png)
