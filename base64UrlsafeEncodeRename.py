import glob, os, base64, re

rootDir = input('Path：')
for filename in glob.iglob(rootDir + "/**/*.rar", recursive=True): 
    #print(filename)
    fn = os.path.basename(filename)
    #print(fn)
    if "part" in fn:
        sp = re.split('\.', fn)
        fnsub = re.sub('\.part.*\.rar', '', fn)
        filenameenc = base64.urlsafe_b64encode(fnsub.encode())
        fb64 = filenameenc.decode()
        newfn = fb64 + '.' + sp[-2] + '.' + sp[-1]
    elif "rar" in fn:
        sp = re.split('\.', fn)
        fnsub = re.sub('\.rar', '', fn)
        filenameenc = base64.urlsafe_b64encode(fnsub.encode())
        fb64 = filenameenc.decode()
        newfn = fb64 + '.' + sp[-1]
    #print("Your filename is: " + fnsub)
    print("The urlsafe_base64 encoded filename is: " + fb64)
    print("newfn: " + os.path.dirname(filename) + "\\" + newfn + "\n")
    os.rename(filename, os.path.dirname(filename) + "\\" + newfn)
    