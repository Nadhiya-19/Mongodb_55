#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

a = ['1234', '4667', 'H345', 'U456', 'K765']
b = ['1234', '1234', '1234', '1234', '4567', '4567', '4567', '4567', '4567']

# Find unique common values
common_values = set(a) & set(b)

# Create the requested DataFrame
df = pd.DataFrame({
    'GUID': list(common_values),
    'Status': 'Updated'
})
print(df)


# In[12]:


html_table = df.to_html(index=False, border=1, justify="center")

# ✅ Build email body with HTML format
email_body = f"""
<html>
  <body>
    <p>Hi Rajaraman,</p>
    <p>Please find the output below:</p>
    {html_table}
    <p>Regards,<br>Nadhiya C</p>
  </body>
</html>
"""

# Email setup
sender_email = "nadhiyamhnrj@gmail.com"
receiver_email = "rjraman100@gmail.com.com"
password = "arvw nvho rfmm dtbz"  # ⚠️ Replace with your Gmail App Password, not your login password

msg = MIMEMultipart("alternative")
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "GUID matched values"

# Attach HTML content
msg.attach(MIMEText(email_body, "html"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("nadhiyamhnrj@gmail.com", "arvw nvho rfmm dtbz")
    server.send_message(msg)
    print("✅ Email sent successfully with formatted table!")
except Exception as e:
    print("❌ Failed to send email:", e)
finally:
    server.quit()


# In[13]:


import pandas as pd

a = ['1234', '4667', 'H345', 'U456', 'K765']
b = ['1234', '1234', '1234', '1234', '4567', '4567', '4567', '4567', '4567']

results = []
for item in a:
    if item in b:
        results.append({'GUID': item, 'Type': 'Matched '})
    else:
        results.append({'GUID': item, 'Type': 'Unmatched '})

df_1 = pd.DataFrame(results)
print(df_1)


# In[14]:


html_table = df_1.to_html(index=False, border=1, justify="center")

# ✅ Build email body with HTML format
email_body = f"""
<html>
  <body>
    <p>Hi Rajaraman,</p>
    <p>Please find the output below:</p>
    {html_table}
    <p>Regards,<br>Nadhiya C</p>
  </body>
</html>
"""

# Email setup
sender_email = "nadhiyamhnrj@gmail.com"
receiver_email = "rjraman100@gmail.com.com"
password = "arvw nvho rfmm dtbz"  # ⚠️ Replace with your Gmail App Password, not your login password

msg = MIMEMultipart("alternative")
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "GUID Matched and unmatched values"

# Attach HTML content
msg.attach(MIMEText(email_body, "html"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("nadhiyamhnrj@gmail.com", "arvw nvho rfmm dtbz")
    server.send_message(msg)
    print("✅ Email sent successfully with formatted table!")
except Exception as e:
    print("❌ Failed to send email:", e)
finally:
    server.quit()


# In[ ]:





# In[ ]:




