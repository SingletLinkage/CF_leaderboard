import subprocess

def curl_request(url):
    curl_command = f'''
    curl '{url}' --compressed -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: cross-site' -H 'Connection: keep-alive' 
    -H 'Cookie: _ga_K230KVN22K=GS1.1.1700933127.1.1.1700934586.0.0.0; _ga=GA1.2.520676036.1700933127; X-User-Sha1=ee038a4867f79d01c66e117af04cdaf3215754b6; 39ce7=CFNFP4Q2; evercookie_etag=undefined; evercookie_cache=undefined; 70a7c28f3de=zdt9yx4idbfmpex3si; JSESSIONID=2107EBC444148FC8242AB6217BEB3399; cf_clearance=vxhXAbnSj2S.9GjInduRSycnex8WWP1VzYOiulnHBT0-1723263244-1.0.1.1-qnLbyNtP0RMuC3K0VM64orzqLcCYscWecTNqGqXokFsokxgGLVp2H9CMT.rtMejCWxNvg4_zT_FXs61whmK9kQ' 
    -H 'Priority: u=0, i' -H 'TE: trailers'  
    '''
    return subprocess.run(curl_command, shell=True, capture_output=True, text=True).stdout

if __name__ == "__main__":
    print(curl_request("https://codeforces.com/api/user.status?handle=qchaos"))

