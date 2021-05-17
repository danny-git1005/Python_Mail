import pandas as pd

mail = pd.read_csv("all_mail.csv")
df = pd.DataFrame(columns=["name","mail"])

for i in range(len(mail)):
    temp = mail["name"][i]
    string = str(temp).split(" ")
    print(string)
    df = df.append({"name":string[0], "mail":string[1]}, ignore_index=True)

df.to_csv("student_mail.csv",encoding="utf-8-sig")
print(df)
