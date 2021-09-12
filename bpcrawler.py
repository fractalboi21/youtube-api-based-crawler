
#youtube data api search
#"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=YOURKEYWORD&type=video&key=YOURAPIKEY"
import requests
CORE = "https://www.googleapis.com/youtube/v3/search"
API_KEY = "AIzaSyDhzUyksZsIN-OsKTMNdDs_yh0_khuV90Y"
TYPE = ""
PARAMETERS = "snippet&contentDetails&maxResults=10&q=blackpill&type=video"
PART = f"?part={PARAMETERS}"
#url = f"{CORE_URL}{TYPE}{PART}&key={API_KEY}"
#url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId=UCBkNpeyvBO2TdPGVC_PsPUA&key="+API_KEY
#url = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&part=contentDetails&part=status&part=id&maxResults=50&playlistId=PLdPBL8cOjdzWQOdmxe6jhA5bhiKtxW0Oj&key="+API_KEY
url = CORE+"?part=snippet&q=blackpill&maxResults=50&key="+API_KEY

lst = []
count = 0
res = requests.get(url).json()
while bool(res.get("nextPageToken")):
    lst.append(res)
    token = res.get("nextPageToken")
    nurl = CORE+f"?part=snippet&q=blackpill&pageToken={token}&maxResults=50&key="+API_KEY
    res = requests.get(nurl).json()
    count += 1
    print(count)
    
    if res.get("nextPageToken"):
        pass
    else:
        break
    
    
