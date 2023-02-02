import qrcode
#Link to mmy github
github = "https://github.com/DenzelGitonga007"
#Encode the link
github_qrcode = qrcode.make(github)
#Save the png
github_qrcode.save("DenzelGitHub.png")