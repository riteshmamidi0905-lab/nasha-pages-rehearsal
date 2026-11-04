"""Read-only observer for the disposable source transition; never changes settings."""
import argparse,datetime,hashlib,json,pathlib,time,urllib.request,urllib.error
p=argparse.ArgumentParser();p.add_argument('--seconds',type=int,default=180);p.add_argument('--interval',type=float,default=2);p.add_argument('--out',required=True);a=p.parse_args()
assert 0<a.seconds<=900 and a.interval>=1
url='https://riteshmamidi0905-lab.github.io/nasha-pages-rehearsal/'
expected='1119df2fc77225e73298481c1bacb1d34dcc953cea207e727fd49d64ba872926'
out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);end=time.monotonic()+a.seconds
with out.open('x') as f:
 while time.monotonic()<end:
  row={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url}
  try:
   req=urllib.request.Request(url+'?source_rehearsal='+str(time.time_ns()),headers={'Cache-Control':'no-cache'})
   with urllib.request.urlopen(req,timeout=10) as r:
    body=r.read();row.update(status=r.status,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),final_url=r.url)
   row['matches_fixture']=row['status']==200 and row['bytes']==230 and row['sha256']==expected
  except urllib.error.HTTPError as e:row.update(status=e.code,matches_fixture=False)
  except Exception as e:row.update(error=type(e).__name__,matches_fixture=False)
  f.write(json.dumps(row)+'\n');f.flush();time.sleep(min(a.interval,max(0,end-time.monotonic())))
print('Read-only transition observations saved:',str(out))
