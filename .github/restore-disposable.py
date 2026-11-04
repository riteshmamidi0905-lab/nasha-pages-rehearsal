"""Restore only the disposable tree; default mode is read-only and fails closed."""
import argparse,json,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--execute',action='store_true');a=p.parse_args()
repo='repos/riteshmamidi0905-lab/nasha-pages-rehearsal/'
expected='9f892bf91fb99823f4a4f143ca59e4bf78d6efa3'
target='021e9a9bfabee707d4b021076620665b283d933e'
def get(ep):
 return json.loads(subprocess.check_output(['gh','api','-H','Cache-Control: no-cache',repo+ep],text=True))
def source():
 mode=get('pages?restore_readback='+str(time.time_ns()))['build_type']
 if mode!='workflow':raise SystemExit('BLOCKED: Pages source is '+mode+'; stopping the entire operation before any further mutation.')
def head():
 h=get('git/ref/heads/main')['object']['sha']
 if h!=expected:raise SystemExit('BLOCKED: disposable main changed; inspect the new head before proceeding: '+h)
source();head()
if not a.execute:
 print('Read-only source/main checks passed; --execute was not supplied, so no commit or branch update was attempted.');raise SystemExit(0)
source();head()
tree=get('git/commits/'+target)['tree']['sha']
payload={'message':'Restore preserved disposable tree after independently confirmed Actions source','tree':tree,'parents':[expected]}
r=subprocess.run(['gh','api','--method','POST',repo+'git/commits','--input','-'],input=json.dumps(payload),text=True,capture_output=True,check=True)
commit=json.loads(r.stdout)['sha']
source();head()
# force=false refuses a non-fast-forward update if another writer advanced main.
subprocess.run(['gh','api','--method','PATCH',repo+'git/refs/heads/main','--input','-'],input=json.dumps({'sha':commit,'force':False}),text=True,capture_output=True,check=True)
assert get('git/ref/heads/main')['object']['sha']==commit
assert get('git/commits/'+commit)['tree']['sha']==tree
print('Disposable tree restored:',commit)
