import glob, os, base64, re

rootDir = input('Path：')
for filename in glob.iglob(rootDir + "/**/*.rar", recursive=True): 
    #print(filename)
    fn = os.path.basename(filename)
    #print(fn)
    if "part" in fn:
        sp = re.split('\.', fn)
        fnsub = re.sub('\.part.*\.rar', '', fn)
        filenamedec = base64.urlsafe_b64decode(fnsub.encode())
        fb64 = filenamedec.decode()
        newfn = fb64 + '.' + sp[-2] + '.' + sp[-1]
    elif "rar" in fn:
        sp = re.split('\.', fn)
        fnsub = re.sub('\.rar', '', fn)
        filenamedec = base64.urlsafe_b64decode(fnsub.encode())
        fb64 = filenamedec.decode()
        newfn = fb64 + '.' + sp[-1]
    #print("Your filename is: " + fnsub)
    #print("The base64 decoded filename is: " + fb64)
    print("newfn: " + os.path.dirname(filename) + "\\" + newfn + "\n")
    os.rename(filename, os.path.dirname(filename) + "\\" + newfn)
    