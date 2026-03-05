import re
import sys

def anonymize(text):
    ip_pattern=r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    email_pattern=r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+\b'
    text=re.sub(ip_pattern,'[IP_REDACTED]',text)
    text=re.sub(email_pattern,'[EMAIL_REDACTED]',text)
    return text

def process_file(input_file,output_file):
    with open(input_file,'r',encoding='utf-8') as f:
        data=f.read()
    result=anonymize(data)
    with open(output_file,'w',encoding='utf-8') as f:
        f.write(result)

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: python anonymizer.py input.log output.log")
    else:
        process_file(sys.argv[1],sys.argv[2])
