import smtplib    
# Calling SMTP    
s = smtplib.SMTP('smtp.gmail.com', 587)    
# TLS for network security    
s.starttls()    
# User email Authentication    
s.login("genesisdeep48@gmail.com", "tzrxduydgmfntbnq")    
# Message to be sent    
message = "hey sexy"    
# Sending the mail    
s.sendmail("genesisdeep48@gmail.com", "debasishmandal8244@gmail.com", message)