again=2
print("Welcome to online-diary.net!")
print("Please enter your Username and Password ")
username=input("Username: ")
password=input("Password: ")
while username=="C_Auguste" and password!="TryAgain":
  while again==2:
    again=1
    print("Try again")
    username=input("Username: ")
    password=input("Password: ")
  while again==1:
    again=0
    print("Try Again")
    username=input("Username: ")
    password=input("Password: ")
  else:
    print("TryAgain")
    username=input("Username: ")
    password=input("Password: ")
if username=="C_Auguste" and password=="TryAgain":
  print("Welcome, C_Auguste!")
  print("In your last session, you wrote:")
  print("It's me. I'm the Contra-Auguste clown. Father is a Whiteface. And Elene is the Auguste. I can't do this anymore. One more argument and I'll snap. The trauma from my childhood will take over. Sometimes I look in the mirror and just have my hands covering my crying face. But that's it. Next time. Next time.")
elif username=="Milo_M" and password=="Guilty":
  print("Welcome, C_Auguste!")
  print("In your last session, you wrote:")
  print("I'm worried about Mason. He cries out at night. I don't know if he's ok. I've tried to be better for him, but it doesn't look like it's going to possible. He's still so much like the child he was all those years ago. Fearful. Scared. Elene is good for him. She's calm, and controls a situation very easily. I can't believe she died!")
elif username=="Scarlet_Starts" and password=="I1oveMason!":
  print("Welcome, Scarlet_Starts!")
  print("In your last session, you wrote:")
  print("Mason is just so HOT! WTF! How is this even legal lmfao! I finally made my move today. I asked him out. He's so cute! I can't believe it's taken me until I'm 19 to get feelings for a guy. I was starting to worry I was asexual! But no, thank god. This was where it got awkward. He's already in a relationship with some b*tch called Elene. So he said 'Let's begin an affair. You deserve me more than she does.' And I nearly fainted. Yes. I love him. He's so evil.")
elif username=="Azoth" and password=="EleneFTW":
  print("Welcome, Azoth!")
  print("In your last session, you wrote:")
  print("Why does Scarlet have to be so mean? Elene would never have been so difficult to talk to. I'd make sure she knew I love her. From what I hear about Mason, he's not the best person to be around. Maybe I should tell him about it. No. I definitely can't talk to someone as crazy as him. He's so toxic. Although, when I think about, I did hear he's traumatized from what he went through as a child.")
elif username=="Stickmin" and password=="To7a!ed":
  print("Welcome, Stickmin!")
  print("In your last session, you wrote:")
  print("Why won't Elene love me? She's so incredibly beautiful, and hot, too! My day's been terrible. My heroin dealer got raided and arrested, so I'm going to have to find a new source. God, I love how Mason made this website!")
else:
  print("Incorrect. Due to poor design choices, you'll have to reload the page to try again.")
